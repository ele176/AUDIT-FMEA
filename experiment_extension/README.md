# AUDIT-FMEA Experiment Extension Pack

Purpose: strengthen the rejected AEI manuscript for a stronger conference or special issue by adding evidence that does not require physical equipment.

This pack supports three extensions:

1. repeated-run stability across LLM workflows;
2. role ablation for the proposed multi-agent workflow;
3. optional blinded expert plausibility scoring.

The pack does not fabricate new experimental results. It creates the protocol, data templates, prompts, and metric scripts needed to produce defensible new evidence.

## Folder layout

| Folder | Purpose |
|---|---|
| `data/runs/` | Put normalized CSV outputs from each repeated run or ablation here |
| `prompts/` | Prompt protocols for repeated-run and ablation experiments |
| `scripts/` | Metric scripts for stability and ablation summaries |
| `expert_review_pack/` | Blinded scoring materials for teachers, classmates, or engineers |

## Naming convention for run CSVs

Use:

`<variant>_run<NN>.csv`

Examples:

- `M2_run01.csv`
- `M3_run01.csv`
- `M4_full_run01.csv`
- `M4_no_critic_run01.csv`
- `M4_no_integrity_run01.csv`
- `M4_no_evidence_labels_run01.csv`

Each CSV must use the same normalized schema as the original DFMEA data.

## Minimum recommended experiment

If time is tight:

- run `M2`, `M3`, and `M4_full` three times each;
- run `M4_no_critic` and `M4_no_integrity` three times each;
- compute stability metrics;
- discuss results as structural evidence, not technical correctness.

## Stronger experiment

If time allows:

- five runs each for `M2`, `M3`, `M4_full`, and all ablations;
- one blinded plausibility review from a mechanical/reliability person;
- public artifact deposit through OSF, Zenodo, GitHub, or an institutional repository.

## Run the summary script

From the project root:

```powershell
python paper_project\08_top_conference_rework\experiment_extension\scripts\stability_metrics.py `
  --runs paper_project\08_top_conference_rework\experiment_extension\data\runs `
  --out paper_project\08_top_conference_rework\experiment_extension\data\stability_summary.json
```

The script also writes a Markdown table next to the JSON output.

