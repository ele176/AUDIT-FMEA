"""Summarize repeated-run and ablation metrics for AUDIT-FMEA.

The script expects normalized DFMEA CSV files in a runs directory. File names
must follow:

    <variant>_run<NN>.csv

Examples:
    M2_run01.csv
    M4_full_run03.csv
    M4_no_critic_run02.csv

The script computes the same structural metrics as the original AEI manuscript,
then reports per-variant mean, standard deviation, min, and max.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev


HIGH_RISK_RPN = 180
HIGH_SEVERITY = 8
VALID_METHODS = {"M1", "M2", "M3", "M4"}
RUN_RE = re.compile(r"^(?P<variant>.+)_run(?P<run_id>\d+)\.csv$", re.IGNORECASE)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def to_int(value: str) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def normalized_text(row: dict[str, str]) -> str:
    parts = [
        row.get("subsystem", ""),
        row.get("potential_failure_mode", ""),
        row.get("potential_cause", ""),
        row.get("potential_effect", ""),
    ]
    return " | ".join(part.strip().lower() for part in parts)


def has_evidence(row: dict[str, str]) -> bool:
    value = (row.get("evidence_trace") or "").strip().lower()
    if not value or value in {"none", "not_applicable", "n/a", "na"}:
        return False
    return value != "unsupported_candidate"


def row_invalid_reasons(row: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    required_text = [
        "method_id",
        "item_id",
        "subsystem",
        "function",
        "potential_failure_mode",
        "potential_effect",
        "potential_cause",
        "current_control",
        "recommended_action",
        "status",
    ]
    for field in required_text:
        if not (row.get(field) or "").strip():
            reasons.append(f"missing_{field}")

    method_id = (row.get("method_id") or "").strip()
    if method_id not in VALID_METHODS:
        reasons.append("invalid_method_id")

    s = to_int(row.get("severity_s", ""))
    o = to_int(row.get("occurrence_o", ""))
    d = to_int(row.get("detection_d", ""))
    rpn = to_int(row.get("rpn", ""))

    if s is None or not 1 <= s <= 10:
        reasons.append("invalid_severity")
    if o is None or not 1 <= o <= 10:
        reasons.append("invalid_occurrence")
    if d is None or not 1 <= d <= 10:
        reasons.append("invalid_detection")
    if rpn is None:
        reasons.append("invalid_rpn")
    if None not in (s, o, d, rpn) and s * o * d != rpn:
        reasons.append("rpn_mismatch")

    failure_mode = (row.get("potential_failure_mode") or "").strip().lower()
    if failure_mode in {"brake failure", "failure", "system failure"}:
        reasons.append("too_vague_failure_mode")

    if method_id in {"M3", "M4"} and not has_evidence(row):
        reasons.append("missing_required_evidence_trace")

    return reasons


def duplicate_pairs(rows: list[dict[str, str]], threshold: float = 0.88) -> list[tuple[str, str, float]]:
    pairs: list[tuple[str, str, float]] = []
    for i, left in enumerate(rows):
        left_text = normalized_text(left)
        for right in rows[i + 1 :]:
            ratio = difflib.SequenceMatcher(None, left_text, normalized_text(right)).ratio()
            if ratio >= threshold:
                pairs.append((left.get("item_id", ""), right.get("item_id", ""), round(ratio, 3)))
    return pairs


def compute_metrics(rows: list[dict[str, str]]) -> dict[str, object]:
    invalid_map = {row.get("item_id", ""): row_invalid_reasons(row) for row in rows}
    invalid_count = sum(1 for reasons in invalid_map.values() if reasons)
    evidence_count = sum(1 for row in rows if has_evidence(row))
    high_risk_count = 0
    severity_high_count = 0
    rpn_mismatch_count = 0

    for row in rows:
        s = to_int(row.get("severity_s", ""))
        o = to_int(row.get("occurrence_o", ""))
        d = to_int(row.get("detection_d", ""))
        rpn = to_int(row.get("rpn", ""))
        if s is not None and s >= HIGH_SEVERITY:
            severity_high_count += 1
        if rpn is not None and rpn >= HIGH_RISK_RPN:
            high_risk_count += 1
        if None not in (s, o, d, rpn) and s * o * d != rpn:
            rpn_mismatch_count += 1

    duplicates = duplicate_pairs(rows)
    total = len(rows)
    return {
        "row_count": total,
        "invalid_count": invalid_count,
        "invalid_rate": round(invalid_count / total, 3) if total else None,
        "duplicate_pair_count": len(duplicates),
        "evidence_trace_count": evidence_count,
        "evidence_trace_rate": round(evidence_count / total, 3) if total else None,
        "high_risk_rpn_count": high_risk_count,
        "high_severity_count": severity_high_count,
        "rpn_mismatch_count": rpn_mismatch_count,
        "duplicate_pairs": duplicates,
        "invalid_reasons_by_item": invalid_map,
    }


def parse_run_file(path: Path) -> tuple[str, str] | None:
    match = RUN_RE.match(path.name)
    if not match:
        return None
    return match.group("variant"), match.group("run_id")


def summarize(values: list[float | int | None]) -> dict[str, float | int | None]:
    clean = [float(v) for v in values if v is not None]
    if not clean:
        return {"mean": None, "sd": None, "min": None, "max": None}
    return {
        "mean": round(mean(clean), 3),
        "sd": round(stdev(clean), 3) if len(clean) > 1 else 0.0,
        "min": round(min(clean), 3),
        "max": round(max(clean), 3),
    }


def build_summary(run_metrics: list[dict[str, object]]) -> dict[str, object]:
    by_variant: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in run_metrics:
        by_variant[str(item["variant"])].append(item)

    metric_names = [
        "row_count",
        "invalid_rate",
        "duplicate_pair_count",
        "evidence_trace_rate",
        "high_risk_rpn_count",
        "high_severity_count",
        "rpn_mismatch_count",
    ]

    summary: dict[str, object] = {}
    for variant, rows in sorted(by_variant.items()):
        summary[variant] = {
            "n_runs": len(rows),
            "metrics": {
                name: summarize([row["metrics"].get(name) for row in rows])  # type: ignore[index]
                for name in metric_names
            },
        }
    return summary


def markdown_table(summary: dict[str, object]) -> str:
    headers = [
        "Variant",
        "n",
        "Rows mean+/-sd",
        "Invalid rate mean+/-sd",
        "Duplicate pairs mean+/-sd",
        "Evidence trace mean+/-sd",
        "High-RPN mean+/-sd",
        "High-severity mean+/-sd",
        "RPN mismatches mean+/-sd",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]

    def fmt(metric: dict[str, object]) -> str:
        if metric["mean"] is None:
            return "NA"
        return f"{metric['mean']}+/-{metric['sd']}"

    for variant, payload in summary.items():
        metrics = payload["metrics"]  # type: ignore[index]
        lines.append(
            "| "
            + " | ".join(
                [
                    variant,
                    str(payload["n_runs"]),  # type: ignore[index]
                    fmt(metrics["row_count"]),
                    fmt(metrics["invalid_rate"]),
                    fmt(metrics["duplicate_pair_count"]),
                    fmt(metrics["evidence_trace_rate"]),
                    fmt(metrics["high_risk_rpn_count"]),
                    fmt(metrics["high_severity_count"]),
                    fmt(metrics["rpn_mismatch_count"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    run_metrics: list[dict[str, object]] = []
    for path in sorted(args.runs.glob("*.csv")):
        parsed = parse_run_file(path)
        if parsed is None:
            continue
        variant, run_id = parsed
        rows = read_csv(path)
        run_metrics.append(
            {
                "variant": variant,
                "run_id": run_id,
                "file": path.name,
                "metrics": compute_metrics(rows),
            }
        )

    payload = {
        "runs_dir": str(args.runs),
        "run_count": len(run_metrics),
        "runs": run_metrics,
        "summary": build_summary(run_metrics),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.out.with_suffix(".md").write_text(markdown_table(payload["summary"]), encoding="utf-8")
    print(f"Wrote {args.out}")
    print(f"Wrote {args.out.with_suffix('.md')}")


if __name__ == "__main__":
    main()
