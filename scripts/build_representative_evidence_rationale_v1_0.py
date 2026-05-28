"""Build a representative row-level evidence rationale appendix for AUDIT-FMEA."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAIN_DIR = ROOT / "manuscript_support" / "data_evidence_chain_v1.0"
OUT_DIR = ROOT / "manuscript_support" / "representative_evidence_rationale_v1.0"

SELECTED_IDS = [
    "M4-004",
    "M4-006",
    "M4-012",
    "M4-015",
    "M4-018",
    "C2-M4-004",
    "C2-M4-006",
    "C2-M4-007",
    "C2-M4-013",
    "C2-M4-018",
]

RATIONALE_NOTES = {
    "M4-004": {
        "source_note": "Public micromobility hazard context supports brake attachment / cable-path concern; construction-standard material supports treating force-path retention as design-review relevant.",
        "inference_boundary": "Clamp torque, positive retention, and assembly poka-yoke are engineering extensions from force-path reasoning.",
        "remains_unverified": "Actual failure frequency, exact clamp design, and mitigation effectiveness.",
    },
    "M4-006": {
        "source_note": "Public hazard context supports intermittent braking / control-loss concern; terminology source supports braking-response boundary.",
        "inference_boundary": "Kinked cable, sticking linkage, and contamination mechanisms are candidate mechanical explanations.",
        "remains_unverified": "Specific root cause in any product and calibrated S/O/D ratings.",
    },
    "M4-012": {
        "source_note": "Construction-standard material supports treating repeated braking and brake performance as design-review context.",
        "inference_boundary": "Thermal fade mechanism, lining material recommendation, and temperature-grade action are engineering-inference items.",
        "remains_unverified": "Thermal load, pad material data, stopping distance, and fade threshold.",
    },
    "M4-015": {
        "source_note": "Public micromobility hazard context and construction-standard material support retaining brake mounting hardware inside the review boundary.",
        "inference_boundary": "Thread-locking, torque marking, and pack-out verification are design-control inferences.",
        "remains_unverified": "Fastener design, vibration spectrum, and durability performance.",
    },
    "M4-018": {
        "source_note": "Public hazard context supports abrupt or unexpected brake engagement as a rider-control concern.",
        "inference_boundary": "Lever ratio, pad friction, and wheel-lock tendency are mechanism-level hypotheses to be checked by an engineer.",
        "remains_unverified": "Wheel-lock dynamics, rider response, friction curve, and stopping-distance behavior.",
    },
    "C2-M4-004": {
        "source_note": "Bicycle braking regulation and mechanical disc brake manual support cable anchoring, cable condition, and torque/assembly checks.",
        "inference_boundary": "Positive cable retention and strand-damage inspection are design/control refinements.",
        "remains_unverified": "Actual clamp geometry, strand damage rate, and field occurrence.",
    },
    "C2-M4-006": {
        "source_note": "The TRP/Tektro recall directly supports actuator-arm over-rotation and caliper-part dislocation as a mechanical disc brake failure mechanism.",
        "inference_boundary": "Travel-stop verification and containment feature are proposed engineering controls.",
        "remains_unverified": "Applicability to non-recalled calipers and mitigation performance.",
    },
    "C2-M4-007": {
        "source_note": "Two CPSC recall sources support caliper failure, loss of braking power, and loss-of-control effects.",
        "inference_boundary": "Supplier screening, proof test, and recall traceability are quality-control recommendations.",
        "remains_unverified": "Failure rate, supplier process capability, and root-cause distribution.",
    },
    "C2-M4-013": {
        "source_note": "Mechanical disc brake manual supports treating oil/grease contamination of rotor or pads as a direct maintenance and performance concern.",
        "inference_boundary": "Cleaning protocol and friction-material handling procedure are control extensions.",
        "remains_unverified": "Contamination probability, friction degradation magnitude, and cleaning effectiveness.",
    },
    "C2-M4-018": {
        "source_note": "Bicycle braking regulation and mechanical disc brake manual support final brake attachment, adjustment, and rotor-interference checks.",
        "inference_boundary": "End-of-line checklist design and functional verification scope are workflow-level inferences.",
        "remains_unverified": "Whether a specific assembly process omits the check and whether added checks reduce defects.",
    },
}

FIELDS = [
    "item_id",
    "case_id",
    "subsystem",
    "failure_mode",
    "effect",
    "cause",
    "rpn",
    "evidence_trace",
    "support_class",
    "source_basis_summary",
    "source_note",
    "inference_boundary",
    "remains_unverified",
    "reader_check",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def build_rows() -> list[dict[str, str]]:
    rows_by_id = {row["item_id"]: row for row in read_csv(CHAIN_DIR / "row_level_evidence_chain_v1.0.csv")}
    output: list[dict[str, str]] = []
    for item_id in SELECTED_IDS:
        source = rows_by_id[item_id]
        notes = RATIONALE_NOTES[item_id]
        output.append(
            {
                "item_id": item_id,
                "case_id": source["case_id"],
                "subsystem": source["subsystem"],
                "failure_mode": source["failure_mode"],
                "effect": source["effect"],
                "cause": source["cause"],
                "rpn": source["rpn"],
                "evidence_trace": source["evidence_trace"],
                "support_class": source["evidence_support_class"],
                "source_basis_summary": source["source_basis_summary"],
                "source_note": notes["source_note"],
                "inference_boundary": notes["inference_boundary"],
                "remains_unverified": notes["remains_unverified"],
                "reader_check": source["recommended_reader_check"],
            }
        )
    return output


def markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "# Representative Row-Level Evidence Rationale v1.0",
        "",
        "Purpose: make a small set of AUDIT-FMEA row-level evidence boundaries easier to inspect.",
        "",
        "This appendix is not an expert validation file. It explains source support, engineering-inference boundaries, and remaining unverified claims for representative rows.",
        "",
        "| Item | Case | Failure mode | Evidence trace | Support class | Source note | Inference boundary | Remains unverified |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {item_id} | {case_id} | {failure_mode} | {evidence_trace} | {support_class} | {source_note} | {inference_boundary} | {remains_unverified} |".format(
                **row
            )
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    rows = build_rows()
    csv_path = OUT_DIR / "representative_row_level_evidence_rationale_v1.0.csv"
    md_path = OUT_DIR / "representative_row_level_evidence_rationale_v1.0.md"
    write_csv(csv_path, rows)
    md_path.write_text(markdown(rows), encoding="utf-8")

    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
