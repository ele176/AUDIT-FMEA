# Manuscript Insert: Stability and Role-Ablation Extension v0.1

## Methods insert

To assess whether the observed structural differences were stable across model generations, we added a repeated-run evaluation. The single-LLM baseline (M2), the RAG-LLM baseline (M3), and the full AUDIT-FMEA workflow (M4_full) were each repeated under the same system boundary, DFMEA schema, S/O/D anchors, and evidence-pack version. For each run, outputs were normalized to the common CSV schema and evaluated using the same structural metrics as the main experiment: row count, invalid rate, duplicate pair count, evidence trace rate, high-RPN item count, high-severity item count, and RPN arithmetic mismatch count. Model name, provider, generation date, and available sampling settings were recorded in a run manifest.

We also performed role ablations to test whether the proposed multi-agent structure contributed measurable reviewability effects. Starting from the full AUDIT-FMEA workflow, we removed the critic role (`M4_no_critic`) and the final integrity-check role (`M4_no_integrity`). These ablations were designed to isolate whether critic review and integrity checking affect structural auditability. The ablation analysis does not test physical correctness or safety validity; it tests whether the workflow produces more inspectable DFMEA artifacts.

## Results insert

Table X reports the repeated-run and ablation summary. Across repeated runs, the full AUDIT-FMEA workflow preserved full evidence traceability, zero duplicate pairs, zero invalid rows, and zero RPN arithmetic mismatches. The single-LLM baseline remained structurally valid but had no evidence traceability. The RAG baseline preserved evidence traceability but lacked critic and integrity artifacts. In the role-ablation conditions, removing the critic role produced vague failure modes and near-duplicate rows, while removing the integrity role produced RPN mismatches and missing required fields. These findings support the claim that critic and integrity roles improve structural auditability under the current protocol.

| Variant | n | Rows mean+/-sd | Invalid rate mean+/-sd | Duplicate pairs mean+/-sd | Evidence trace mean+/-sd | High-RPN mean+/-sd | High-severity mean+/-sd | RPN mismatches mean+/-sd |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| M2 | 3 | 15.333+/-0.577 | 0.0+/-0.0 | 0.0+/-0.0 | 0.0+/-0.0 | 9.667+/-4.933 | 9.333+/-1.155 | 0.0+/-0.0 |
| M3 | 3 | 16.0+/-0.0 | 0.0+/-0.0 | 0.0+/-0.0 | 1.0+/-0.0 | 9.667+/-4.509 | 9.0+/-0.0 | 0.0+/-0.0 |
| M4_full | 3 | 17.667+/-0.577 | 0.0+/-0.0 | 0.0+/-0.0 | 1.0+/-0.0 | 11.0+/-5.292 | 10.667+/-0.577 | 0.0+/-0.0 |
| M4_no_critic | 3 | 17.667+/-0.577 | 0.057+/-0.002 | 1.0+/-0.0 | 1.0+/-0.0 | 14.0+/-2.0 | 11.333+/-0.577 | 0.0+/-0.0 |
| M4_no_integrity | 3 | 16.0+/-0.0 | 0.104+/-0.036 | 0.0+/-0.0 | 0.979+/-0.036 | 10.333+/-0.577 | 10.0+/-1.0 | 1.0+/-0.0 |

These findings should be interpreted as structural evidence. They show how role separation affects traceability, duplication, and internal consistency under the current protocol. They do not establish that the generated DFMEA rows are technically correct, sufficient for product release, or equivalent to expert-validated safety analysis.

## Table caption

Table X. Repeated-run and role-ablation summary for LLM-assisted DFMEA workflows. Values are mean +/- standard deviation across normalized runs. Metrics evaluate structural auditability and internal consistency, not physical braking validation or expert-certified correctness.

