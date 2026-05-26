# AUDIT-FMEA Public Artifact v0.3

This repository package supports the manuscript:

**AUDIT-FMEA: Auditable Multi-Agent Workflows for Design Failure Analysis**

## Purpose

The artifact contains prompts, compact evidence material, normalized DFMEA outputs, metric scripts, initial results, repeated-run and role-ablation outputs, generated figures, source data, and manuscript-supporting documentation.

The artifact is intended to support procedural auditability. It does not provide physical braking validation, safety certification, or expert-certified technical correctness.

## Contents

| Folder | Description |
|---|---|
| `original_reproducibility_package/` | Original AEI submission reproducibility files: evidence pack, prompts, method outputs, metric scripts, and initial metric outputs |
| `experiment_extension/` | Top-conference extension package: ChatGPT manual runbook, repeated-run prompts, ablation prompts, run manifest, stability script, generated run CSVs, and stability summaries |
| `figures_v0.3/` | Publication figure outputs in SVG, PDF, and PNG, plus source data |
| `scripts/generate_figures_v0_3.py` | Python script used to regenerate Figures 1-3 |
| `manuscript_support/` | Data availability, figure contracts, and literature-search support files |

## Current evidence status

The current package includes the original single-run outputs for M2, M3, and M4 as `run01` seeds, plus additional repeated-run and role-ablation outputs generated during the top-conference rework. These outputs are AI-generated research artifacts under the documented workflow. They support structural auditability analysis only.

## How to recompute original metrics

From the project root:

```powershell
python original_reproducibility_package\scripts\metrics.py `
  --dfmea original_reproducibility_package\data\dfmea_entries_all_methods.csv `
  --out original_reproducibility_package\outputs\metrics_all_methods_recomputed.json
```

## How to compute repeated-run and ablation summaries

After adding normalized run CSVs into:

```text
experiment_extension/data/runs/
```

run:

```powershell
python experiment_extension\scripts\stability_metrics.py `
  --runs experiment_extension\data\runs `
  --out experiment_extension\data\stability_summary.json
```

The script also writes:

```text
experiment_extension/data/stability_summary.md
```

## How to regenerate manuscript figures

From the project root:

```powershell
python scripts\generate_figures_v0_3.py
```

The script writes SVG, PDF, PNG, and source-data files into:

```text
figures_v0.3/
```

The TIFF files used for manuscript submission are intentionally not required for repository use because they are large generated derivatives.

## Data and claim boundary

This artifact supports the following claims:

- structural traceability can be measured from normalized DFMEA rows;
- evidence and inference labels can be inspected row by row;
- RPN arithmetic consistency can be checked by script;
- repeated-run and ablation outputs can be summarized with the included script once generated.

This artifact does not support the following claims:

- the generated DFMEA is technically complete;
- the generated DFMEA is safer or more correct than expert analysis;
- the braking system is physically validated;
- any product is certified as safe or compliant.

## Suggested citation

See `CITATION.cff`.
