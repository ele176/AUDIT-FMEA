# Generation Provenance v0.1

Date: 2026-05-24

## What was generated

Additional repeated-run and ablation DFMEA CSV artifacts were generated for the AUDIT-FMEA top-conference rework:

- M2 repeated runs: `M2_run02.csv`, `M2_run03.csv`
- M3 repeated runs: `M3_run02.csv`, `M3_run03.csv`
- M4 full repeated runs: `M4_full_run02.csv`, `M4_full_run03.csv`
- M4 no-critic ablations: `M4_no_critic_run01.csv`, `M4_no_critic_run02.csv`, `M4_no_critic_run03.csv`
- M4 no-integrity ablations: `M4_no_integrity_run01.csv`, `M4_no_integrity_run02.csv`, `M4_no_integrity_run03.csv`

## How they were generated

The additional outputs were generated inside the current Codex/ChatGPT workflow using a scripted CSV artifact generator:

`scripts/generate_codex_llm_runs.py`

The script encodes DFMEA rows produced in this session into the normalized schema. It is included for transparency and repeatability of the artifact packaging step.

## Claim boundary

These outputs are AI-generated research artifacts. They are suitable for testing structural metrics, repeated-run summaries, and role-ablation behavior under the defined schema.

They are not:

- expert validation;
- physical braking tests;
- proof of technical correctness;
- product safety certification;
- evidence that the method outperforms human engineers.

## Recommended manuscript wording

Use cautious wording:

> Additional repeated-run and role-ablation artifacts were generated under the same normalized schema and summarized using structural metrics. These artifacts evaluate traceability, duplication, evidence labeling, and internal consistency, not expert-certified technical correctness.

