# Package Integrity Note

Date: 2026-05-22

## Verification

The metric recomputation command was tested on this package:

```powershell
python .\06_supplementary\reproducibility_package\scripts\metrics.py --dfmea .\06_supplementary\reproducibility_package\data\dfmea_entries_all_methods.csv --out .\06_supplementary\reproducibility_package\outputs\metrics_all_methods_recomputed.json
```

Output created:

- `outputs/metrics_all_methods_recomputed.json`

The recomputed metrics match the manuscript-reported values:

| Method | Rows | Evidence trace rate | High-RPN items | High-severity items | RPN mismatches |
|---|---:|---:|---:|---:|---:|
| M1 | 7 | 0.000 | 2 | 3 | 0 |
| M2 | 15 | 0.000 | 4 | 8 | 0 |
| M3 | 16 | 1.000 | 5 | 9 | 0 |
| M4 | 18 | 1.000 | 5 | 11 | 0 |

## Excluded Materials

The package does not include:

- external validation scoring sheets or identity keys,
- external-score aggregation utilities,
- reviewer-confidential materials,
- internal peer-review reports,
- internal agent ledger.

## Publication Caution

Before public release:

1. Review all files for institutional or personal identifiers.
2. Remove Figure 3 if publisher artwork policies require manually recreated figures only.
3. Keep any future external-score aggregation utilities outside the public supplementary package unless external validation is actually collected and reported.
