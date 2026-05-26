# Reproducibility Package

Paper:

An Evidence-Grounded Multi-Agent LLM Workflow for Auditable Design FMEA in Mechanical Braking Systems

Version:

- v0.1, prepared on 2026-05-23

## Purpose

This package provides the prompt templates, evidence pack, normalized DFMEA outputs, metric script, metric outputs, and draft figure files used in the structural evaluation. It is designed to support auditability and procedural reproducibility.

## Package Structure

| Folder | Content |
|---|---|
| `prompts/` | Prompt templates for M1-M4 workflows |
| `data/` | DFMEA schema, compact evidence pack, and normalized combined CSV |
| `method_outputs/` | Raw markdown and CSV outputs for M1-M4 |
| `scripts/` | Metric recomputation script |
| `outputs/` | Metric JSON and summary markdown |
| `figures/` | Draft figure files and figure-generation script |

## Main Files

### Prompts

- `prompts/m1_template_only_fmea.md`
- `prompts/m2_single_llm_fmea.md`
- `prompts/m3_rag_llm_fmea.md`
- `prompts/m4_multi_agent_fmea.md`

### Data

- `data/dfmea_schema.md`
- `data/evidence_pack.md`
- `data/dfmea_entries_all_methods.csv`

### Scripts

- `scripts/metrics.py`

### Outputs

- `outputs/metrics_all_methods.json`
- `outputs/metrics_summary.md`

### Method Outputs

- `method_outputs/m1_output.md`
- `method_outputs/m1_dfmea.csv`
- `method_outputs/m2_output.md`
- `method_outputs/m2_dfmea.csv`
- `method_outputs/m3_output.md`
- `method_outputs/m3_dfmea.csv`
- `method_outputs/m4_output.md`
- `method_outputs/m4_dfmea.csv`

## Recalculate Metrics

From the project root, run:

```powershell
python .\06_supplementary\reproducibility_package\scripts\metrics.py --dfmea .\06_supplementary\reproducibility_package\data\dfmea_entries_all_methods.csv --out .\06_supplementary\reproducibility_package\outputs\metrics_all_methods_recomputed.json
```

If your Python command differs, use the local Python executable available in your environment.

## What Is Not Included

This package intentionally excludes:

- external validation scoring sheets or identity keys
- internal peer-review reports
- internal planning ledger
- reviewer-confidential materials

## Reproducibility Boundary

The package supports procedural reproduction of the structural evaluation after the LLM outputs have been generated. It does not provide a complete API-level generation log with fixed model build, random seed, temperature, or repeated-run variance. This limitation is disclosed in the manuscript.

## Suggested Citation in Manuscript

The prompts, compact evidence pack, normalized DFMEA outputs, metric script, and metric outputs used in this study are provided as supplementary reproducibility materials.
