# Data Provenance and Evidence-Boundary Audit v1.0

Purpose: make the evidential status of the AUDIT-FMEA dataset explicit at field, row, and manuscript-claim level.

This audit is intentionally conservative. It treats generated DFMEA rows as research artifacts for structural auditability analysis, not as verified mechanical truth.

## Summary

- Final-row audit rows: 36
- Rows with at least one direct source ID: 29
- Rows with engineering-inference labels: 20
- Direct-only rows: 16
- Mixed direct + inference rows: 13
- Inference-only rows: 7
- Rows passing RPN arithmetic recomputation: 36/36

## Files produced

- `row_level_evidence_chain_v1.0.csv`: row-by-row evidence and provenance map for primary M4 run 01 and the second transfer case.
- `field_provenance_matrix_v1.0.csv`: schema-field provenance, processing, audit check, and claim boundary.
- `claim_evidence_boundary_matrix_v1.0.csv`: manuscript claim-to-evidence mapping, including unsupported claims.
- `source_id_legend_v1.0.csv`: source identifier legend used by evidence traces.
- `manuscript_insert_data_evidence_chain_v1.0.md`: ready-to-adapt manuscript text.

## Claim Boundary

The dataset supports claims about row-level traceability, required-field completeness, duplicate control, RPN arithmetic consistency, and role-ablation artifact defects.

The dataset does not support claims about technical correctness, braking safety, real-world failure frequency, calibrated S/O/D ratings, mitigation effectiveness, or regulatory compliance.

## Field Provenance Matrix

| field_or_artifact | primary_origin | audit_check | supports | does_not_support |
|---|---|---|---|---|
| case boundary | author-defined from public reports, standards-related material, and subsystem scope decisions | manual inspection against stated boundary | scope transparency and boundary auditability | complete product hazard coverage or regulatory compliance |
| evidence pack and source IDs | compact summaries of public reports, recalls, standards-related material, manuals, and prior literature | source IDs can be traced to evidence_pack files and manuscript references | row-level traceability | proof that a row is technically correct |
| subsystem/function/failure/effect/cause/current_control/recommended_action/responsible_role | LLM-generated candidate DFMEA artifact under bounded prompts | required-field and boundary checks; critic notes for M4 rows | reviewable candidate DFMEA content | ground-truth failure mechanisms, field frequency, or mitigation effectiveness |
| S/O/D ratings | LLM-estimated early DFMEA ratings under shared anchors | range validity only; no expert calibration yet | RPN recomputation and high-risk/high-severity structural summaries | validated risk priority or calibrated severity/occurrence/detection |
| RPN | product of S, O, and D fields | RPN arithmetic mismatch check | internal arithmetic consistency | real-world risk magnitude |
| critic_notes | M4 critic/review role output or ablation marker | presence and defect category inspection | visibility of review rationale | independent human review |
| status | workflow retention decision | status field present and normalized | artifact filtering transparency | expert acceptance |
| structural metrics | deterministic scripts over normalized CSV files | recompute scripts and source data provided | traceability, completeness, duplication, and arithmetic-consistency claims | engineering correctness or braking safety |
| figures and result tables | generated from metric summaries and source-data files | figure source data available | visual reporting of structural metrics | additional empirical evidence beyond the source metrics |

## Manuscript Claim Boundary Matrix

| manuscript_claim | supporting_data | evidence_strength | remaining_limit |
|---|---|---|---|
| AUDIT-FMEA preserves row-level evidence traceability | M3/M4 evidence_trace fields; evidence trace rate metric | recomputable structural evidence | a trace marker is not a correctness certificate |
| AUDIT-FMEA reduces opaque table generation by exposing intermediate artifacts | role-to-defect contract, critic_notes, evidence labels, integrity checks, prompts | artifact/process evidence | does not prove improved human decision outcomes |
| The integrity role prevents formal defects | M4_no_integrity ablation metrics: invalid rate, evidence trace drop, RPN mismatch | recomputable ablation evidence | only tested in generated artifacts, not physical engineering workflow |
| The critic role targets semantic artifact defects | M4_no_critic ablation metrics: duplicate pair and invalid-row pattern | bounded artifact evidence | semantic correctness still requires human/domain review |
| The workflow transfers to a second related mechanical braking case | bicycle/e-bike mechanical disc brake run and case2 structural metrics | single transfer-case structural evidence | both cases remain related braking systems; no broad mechanical generality claim |
| The generated DFMEA rows are technically correct | not supported in current dataset | unsupported claim | requires expert validation, proprietary design data, or physical/field evidence |
| S/O/D ratings are calibrated or accurate | not supported in current dataset | unsupported claim | requires expert scoring protocol or empirical reliability data |
| The workflow certifies braking safety or regulatory compliance | not supported in current dataset | unsupported claim | requires formal safety assessment, testing, and compliance review |
