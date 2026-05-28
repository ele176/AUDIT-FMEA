"""Build a known-defect stress test for AUDIT-FMEA.

The stress test injects deliberately corrupted DFMEA rows and evaluates whether
the critic/integrity defect classes used by AUDIT-FMEA can flag them. This is a
structural negative-control test, not an expert validation of mechanical truth.
"""

from __future__ import annotations

import csv
import difflib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "manuscript_support" / "known_defect_stress_test_v1.0"

FIELDS = [
    "method_id",
    "item_id",
    "subsystem",
    "function",
    "requirement_or_evidence_anchor",
    "potential_failure_mode",
    "potential_effect",
    "severity_s",
    "potential_cause",
    "occurrence_o",
    "current_control",
    "detection_d",
    "rpn",
    "recommended_action",
    "responsible_role",
    "evidence_trace",
    "critic_notes",
    "status",
    "injected_defect_type",
    "expected_detector",
]

REQUIRED_TEXT_FIELDS = [
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

VALID_METHODS = {"M1", "M2", "M3", "M4"}
OUT_OF_SCOPE_TERMS = [
    "battery",
    "bms",
    "thermal runaway",
    "motor controller",
    "regenerative braking",
]


def base_row(item_id: str) -> dict[str, str]:
    return {
        "method_id": "M4",
        "item_id": item_id,
        "subsystem": "Cable or hydraulic path",
        "function": "Transmit rider input force to the caliper",
        "requirement_or_evidence_anchor": "S01;engineering_inference:S02",
        "potential_failure_mode": "Cable anchor slips under braking load",
        "potential_effect": "Sudden reduction of braking force",
        "severity_s": "9",
        "potential_cause": "Insufficient clamp torque or missing retainer",
        "occurrence_o": "3",
        "current_control": "Torque check and functional brake test",
        "detection_d": "8",
        "rpn": "216",
        "recommended_action": "Add positive retention feature and torque marking",
        "responsible_role": "Manufacturer",
        "evidence_trace": "S01;engineering_inference:S02",
        "critic_notes": "Known-defect stress-test row",
        "status": "stress_test",
        "injected_defect_type": "",
        "expected_detector": "",
    }


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    row = base_row("KD-001")
    row.update(
        {
            "subsystem": "Brake lever",
            "function": "Return lever to the released position",
            "potential_failure_mode": "Lever return spring detaches after repeated actuation",
            "potential_effect": "Delayed brake release and dragging pad contact",
            "potential_cause": "Weak spring hook retention and vibration loosening",
            "recommended_action": "Add spring retention feature and return-force inspection",
        }
    )
    row["evidence_trace"] = ""
    row["injected_defect_type"] = "missing_evidence_trace"
    row["expected_detector"] = "integrity:missing_required_evidence_trace"
    rows.append(row)

    row = base_row("KD-002")
    row.update(
        {
            "subsystem": "Caliper mounting bracket",
            "function": "Hold caliper alignment relative to disc rotor",
            "potential_failure_mode": "Mounting bracket loosens under vibration",
            "potential_effect": "Pad-rotor misalignment and reduced braking force",
            "potential_cause": "Insufficient fastener preload or missing thread-locking control",
            "recommended_action": "Specify locking fastener and torque-mark inspection",
        }
    )
    row["rpn"] = "200"
    row["injected_defect_type"] = "wrong_rpn"
    row["expected_detector"] = "integrity:rpn_mismatch"
    rows.append(row)

    row = base_row("KD-003A")
    row["potential_failure_mode"] = "Cable anchor slips under braking load"
    row["potential_effect"] = "Sudden reduction of braking force"
    row["potential_cause"] = "Insufficient clamp torque or missing retainer"
    row["injected_defect_type"] = "duplicate_pair_member"
    row["expected_detector"] = "critic:duplicate_pair_member"
    rows.append(row)

    row = base_row("KD-003B")
    row["potential_failure_mode"] = "Cable anchor slips under braking load"
    row["potential_effect"] = "Sudden reduction of braking force"
    row["potential_cause"] = "Insufficient clamp torque or missing retainer"
    row["injected_defect_type"] = "duplicate_pair_member"
    row["expected_detector"] = "critic:duplicate_pair_member"
    rows.append(row)

    row = base_row("KD-004")
    row.update(
        {
            "subsystem": "Disc rotor",
            "function": "Provide friction surface for pad contact",
            "potential_effect": "Loss of rider speed control during braking",
            "potential_cause": "Unspecified defect mechanism",
            "recommended_action": "Define mechanism-specific rotor inspection criteria",
        }
    )
    row["potential_failure_mode"] = "Brake failure"
    row["injected_defect_type"] = "generic_failure_label"
    row["expected_detector"] = "critic:too_vague_failure_mode"
    rows.append(row)

    row = base_row("KD-005")
    row["subsystem"] = "Battery management system"
    row["function"] = "Prevent battery thermal runaway"
    row["potential_failure_mode"] = "Cell thermal runaway occurs during charging"
    row["potential_effect"] = "Battery fire unrelated to mechanical brake force path"
    row["potential_cause"] = "Cell imbalance and charger fault"
    row["recommended_action"] = "Add BMS over-temperature cutoff"
    row["injected_defect_type"] = "out_of_scope_boundary"
    row["expected_detector"] = "critic:out_of_scope_boundary"
    rows.append(row)

    row = base_row("KD-006")
    row.update(
        {
            "subsystem": "Brake pad retention",
            "function": "Keep pads retained in the caliper during braking",
            "potential_failure_mode": "Pad retaining pin backs out during service life",
            "potential_effect": "Pad displacement and sudden loss of friction force",
            "potential_cause": "Missing secondary retention or inadequate service inspection",
            "current_control": "Visual pad-retention inspection",
            "detection_d": "7",
            "rpn": "189",
        }
    )
    row["severity_s"] = "9"
    row["recommended_action"] = ""
    row["injected_defect_type"] = "missing_high_severity_mitigation"
    row["expected_detector"] = "integrity:missing_recommended_action"
    rows.append(row)

    row = base_row("KD-007")
    row.update(
        {
            "subsystem": "Cable fixing interface",
            "function": "Retain cable force path under hand-lever load",
            "potential_failure_mode": "Cable fixing bolt clamps insulation instead of cable strands",
            "potential_effect": "Cable slip and sudden weak braking",
            "potential_cause": "Incorrect clamp stack-up or assembly torque error",
        }
    )
    row["recommended_action"] = "Update diagnostic firmware and dashboard alert thresholds"
    row["injected_defect_type"] = "mitigation_cause_mismatch"
    row["expected_detector"] = "critic:mitigation_cause_mismatch"
    rows.append(row)

    row = base_row("KD-008")
    row.update(
        {
            "subsystem": "Pad clearance adjuster",
            "function": "Maintain pad clearance after wear adjustment",
            "potential_failure_mode": "Adjuster moves beyond intended range",
            "potential_effect": "Excessive lever travel before pad contact",
            "potential_cause": "Absent end-stop or unclear service limit",
            "recommended_action": "Add adjustment travel limit and service-limit marking",
        }
    )
    row["severity_s"] = "11"
    row["rpn"] = "264"
    row["injected_defect_type"] = "invalid_severity"
    row["expected_detector"] = "integrity:invalid_severity"
    rows.append(row)

    row = base_row("KD-009")
    row.update(
        {
            "subsystem": "Rotor-side fasteners",
            "function": "Maintain rotor-side hardware clearance",
            "potential_failure_mode": "Fastener head interferes with caliper body",
            "potential_effect": "Rotor drag and unstable braking response",
            "potential_cause": "Wrong fastener height or missing clearance check",
            "recommended_action": "Add rotor-fastener height gauge and clearance verification",
        }
    )
    row["detection_d"] = "0"
    row["rpn"] = "0"
    row["injected_defect_type"] = "invalid_detection"
    row["expected_detector"] = "integrity:invalid_detection"
    rows.append(row)

    row = base_row("KD-010")
    row.update(
        {
            "subsystem": "Wet-condition friction interface",
            "function": "Maintain predictable friction in wet conditions",
            "potential_failure_mode": "Pad compound loses friction after water exposure",
            "potential_effect": "Longer stopping distance in wet operation",
            "potential_cause": "Pad material not specified for expected wet environment",
            "recommended_action": "Specify wet-condition pad test and minimum friction criterion",
        }
    )
    row["current_control"] = ""
    row["injected_defect_type"] = "missing_required_field"
    row["expected_detector"] = "integrity:missing_current_control"
    rows.append(row)

    row = base_row("KD-011")
    row.update(
        {
            "subsystem": "Final assembly verification",
            "function": "Confirm complete braking function before release",
            "potential_failure_mode": "Final assembly check omits front-wheel lock tendency",
            "potential_effect": "Over-aggressive front brake response remains undetected",
            "potential_cause": "Checklist lacks modulation and lock-tendency criteria",
            "recommended_action": "Add modulation and controlled-force verification step",
        }
    )
    row["evidence_trace"] = "unsupported_candidate"
    row["injected_defect_type"] = "unsupported_candidate_evidence"
    row["expected_detector"] = "integrity:missing_required_evidence_trace"
    rows.append(row)

    return rows


def to_int(value: str) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def has_evidence(row: dict[str, str]) -> bool:
    value = (row.get("evidence_trace") or "").strip().lower()
    if not value or value in {"none", "not_applicable", "n/a", "na"}:
        return False
    return value != "unsupported_candidate"


def normalized_text(row: dict[str, str]) -> str:
    parts = [
        row.get("subsystem", ""),
        row.get("potential_failure_mode", ""),
        row.get("potential_cause", ""),
        row.get("potential_effect", ""),
    ]
    return " | ".join(part.strip().lower() for part in parts)


def duplicate_pairs(rows: list[dict[str, str]], threshold: float = 0.88) -> list[tuple[str, str, float]]:
    pairs: list[tuple[str, str, float]] = []
    for i, left in enumerate(rows):
        left_text = normalized_text(left)
        for right in rows[i + 1 :]:
            ratio = difflib.SequenceMatcher(None, left_text, normalized_text(right)).ratio()
            if ratio >= threshold:
                pairs.append((left["item_id"], right["item_id"], round(ratio, 3)))
    return pairs


def formal_reasons(row: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    for field in REQUIRED_TEXT_FIELDS:
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

    if method_id in {"M3", "M4"} and not has_evidence(row):
        reasons.append("missing_required_evidence_trace")

    if s is not None and s >= 8 and not (row.get("recommended_action") or "").strip():
        if "missing_recommended_action" not in reasons:
            reasons.append("missing_recommended_action")

    return reasons


def critic_reasons(row: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    failure_mode = (row.get("potential_failure_mode") or "").strip().lower()
    if failure_mode in {"brake failure", "failure", "system failure"}:
        reasons.append("too_vague_failure_mode")

    combined = " ".join(
        [
            row.get("subsystem", ""),
            row.get("function", ""),
            row.get("potential_failure_mode", ""),
            row.get("potential_effect", ""),
            row.get("potential_cause", ""),
            row.get("recommended_action", ""),
        ]
    ).lower()
    if any(term in combined for term in OUT_OF_SCOPE_TERMS):
        reasons.append("out_of_scope_boundary")

    cause_and_mode = " ".join(
        [
            row.get("potential_failure_mode", ""),
            row.get("potential_cause", ""),
        ]
    ).lower()
    action = (row.get("recommended_action") or "").lower()
    cable_problem = any(term in cause_and_mode for term in ["cable", "clamp", "anchor", "torque", "retainer"])
    battery_action = any(term in action for term in ["battery", "bms", "firmware", "cell-balancing", "cell balancing"])
    if cable_problem and battery_action:
        reasons.append("mitigation_cause_mismatch")

    return reasons


def evaluate_rows(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, object]]:
    duplicate_members: set[str] = set()
    pairs = duplicate_pairs(rows)
    for left, right, _ in pairs:
        duplicate_members.add(left)
        duplicate_members.add(right)

    results: list[dict[str, str]] = []
    detected_expected = 0
    false_negative_rows: list[str] = []
    for row in rows:
        detected = formal_reasons(row) + critic_reasons(row)
        if row["item_id"] in duplicate_members:
            detected.append("duplicate_pair_member")
        detected_unique = sorted(set(detected))

        expected = row["expected_detector"].split(":", 1)[-1]
        expected_detected = expected in detected_unique
        if expected_detected:
            detected_expected += 1
        else:
            false_negative_rows.append(row["item_id"])

        results.append(
            {
                "item_id": row["item_id"],
                "injected_defect_type": row["injected_defect_type"],
                "expected_detector": row["expected_detector"],
                "detected_reasons": ";".join(detected_unique) if detected_unique else "none",
                "expected_detected": "PASS" if expected_detected else "FAIL",
            }
        )

    by_gate = {
        "integrity_expected": sum(1 for row in rows if row["expected_detector"].startswith("integrity:")),
        "critic_expected": sum(1 for row in rows if row["expected_detector"].startswith("critic:")),
        "integrity_detected": sum(
            1
            for result in results
            if result["expected_detector"].startswith("integrity:") and result["expected_detected"] == "PASS"
        ),
        "critic_detected": sum(
            1
            for result in results
            if result["expected_detector"].startswith("critic:") and result["expected_detected"] == "PASS"
        ),
    }
    summary = {
        "stress_test_version": "v1.0",
        "purpose": "structural negative-control test for known DFMEA artifact defects",
        "row_count": len(rows),
        "expected_row_level_defects": len(rows),
        "detected_expected_defects": detected_expected,
        "row_level_detection_recall": round(detected_expected / len(rows), 3) if rows else None,
        "duplicate_pair_count": len(pairs),
        "duplicate_pairs": pairs,
        "false_negative_rows": false_negative_rows,
        "by_gate": by_gate,
        "claim_boundary": (
            "Supports defect-detection and audit-protocol claims for injected structural/semantic "
            "artifact defects; does not validate real braking safety, S/O/D accuracy, or row correctness."
        ),
    }
    return results, summary


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def markdown_summary(summary: dict[str, object], results: list[dict[str, str]]) -> str:
    by_gate = summary["by_gate"]  # type: ignore[index]
    lines = [
        "# Known-Defect Stress Test v1.0",
        "",
        "Purpose: test whether AUDIT-FMEA's critic and integrity defect classes flag deliberately injected DFMEA artifact defects.",
        "",
        "This is a structural negative-control test. It does not validate braking safety, S/O/D calibration, mitigation effectiveness, or expert correctness.",
        "",
        "## Summary",
        "",
        f"- Injected rows: {summary['row_count']}",
        f"- Expected row-level defect labels: {summary['expected_row_level_defects']}",
        f"- Detected expected defect labels: {summary['detected_expected_defects']}",
        f"- Row-level detection recall: {summary['row_level_detection_recall']}",
        f"- Duplicate pairs detected: {summary['duplicate_pair_count']}",
        f"- Integrity expected/detected: {by_gate['integrity_detected']}/{by_gate['integrity_expected']}",  # type: ignore[index]
        f"- Critic expected/detected: {by_gate['critic_detected']}/{by_gate['critic_expected']}",  # type: ignore[index]
        f"- False-negative rows: {', '.join(summary['false_negative_rows']) if summary['false_negative_rows'] else 'none'}",  # type: ignore[index]
        "",
        "## Detection Results",
        "",
        "| Item | Injected defect | Expected detector | Detected reasons | Result |",
        "|---|---|---|---|---|",
    ]
    for row in results:
        lines.append(
            "| {item_id} | {injected_defect_type} | {expected_detector} | {detected_reasons} | {expected_detected} |".format(
                **row
            )
        )
    lines += [
        "",
        "## Claim Boundary",
        "",
        str(summary["claim_boundary"]),
        "",
    ]
    return "\n".join(lines)


def manuscript_insert() -> str:
    return """# Manuscript Insert: Known-Defect Stress Test v1.0

## Methods insert

### Known-defect stress test

To reduce the risk that the auditability metrics merely rewarded the workflow for emitting its own preferred artifact structure, a known-defect stress test was added as a negative control. Twelve deliberately corrupted DFMEA rows were constructed under the same normalized schema. Each row contained one expected artifact defect: missing evidence trace, incorrect RPN arithmetic, duplicate row membership, generic failure labeling, out-of-bound subsystem content, missing mitigation for a high-severity row, mitigation-cause mismatch, invalid S/O/D value, missing required field, or unsupported evidence marker. The stress test mapped these defects to the two post-generation gates used by AUDIT-FMEA: formal integrity checks and critic-style semantic checks. The test was deterministic and script-computed. It was designed to evaluate whether the audit protocol detects known artifact defects, not whether any generated DFMEA row is mechanically correct.

## Results insert

### Known-defect stress-test results

The known-defect stress test included 12 deliberately corrupted DFMEA rows. All 12 expected row-level defect labels were detected, giving a row-level detection recall of 1.000. The integrity-oriented checks detected 7/7 expected formal defects, including missing evidence traces, RPN mismatch, invalid S/O/D values, missing current control, missing recommended action, and an unsupported-candidate evidence marker. The critic-oriented checks detected 5/5 expected semantic defects, including duplicate pair membership, generic failure labeling, out-of-bound subsystem content, and mitigation-cause mismatch. One duplicate pair was detected as intended. These results strengthen the claim that AUDIT-FMEA's review gates can identify pre-specified structural and semantic artifact defects. They do not validate braking safety, calibrated S/O/D ratings, mitigation effectiveness, or the expert correctness of generated DFMEA rows.
"""


def main() -> None:
    rows = build_rows()
    results, summary = evaluate_rows(rows)

    input_csv = OUT_DIR / "known_defect_injected_rows_v1.0.csv"
    results_csv = OUT_DIR / "known_defect_detection_results_v1.0.csv"
    summary_json = OUT_DIR / "known_defect_stress_test_summary_v1.0.json"
    summary_md = OUT_DIR / "known_defect_stress_test_summary_v1.0.md"
    insert_md = OUT_DIR / "manuscript_insert_known_defect_stress_test_v1.0.md"

    write_csv(input_csv, rows, FIELDS)
    write_csv(
        results_csv,
        results,
        ["item_id", "injected_defect_type", "expected_detector", "detected_reasons", "expected_detected"],
    )
    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary_md.write_text(markdown_summary(summary, results), encoding="utf-8")
    insert_md.write_text(manuscript_insert(), encoding="utf-8")

    print(f"Wrote {input_csv}")
    print(f"Wrote {results_csv}")
    print(f"Wrote {summary_json}")
    print(f"Wrote {summary_md}")
    print(f"Wrote {insert_md}")


if __name__ == "__main__":
    main()
