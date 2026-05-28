# Manuscript Insert: Data Provenance and Evidence-Boundary Audit v1.0

## Suggested Methods subsection

### Data provenance and evidence-boundary audit

Because the dataset consists of AI-generated DFMEA artifacts rather than physical test data or expert-labelled ground truth, we added a data provenance and evidence-boundary audit. The audit maps each retained row in the primary AUDIT-FMEA run and in the bicycle/e-bike mechanical disc brake transfer case to its source identifiers, engineering-inference tags, generation route, field provenance, RPN arithmetic status, and claim boundary. Schema fields were classified into five provenance categories: public-source inputs, LLM-generated candidate DFMEA content, LLM-estimated S/O/D ratings, deterministic script-computed checks, and author-normalized artifact decisions. The audit is released with the reproducibility package as `08_data_evidence_chain/row_level_evidence_chain_v1.0.csv`, `field_provenance_matrix_v1.0.csv`, and `claim_evidence_boundary_matrix_v1.0.csv`.

This audit does not validate the generated rows as mechanically correct. Its purpose is to make explicit which parts of the dataset support structural auditability claims and which parts remain outside the current evidence boundary. Direct source labels indicate row-level traceability to the compact evidence pack. Engineering-inference labels indicate plausible extensions from subsystem function, interface reasoning, or related evidence. S/O/D ratings are treated as early candidate ratings rather than calibrated risk estimates.

## Suggested Results paragraph

The evidence-boundary audit covers 36 retained AUDIT-FMEA rows across the primary and transfer cases. Every audited row contains an evidence trace and passes RPN arithmetic recomputation. However, the audit also shows that many rows contain engineering-inference labels, meaning that the public evidence supports the inclusion or context of the row rather than proving the exact failure mechanism or S/O/D values. This strengthens the paper's process-level claim while narrowing the interpretation of the data: the results support traceability, internal consistency, and reviewability of generated DFMEA artifacts, not expert-validated mechanical correctness.

## Suggested limitation sentence

The provenance audit makes the evidence boundary explicit but does not remove it: generated DFMEA text fields and S/O/D ratings remain candidate artifacts until checked against expert judgement, proprietary design information, field data, or physical tests.
