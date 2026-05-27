# Bicycle/e-bike Mechanical Disc Brake Transfer Case v1.0

This folder contains a second mechanical braking case for the AUDIT-FMEA manuscript revision.

## Files

| File | Role |
|---|---|
| `evidence_pack_bicycle_disc_brake_v1.0.md` | Public-source evidence pack and case boundary |
| `runs/M4_case2_bicycle_disc_brake_run01.csv` | Author-verified AUDIT-FMEA DFMEA artifact for the second case |
| `case2_structural_metrics_v1.0.json` | Machine-readable structural metric output after recomputation |
| `case2_structural_metrics_v1.0.md` | Markdown summary table after recomputation |
| `manuscript_insert_second_case_v1.0.md` | Ready-to-integrate English manuscript text |

## Claim boundary

This transfer case supports only a structural auditability claim:

- row-level evidence traces are present
- required fields are complete
- duplicate rows are not detected by the stated text-similarity threshold
- RPN arithmetic is internally consistent

It does not support claims of:

- physical braking performance
- regulatory compliance
- product safety certification
- expert-validated S/O/D correctness
- completeness of all possible bicycle/e-bike brake failure modes

## Next integration step

If this extension is adopted in the manuscript, the public GitHub/Zenodo artifact should be updated with this folder and released as a new version before submission.

