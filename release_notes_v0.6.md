# AUDIT-FMEA Public Artifact v0.6 Release Notes

Date: 2026-05-28

## Added

- Added `manuscript_support/known_defect_stress_test_v1.0/`, a structural negative-control test with 12 deliberately corrupted DFMEA rows.
- Added detection outputs showing that all 12 expected injected defect labels were detected:
  - integrity-oriented defects: 7/7;
  - critic-oriented defects: 5/5;
  - duplicate pairs detected as intended: 1.
- Added `manuscript_support/representative_evidence_rationale_v1.0/`, a representative row-level appendix for ten selected DFMEA rows.
- Updated metadata to align with the v1.4 manuscript framing: AUDIT-FMEA as an auditable multi-agent LLM protocol for mechanical braking DFMEA artifacts.

## Claim boundary

This release strengthens the artifact-level audit protocol. It supports inspection of structural auditability, evidence-boundary labelling, representative row-level source/inference rationales, and injected-defect detection. It does not provide expert validation, physical braking tests, calibrated S/O/D ratings, real-world failure-frequency evidence, regulatory compliance evidence, or safety certification.
