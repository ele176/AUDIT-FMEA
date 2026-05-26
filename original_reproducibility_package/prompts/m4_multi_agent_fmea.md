# M4 Prompt Protocol: Proposed Evidence-Grounded Multi-Agent FMEA

Purpose:

Generate the proposed method output using separated agent roles, evidence traceability, critic review, and mitigation refinement.

## Agent Roles

1. Function Decomposition Agent
2. Evidence Retrieval Agent
3. Failure Mode Generation Agent
4. Cause-Effect Reasoning Agent
5. Risk Scoring Agent
6. Critic Agent
7. Mitigation Agent
8. Integrity Check Agent

These experiment-specific roles operationalize the ARS agent workflow for the DFMEA task.

## Inputs Allowed

- System boundary from `dfmea_schema.md`
- Required DFMEA columns
- S/O/D scoring anchors
- Evidence corpus excerpts and source IDs
- Critic review and revision cycle

## Procedure

### Step 1: Function Decomposition

Decompose the braking subsystem into functions, interfaces, and expected performance requirements.

Output:

- Function-component map
- Requirement/evidence anchors

### Step 2: Evidence Retrieval

Map evidence items from the evidence pack to each subsystem and function.

Output:

- Evidence coverage table
- Coverage gaps

### Step 3: Failure Mode Generation

Generate candidate failure modes for each component-function pair.

Rules:

- Cover all included subsystems.
- Prefer specific failure mechanisms over generic "brake failure."
- Mark evidence-supported and engineering-inference entries separately.

### Step 4: Cause-Effect Reasoning

For each candidate:

- Identify plausible causes.
- Identify local, system-level, and rider-safety effects.
- Remove entries outside the system boundary.

### Step 5: Risk Scoring

Assign S/O/D ratings using the anchors in `dfmea_schema.md`.

Rules:

- Explain any S >= 8.
- Explain any D >= 8.
- Recalculate RPN.
- Flag high-risk entries.

### Step 6: Critic Review

Review the table for:

- Duplicates
- Mechanically implausible items
- Unsupported rows
- Vague failure modes
- Boundary violations
- Inconsistent S/O/D ratings
- Missing high-risk candidates

Output:

- `critic_notes`
- status: keep, merge, revise, remove

### Step 7: Mitigation Refinement

For rows marked keep or revise:

- Improve recommended actions.
- Separate design, manufacturing, inspection, and maintenance actions where useful.
- Avoid overclaiming mitigation effectiveness.

### Step 8: Integrity Check

Confirm:

- Every M4 row has evidence trace or engineering inference tag.
- Every RPN equals S x O x D.
- Every high-severity row has a mitigation action.
- No row claims physical validation.

## Output Requirements

Generate:

1. Function-component map.
2. Evidence coverage table.
3. Final normalized DFMEA table.
4. Critic review summary.
5. Integrity checklist.

Set:

- `method_id = M4`

## Prompt Text

You are executing an evidence-grounded multi-agent DFMEA workflow for an electric scooter mechanical braking subsystem. Follow the eight-step protocol exactly: function decomposition, evidence retrieval, failure mode generation, cause-effect reasoning, risk scoring, critic review, mitigation refinement, and integrity check. Use the provided evidence pack, source IDs, system boundary, DFMEA schema, and S/O/D anchors. The final DFMEA rows must be specific, traceable, mechanically plausible, and suitable for early-stage design review. Do not claim physical braking-performance validation.

