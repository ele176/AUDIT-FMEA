# DFMEA Schema and Scoring Protocol v0.1

Agents used:

- `academic-paper/agents/structure_architect_agent.md`
- `academic-paper/agents/argument_builder_agent.md`
- `academic-pipeline/agents/integrity_verification_agent.md`

Purpose:

This file defines the common DFMEA output schema for all four experimental methods. All generated outputs must be normalized to this schema before comparison.

## Compared Methods

M1. Template-only FMEA

M2. Single-LLM FMEA

M3. RAG-LLM FMEA

M4. Proposed evidence-grounded multi-agent FMEA

## System Boundary

System: E-scooter mechanical braking subsystem

Included components:

- Brake lever
- Cable or hydraulic transmission path
- Brake caliper
- Brake pads
- Disc rotor
- Mounting hardware
- Wheel-level braking response

Excluded components:

- Battery
- Motor controller
- Regenerative braking logic unless directly interacting with mechanical braking
- Full vehicle dynamics
- ABS control
- Road testing and physical measurement

## Required DFMEA Columns

| Column | Required | Description |
|---|---:|---|
| method_id | Yes | M1, M2, M3, or M4 |
| item_id | Yes | Unique entry ID within each method, e.g., M4-001 |
| subsystem | Yes | Brake lever, cable/hydraulic line, caliper, pads, rotor, mount, wheel-level response |
| function | Yes | Intended function of the item |
| requirement_or_evidence_anchor | Yes for M3/M4 | Standard, report, manual, or source anchor supporting this function/failure mode |
| potential_failure_mode | Yes | How the item could fail |
| potential_effect | Yes | Effect on system, rider, or safety |
| severity_s | Yes | Severity rating from 1 to 10 |
| potential_cause | Yes | Plausible root cause or mechanism |
| occurrence_o | Yes | Occurrence rating from 1 to 10 |
| current_control | Yes | Existing prevention or detection control |
| detection_d | Yes | Detection rating from 1 to 10 |
| rpn | Yes | S x O x D |
| recommended_action | Yes | Design, manufacturing, inspection, or maintenance action |
| responsible_role | Optional | Designer, manufacturer, service technician, rider, inspector |
| evidence_trace | Yes for M3/M4 | Source IDs supporting the entry, e.g., S01; S02 |
| critic_notes | Yes for M4 | Notes from critic review or consistency check |
| status | Yes | keep, merge, revise, remove |

## S/O/D Rating Anchors

The scale is adapted for early-stage design FMEA. It is not a certified safety standard.

### Severity (S)

| Score | Anchor |
|---:|---|
| 1 | No noticeable effect on braking or user safety |
| 2 | Very minor inconvenience; no safety impact |
| 3 | Minor braking discomfort or maintenance issue |
| 4 | Noticeable degraded braking but controllable |
| 5 | Reduced braking performance under some conditions |
| 6 | Significant braking degradation; increased stopping distance |
| 7 | Loss of partial braking capability or high rider control burden |
| 8 | Severe braking loss likely to cause crash or injury |
| 9 | Near-total braking failure with high injury potential |
| 10 | Catastrophic braking failure with severe injury or fatality potential |

### Occurrence (O)

| Score | Anchor |
|---:|---|
| 1 | Remote; highly unlikely under normal use |
| 2 | Very low; rare with proper design and maintenance |
| 3 | Low; possible over extended use or poor maintenance |
| 4 | Occasional; plausible in field use |
| 5 | Moderate; known mechanism with several plausible triggers |
| 6 | Moderately high; likely under harsh use, wear, or poor assembly |
| 7 | High; common failure pathway without robust controls |
| 8 | Very high; expected repeatedly in normal product life |
| 9 | Almost inevitable in many units without redesign |
| 10 | Nearly certain or continuously present |

### Detection (D)

Important: Higher D means harder to detect before the effect occurs.

| Score | Anchor |
|---:|---|
| 1 | Almost certain detection before use |
| 2 | Very high detection likelihood by routine inspection |
| 3 | High detection likelihood with simple check |
| 4 | Moderate-high detection before severe effect |
| 5 | Moderate detection; may require maintenance inspection |
| 6 | Moderate-low detection; early signs may be ambiguous |
| 7 | Low detection before degraded braking is experienced |
| 8 | Very low detection; failure may appear suddenly |
| 9 | Remote detection; hidden until braking demand |
| 10 | No practical detection before hazardous event |

## Derived Fields

RPN = severity_s x occurrence_o x detection_d

High-risk item threshold:

- Primary threshold: RPN >= 180
- Secondary threshold: severity_s >= 8 even if RPN < 180

The secondary threshold prevents high-severity, lower-occurrence items from being hidden by RPN arithmetic.

## Evidence Traceability Rules

For M3 and M4:

- Every row must contain at least one source ID in `evidence_trace`.
- `evidence_trace` can support function, failure mode, effect, or mitigation.
- If a row is inferred from engineering logic rather than directly stated in a source, mark as `engineering_inference:Sxx`.
- Unsupported rows are allowed only if marked `unsupported_candidate` and flagged for critic review.

For M1 and M2:

- Evidence trace is not required, but if provided it will be counted.

## Duplicate and Invalid Item Rules

Duplicate item:

- Two rows describe substantially the same subsystem, failure mode, cause, and effect.
- Minor wording differences do not make an item unique.

Invalid item:

- Outside the system boundary.
- Mechanically implausible.
- Too vague to act on, e.g., "brake failure" with no component or mechanism.
- Unsupported by either evidence or plausible engineering inference.
- Duplicates another row but adds no new mechanism, effect, or control.

## Normalization Rules

1. Convert every method output to CSV using `dfmea_entries_template.csv`.
2. Keep original generated output in the method's output folder.
3. Do not silently delete rows. Mark rows as `remove` with reason in `critic_notes`.
4. RPN must be recalculated by script even if generated by an LLM.
5. If S/O/D are missing or non-numeric, mark the row invalid for risk-score consistency.

