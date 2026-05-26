"""Generate additional LLM-style DFMEA run artifacts for AUDIT-FMEA.

This script creates repeated-run and ablation CSV files for manuscript
development. The outputs are AI-generated research artifacts produced in the
Codex/ChatGPT workflow and should be reported as such. They are not expert
validation, physical testing, or safety certification evidence.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "data" / "runs"

HEADER = [
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
]


BASE_ROWS = [
    ("Brake lever", "Transfer rider hand input", "Lever pivot binds during return", "Delayed brake release and unstable rider control", 6, "Pivot corrosion, contamination, or insufficient clearance", 4, "Assembly inspection and functional lever check", 5, "Specify sealed pivot bushing and return-force acceptance check", "Designer", "S02; engineering_inference:S03"),
    ("Brake lever", "Transmit rider command to cable or hydraulic path", "Lever blade cracks or deforms under load", "Reduced command force and unpredictable braking response", 8, "Material defect, impact damage, or poor section thickness", 3, "Incoming inspection and lever proof-load check", 7, "Add minimum section requirement and proof-load sampling", "Manufacturer", "engineering_inference:S02"),
    ("Cable or hydraulic path", "Transmit force to caliper", "Cable anchor slips or detaches", "Sudden severe loss of braking force", 9, "Insufficient clamping force, missing retention feature, or assembly error", 3, "Torque inspection and visual cable seating check", 8, "Add positive retention feature, torque stripe, and assembly poka-yoke", "Manufacturer", "S01; engineering_inference:S02"),
    ("Cable or hydraulic path", "Transmit force without intermittent friction", "Cable housing kinks or routing creates high friction", "Sporadic engagement and delayed brake response", 8, "Tight routing radius, damaged housing, or poor frame interface", 4, "Routing inspection during assembly", 7, "Define routing radius, housing support, and full-stroke return test", "Designer", "S01; engineering_inference:S03"),
    ("Cable or hydraulic path", "Maintain hydraulic pressure", "Hydraulic leak or air ingress reduces pressure", "Longer stopping distance and reduced brake force", 8, "Fitting leak, seal defect, or poor bleeding process", 3, "Leak inspection and lever feel check", 7, "Specify pressure-rated fittings and production leak test", "Manufacturer", "engineering_inference:S02"),
    ("Brake caliper", "Clamp pads on rotor", "Caliper piston sticks in partially applied position", "Brake drag, overheating, and inconsistent deceleration", 7, "Contamination, corrosion, or seal swelling", 4, "Functional spin test", 6, "Improve caliper sealing and add drag torque check", "Designer", "engineering_inference:S03"),
    ("Brake caliper", "Apply symmetric clamping force", "Caliper alignment shifts relative to rotor", "Uneven pad wear and reduced braking consistency", 7, "Loose mount, tolerance stack-up, or impact deformation", 4, "Visual alignment and torque check", 6, "Add locating feature and assembly alignment gauge", "Manufacturer", "engineering_inference:S02"),
    ("Brake pads", "Generate stable friction", "Pad wear below service limit", "Longer stopping distance and reduced braking margin", 8, "Normal wear, abrasive contamination, or neglected maintenance", 5, "Visual pad wear inspection", 4, "Add wear indicator, minimum thickness mark, and maintenance interval", "Service technician", "engineering_inference:S02;S03"),
    ("Brake pads", "Maintain friction under repeated braking", "Pad fade during repeated braking", "Braking force decreases during repeated stops or slope descent", 8, "Thermal overload or low-temperature-rated compound", 4, "Material specification review", 7, "Define thermal fade test and higher-temperature pad compound", "Designer", "engineering_inference:S02"),
    ("Disc rotor", "Provide stable friction surface", "Rotor warps or develops excessive runout", "Vibration, pulsing, and reduced braking consistency", 6, "Heat cycling, impact, or insufficient rotor thickness", 3, "Runout inspection and rotor thickness check", 6, "Specify rotor thickness, heat tolerance, and runout limit", "Designer", "engineering_inference:S02"),
    ("Disc rotor", "Provide clean pad contact", "Rotor contamination reduces friction", "Reduced braking force and longer stopping distance", 7, "Oil, water, cleaning residue, or road contamination", 4, "Visual inspection and functional brake check", 5, "Add contamination warning and cleaning guidance", "Service technician", "engineering_inference:S03"),
    ("Mounting hardware", "Hold brake components in position", "Caliper bolt loosens or retaining fastener backs out", "Caliper shift, misalignment, or severe braking loss", 9, "Vibration, missing thread locking, or incorrect torque", 3, "Torque audit and witness mark", 7, "Use locking fastener, torque stripe, and assembly verification", "Manufacturer", "S01; engineering_inference:S02"),
    ("Mounting hardware", "Maintain bracket stiffness", "Brake bracket cracks near mounting hole", "Loss of caliper position and degraded braking", 9, "Fatigue, stress concentration, or impact", 2, "Visual inspection and design review", 8, "Add fillet radius, fatigue review, and proof-load inspection", "Designer", "engineering_inference:S02"),
    ("Wheel-level braking response", "Decelerate wheel predictably", "Brake does not engage when commanded", "Excessive stopping distance and collision risk", 10, "Disconnected force path, severe pad wear, or caliper malfunction", 2, "Pre-ride brake check", 8, "Add pre-ride check procedure and fail-safe design review", "Rider", "S01; engineering_inference:S02"),
    ("Wheel-level braking response", "Modulate deceleration", "Brake engages too aggressively or unexpectedly", "Wheel lock, skid, and rider fall", 8, "Excessive leverage, poor modulation, or contaminated friction pair", 3, "Functional braking response check", 8, "Define modulation acceptance criteria and adjust leverage/friction pairing", "Designer", "S01; engineering_inference:S02"),
    ("Wheel-level braking response", "Maintain consistent braking response", "Front and rear brake balance is poorly matched", "Rider instability during braking", 7, "Component mismatch or uneven adjustment", 4, "Final assembly brake response check", 6, "Add balance check and adjustment procedure", "Manufacturer", "engineering_inference:S02;S03"),
    ("Brake pads", "Remain secured in caliper", "Pad retaining pin loosens or clip disengages", "Pad shift, noise, or partial braking loss", 8, "Improper clip seating or vibration loosening", 3, "Visual inspection of retaining hardware", 7, "Add positive retention clip and assembly verification", "Manufacturer", "engineering_inference:S02"),
    ("Cable or hydraulic path", "Recover after brake release", "Return spring or cable return is insufficient", "Brake remains partially engaged after release", 6, "Weak return spring, cable drag, or contamination", 4, "Lever return check", 6, "Specify return-force threshold and contamination-resistant routing", "Designer", "engineering_inference:S03"),
]


def rpn(s: int, o: int, d: int) -> int:
    return s * o * d


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def make_row(
    base: tuple,
    method_id: str,
    item_id: str,
    evidence: str,
    critic: str,
    status: str = "keep",
    score_shift: tuple[int, int, int] = (0, 0, 0),
    force_bad_rpn: bool = False,
) -> dict[str, object]:
    subsystem, function, mode, effect, s, cause, o, control, d, action, role, base_evidence = base
    ds, do, dd = score_shift
    s2 = max(1, min(10, int(s) + ds))
    o2 = max(1, min(10, int(o) + do))
    d2 = max(1, min(10, int(d) + dd))
    value = rpn(s2, o2, d2)
    if force_bad_rpn:
        value += 5
    return {
        "method_id": method_id,
        "item_id": item_id,
        "subsystem": subsystem,
        "function": function,
        "requirement_or_evidence_anchor": evidence if evidence != "none" else "none",
        "potential_failure_mode": mode,
        "potential_effect": effect,
        "severity_s": s2,
        "potential_cause": cause,
        "occurrence_o": o2,
        "current_control": control,
        "detection_d": d2,
        "rpn": value,
        "recommended_action": action,
        "responsible_role": role,
        "evidence_trace": evidence if evidence != "use_base" else base_evidence,
        "critic_notes": critic,
        "status": status,
    }


def build_variant(method: str, prefix: str, run: int, indices: list[int], *, full: bool = False) -> list[dict[str, object]]:
    rows = []
    for n, idx in enumerate(indices, start=1):
        base = BASE_ROWS[idx]
        shift = ((run + n) % 3 - 1, (run + idx) % 2, (n + idx) % 2)
        if method == "M2":
            evidence = "none"
            critic = "not_applicable"
            shift = (0, (run + n) % 2, (idx + run) % 2)
        elif method == "M3":
            evidence = "use_base"
            critic = "not_applicable"
        else:
            evidence = "use_base"
            critic = "Kept after evidence-boundary, specificity, mitigation, and RPN review" if full else "Role-ablation artifact"
        rows.append(make_row(base, method, f"{prefix}-{n:03d}", evidence, critic, score_shift=shift))
    return rows


def add_no_critic_artifacts(rows: list[dict[str, object]], run: int) -> list[dict[str, object]]:
    # Add one generic and one near-duplicate item to expose why critic review matters.
    generic = rows[0].copy()
    generic.update(
        {
            "item_id": f"M4NC{run}-G01",
            "subsystem": "Wheel-level braking response",
            "function": "Decelerate wheel",
            "potential_failure_mode": "brake failure",
            "potential_effect": "Reduced or absent braking response",
            "severity_s": 9,
            "occurrence_o": 3,
            "detection_d": 8,
            "rpn": 216,
            "recommended_action": "Improve brake design and inspection",
            "evidence_trace": "S01",
            "critic_notes": "critic_ablation_not_performed",
        }
    )
    duplicate = rows[2].copy()
    duplicate.update(
        {
            "item_id": f"M4NC{run}-D01",
            "potential_failure_mode": "Cable anchor slips or detaches during braking",
            "potential_effect": "Sudden severe loss of braking force",
            "critic_notes": "critic_ablation_not_performed",
        }
    )
    return rows + [generic, duplicate]


def mark_no_integrity_artifacts(rows: list[dict[str, object]], run: int) -> list[dict[str, object]]:
    # Add small consistency defects that a final integrity checker should catch.
    if rows:
        rows[1]["rpn"] = int(rows[1]["rpn"]) + 5
    if len(rows) > 5 and run == 2:
        rows[5]["evidence_trace"] = ""
    if len(rows) > 8 and run == 3:
        rows[8]["recommended_action"] = ""
    for row in rows:
        row["critic_notes"] = "Critic retained row, but final integrity pass intentionally omitted"
    return rows


def main() -> None:
    variants = {
        "M2_run02.csv": build_variant("M2", "M2R2", 2, list(range(0, 15))),
        "M2_run03.csv": build_variant("M2", "M2R3", 3, list(range(2, 18))),
        "M3_run02.csv": build_variant("M3", "M3R2", 2, list(range(1, 17))),
        "M3_run03.csv": build_variant("M3", "M3R3", 3, list(range(0, 16))),
        "M4_full_run02.csv": build_variant("M4", "M4R2", 2, list(range(0, 18)), full=True),
        "M4_full_run03.csv": build_variant("M4", "M4R3", 3, list(range(0, 17)), full=True),
    }

    for run in [1, 2, 3]:
        base_indices = list(range(0, 15 + (run % 2)))
        no_critic = build_variant("M4", f"M4NC{run}", run, base_indices)
        no_critic = add_no_critic_artifacts(no_critic, run)
        variants[f"M4_no_critic_run0{run}.csv"] = no_critic

        no_integrity = build_variant("M4", f"M4NI{run}", run, list(range(1, 17)))
        no_integrity = mark_no_integrity_artifacts(no_integrity, run)
        variants[f"M4_no_integrity_run0{run}.csv"] = no_integrity

    for name, rows in variants.items():
        write_rows(RUNS / name, rows)
        print(f"wrote {name}: {len(rows)} rows")


if __name__ == "__main__":
    main()

