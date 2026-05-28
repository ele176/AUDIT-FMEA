# AUDIT-FMEA Public Artifact v0.5 Release Notes

Date: 2026-05-28

## Added

- Added `manuscript_support/data_evidence_chain_v1.0/`, a data provenance and evidence-boundary audit for the retained AUDIT-FMEA rows.
- Added row-level evidence-chain CSV mapping each primary-case and transfer-case retained row to:
  - source identifiers;
  - engineering-inference labels;
  - generation route;
  - field provenance;
  - RPN arithmetic status;
  - supported and unsupported claim boundaries.
- Added field-level provenance and manuscript claim-boundary matrices.
- Added an audit report and check file.

## Audit summary

- Rows audited: 36.
- Rows passing RPN arithmetic recomputation: 36/36.
- Rows missing evidence traces: 0.
- Direct or close source-translation rows: 16.
- Mixed direct-source and engineering-inference rows: 13.
- Engineering-inference-only rows: 7.

## Claim boundary

This release strengthens transparency around data provenance. It supports inspection of structural auditability, evidence-boundary labelling, and recomputation of formal checks. It does not provide expert validation, physical braking tests, calibrated S/O/D ratings, real-world failure-frequency evidence, regulatory compliance evidence, or safety certification.
