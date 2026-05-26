# DFMEA Metrics Summary v0.1

Generated from:

- `paper_project/02_experiment/data/dfmea_entries_all_methods.csv`
- `paper_project/02_experiment/scripts/metrics.py`
- `paper_project/02_experiment/outputs/metrics_all_methods.json`

## Summary Table

| Method | Rows | Invalid rate | Duplicate pairs | Evidence trace rate | High RPN items | High severity items | RPN mismatches |
|---|---:|---:|---:|---:|---:|---:|---:|
| M1 Template-only FMEA | 7 | 0.000 | 0 | 0.000 | 2 | 3 | 0 |
| M2 Single-LLM FMEA | 15 | 0.000 | 0 | 0.000 | 4 | 8 | 0 |
| M3 RAG-LLM FMEA | 16 | 0.000 | 0 | 1.000 | 5 | 9 | 0 |
| M4 Multi-agent FMEA | 18 | 0.000 | 0 | 1.000 | 5 | 11 | 0 |

## Preliminary Interpretation

M1 provides the smallest baseline and covers each subsystem once. It is useful as a template control but has no evidence traceability and limited granularity.

M2 increases row count and identifies more high-severity and high-RPN items, but it has no traceability and no critic notes.

M3 adds evidence traces to all rows and introduces source-grounded failure modes related to reported brake-problem scenarios. It still lacks explicit role separation and critic review.

M4 provides the most complete structured output: 18 rows, full evidence traceability, critic notes, and an integrity checklist. The current script found no RPN mismatches, duplicate pairs, or invalid rows.

## Caution

These metrics are table-structure metrics, not proof of engineering correctness. Mechanical-domain expert scoring is required before making claims about usefulness or technical quality.

