# Role-Ablation Protocol for AUDIT-FMEA

Purpose: test whether individual AUDIT-FMEA roles contribute measurable structural differences.

## Full variant

`M4_full`: evidence role + failure generation + cause-effect reasoning + risk scoring + critic review + mitigation refinement + integrity checking.

## Ablation variants

### M4_no_critic

Remove the critic review stage.

Prompt:

> Execute the AUDIT-FMEA workflow, but omit the critic review stage. Do not check for duplicates, unsupported rows, vague failure modes, boundary violations, or inconsistent S/O/D ratings through a separate critic pass. Keep evidence attribution, mitigation refinement, and integrity checking. Output only normalized CSV rows.

Expected risk:

- more generic rows;
- more duplicates;
- weaker critic notes;
- less disciplined mitigation wording.

### M4_no_integrity

Remove the final integrity-check stage.

Prompt:

> Execute the AUDIT-FMEA workflow, but omit the final integrity-check stage. Do not perform a final check for required fields, evidence traces, high-severity mitigation coverage, or RPN arithmetic. Keep function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, and mitigation refinement. Output only normalized CSV rows.

Expected risk:

- more missing fields;
- more RPN arithmetic mismatches;
- inconsistent evidence labels.

### M4_no_evidence_labels

Remove explicit evidence/inference labels while still giving the model the evidence pack.

Prompt:

> Execute the AUDIT-FMEA workflow using the evidence pack, but do not require source IDs or `engineering_inference:Sxx` labels in each row. Keep function decomposition, failure generation, cause-effect reasoning, risk scoring, critic review, mitigation refinement, and integrity checking. Output only normalized CSV rows.

Expected risk:

- lower evidence traceability;
- weaker auditability;
- more difficult row-level inspection.

## Reporting

Use the same structural metrics as the main experiment:

- row count;
- invalid rate;
- duplicate pair count;
- evidence trace rate;
- high-RPN item count;
- high-severity item count;
- RPN mismatch count.

Do not claim that ablation proves technical correctness. It only tests structural and process-level auditability.

