# AUDIT-FMEA Public Artifact v0.5

This repository package supports the manuscript:

**AUDIT-FMEA: Auditable Multi-Agent Workflows for Design Failure Analysis**

## Purpose

The artifact contains prompts, compact evidence material, normalized DFMEA outputs, metric scripts, initial results, repeated-run and role-ablation outputs, a second mechanical braking transfer case, generated figures, source data, a data provenance/evidence-boundary audit, and manuscript-supporting documentation.

The artifact is intended to support procedural auditability. It does not provide physical braking validation, safety certification, or expert-certified technical correctness.

## Contents

| Folder | Description |
|---|---|
| `original_reproducibility_package/` | Original AEI submission reproducibility files: evidence pack, prompts, method outputs, metric scripts, and initial metric outputs |
| `experiment_extension/` | Top-conference extension package: ChatGPT manual runbook, repeated-run prompts, ablation prompts, run manifest, stability script, generated run CSVs, and stability summaries |
| `second_case_bicycle_disc_brake_v1.0/` | Bicycle/e-bike mechanical disc brake transfer case: evidence pack, normalized M4 DFMEA rows, recomputed structural metrics, and manuscript-insert notes |
| `figures_v0.3/` | Publication figure outputs in SVG, PDF, and PNG, plus source data |
| `scripts/generate_figures_v0_3.py` | Python script used to regenerate Figures 1-3 |
| `manuscript_support/` | Data availability, figure contracts, literature-search support files, and the data evidence-chain audit |

## Current evidence status

The current package includes the original single-run outputs for M2, M3, and M4 as `run01` seeds, additional repeated-run and role-ablation outputs generated during the top-conference rework, a second bicycle/e-bike mechanical disc brake transfer-case artifact, and a row-level data provenance audit. These outputs are AI-generated and author-verified research artifacts under the documented workflow. They support structural auditability analysis only.

## How to inspect data provenance and evidence boundaries

The data evidence-chain audit is stored in:

```text
manuscript_support/data_evidence_chain_v1.0/
```

Start with:

```text
manuscript_support/data_evidence_chain_v1.0/data_evidence_chain_report_v1.0.md
```

The row-level CSV maps each retained primary-case and transfer-case AUDIT-FMEA row to source IDs, engineering-inference labels, generation route, field provenance, RPN arithmetic status, and unsupported claim boundaries.

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

## How to recompute the second-case metrics

From the project root:

```powershell
python experiment_extension\scripts\stability_metrics.py `
  --runs second_case_bicycle_disc_brake_v1.0\runs `
  --out second_case_bicycle_disc_brake_v1.0\case2_structural_metrics_v1.0.json
```

The script also writes:

```text
second_case_bicycle_disc_brake_v1.0/case2_structural_metrics_v1.0.md
```

## Data and claim boundary

This artifact supports the following claims:

- structural traceability can be measured from normalized DFMEA rows;
- evidence and inference labels can be inspected row by row;
- field-level provenance and claim boundaries can be inspected in the data evidence-chain audit;
- RPN arithmetic consistency can be checked by script;
- repeated-run and ablation outputs can be summarized with the included script once generated.
- the second mechanical braking transfer case can be recomputed with the same structural metric script.

This artifact does not support the following claims:

- the generated DFMEA is technically complete;
- the generated DFMEA is safer or more correct than expert analysis;
- the braking system is physically validated;
- any product is certified as safe or compliant.

## Suggested citation

See `CITATION.cff`.
