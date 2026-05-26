# Figure Contracts v0.3

Date: 2026-05-26

Skill basis: `nature-figure`

Important gate status: Python was selected by the author and used exclusively for figure rendering, exporting, and QA.

## Figure 1: AUDIT-FMEA workflow and audit trail

Core conclusion:
AUDIT-FMEA turns LLM-assisted DFMEA from a final-table generation task into an auditable artifact pipeline with explicit evidence, critique, and integrity gates.

Figure archetype:
Schematic-led composite.

Target output:
High-impact conference or journal figure, editable vector first, high-resolution raster second.

Backend:
Python.

Rendered files:
`figures_v0.3/Figure_1_AUDIT_FMEA_workflow_v0.3.svg`, `.pdf`, `.png`, `.tiff`.

Final size:
Preferred full-width figure. Candidate width: 170-180 mm. Height should remain compact enough to fit with a caption on one page.

Panel map:

| Panel | Role | Content |
|---|---|---|
| a | Hero workflow | Eight roles from function mapping to integrity checking |
| b | Artifact trail | Evidence pack, candidate rows, critic notes, final table, metric report |
| c | Claim boundary | Structural auditability inside scope; expert validation and physical safety outside scope |

Evidence hierarchy:

- Hero evidence: role separation and inspectable artifacts.
- Validation evidence: output artifacts and metric scripts exist in the reproducibility package.
- Controls/robustness: repeated-run and ablation results shown in Figure 2 or Table 2.

Reviewer risk:
If this figure looks like a generic agent diagram, reviewers may dismiss the contribution as prompt engineering. The final figure must foreground audit artifacts, not agent icons.

## Figure 2: Structural metrics across methods

Core conclusion:
The full AUDIT-FMEA workflow preserves traceability and internal consistency while exposing more inspectable high-consequence candidates than the baselines in the current case.

Figure archetype:
Quantitative grid.

Backend:
Python.

Rendered files:
`figures_v0.3/Figure_2_structural_metrics_v0.3.svg`, `.pdf`, `.png`, `.tiff`.

Panel map:

| Panel | Role | Content |
|---|---|---|
| a | Main comparison | M1-M4 row count, evidence trace rate, high-severity item count |
| b | Integrity defects | Invalid rate, duplicate pairs, RPN mismatches |
| c | Boundary note | Small visual tag: structural metrics only, not expert correctness |

Source data needed:

- Initial metrics table for M1-M4.
- Recomputed metric JSON for all methods.

Reviewer risk:
Do not make the plot imply technical correctness. The visual title and caption must say "structural metrics" or "auditability metrics".

## Figure 3: Repeated-run and ablation evidence

Core conclusion:
The critic and integrity roles are linked to measurable structural defects when removed.

Figure archetype:
Asymmetric mixed-modality figure.

Backend:
Python.

Rendered files:
`figures_v0.3/Figure_3_repeated_run_ablation_v0.3.svg`, `.pdf`, `.png`, `.tiff`.

Panel map:

| Panel | Role | Content |
|---|---|---|
| a | Compact ablation table plot | M4_full vs M4_no_critic vs M4_no_integrity |
| b | Defect examples | One vague/duplicate example and one RPN-integrity example |
| c | Repeated-run stability | Mean +/- sd for invalid rate, evidence trace, duplicate pairs, RPN mismatch |

Source data needed:

- Stability summary JSON or CSV.
- Representative row examples from ablation outputs.

Reviewer risk:
The caption must state that the repeated runs are generated research artifacts under a documented workflow, not independent physical experiments.

## Backend record

Selected backend: Python.

Generation script:

`scripts/generate_figures_v0_3.py`
