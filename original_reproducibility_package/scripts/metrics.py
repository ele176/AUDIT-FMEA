"""Compute baseline DFMEA evaluation metrics from normalized CSV files.

Usage:
    python paper_project/02_experiment/scripts/metrics.py \
        --dfmea paper_project/02_experiment/data/dfmea_entries_template.csv

The script uses only the Python standard library so it can run without
additional dependencies during early protocol development.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
from collections import defaultdict
from pathlib import Path


HIGH_RISK_RPN = 180
HIGH_SEVERITY = 8
VALID_METHODS = {"M1", "M2", "M3", "M4"}


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


def compute_dfmea_metrics(rows: list[dict[str, str]]) -> dict[str, object]:
    by_method: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_method[(row.get("method_id") or "UNKNOWN").strip()].append(row)

    result: dict[str, object] = {}
    for method_id, method_rows in sorted(by_method.items()):
        invalid_map = {row.get("item_id", ""): row_invalid_reasons(row) for row in method_rows}
        invalid_count = sum(1 for reasons in invalid_map.values() if reasons)
        evidence_count = sum(1 for row in method_rows if has_evidence(row))
        high_risk_count = 0
        severity_high_count = 0
        rpn_mismatch_count = 0

        for row in method_rows:
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

        duplicates = duplicate_pairs(method_rows)
        total = len(method_rows)
        result[method_id] = {
            "row_count": total,
            "invalid_count": invalid_count,
            "invalid_rate": round(invalid_count / total, 3) if total else None,
            "duplicate_pair_count": len(duplicates),
            "duplicate_pairs": duplicates,
            "evidence_trace_count": evidence_count,
            "evidence_trace_rate": round(evidence_count / total, 3) if total else None,
            "high_risk_rpn_count": high_risk_count,
            "high_severity_count": severity_high_count,
            "rpn_mismatch_count": rpn_mismatch_count,
            "invalid_reasons_by_item": invalid_map,
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dfmea", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    payload = {"dfmea_metrics": compute_dfmea_metrics(read_csv(args.dfmea))}

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
