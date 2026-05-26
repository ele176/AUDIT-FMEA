# Supplementary File Manifest

## Prompts

| File | Description |
|---|---|
| `prompts/m1_template_only_fmea.md` | Template-only FMEA prompt |
| `prompts/m2_single_llm_fmea.md` | Single-LLM FMEA prompt |
| `prompts/m3_rag_llm_fmea.md` | RAG-LLM FMEA prompt |
| `prompts/m4_multi_agent_fmea.md` | Multi-agent FMEA prompt |

## Data

| File | Description |
|---|---|
| `data/dfmea_schema.md` | Common normalized DFMEA schema |
| `data/evidence_pack.md` | Compact source evidence pack |
| `data/dfmea_entries_all_methods.csv` | Combined normalized DFMEA rows for M1-M4 |

## Method Outputs

| File | Description |
|---|---|
| `method_outputs/m1_output.md` | M1 markdown output |
| `method_outputs/m1_dfmea.csv` | M1 DFMEA CSV |
| `method_outputs/m2_output.md` | M2 markdown output |
| `method_outputs/m2_dfmea.csv` | M2 DFMEA CSV |
| `method_outputs/m3_output.md` | M3 markdown output |
| `method_outputs/m3_dfmea.csv` | M3 DFMEA CSV |
| `method_outputs/m4_output.md` | M4 markdown output |
| `method_outputs/m4_dfmea.csv` | M4 DFMEA CSV |

## Scripts

| File | Description |
|---|---|
| `scripts/metrics.py` | Calculates structural metrics from normalized DFMEA CSV |

## Metric Outputs

| File | Description |
|---|---|
| `outputs/metrics_all_methods.json` | Structural metric JSON used in manuscript |
| `outputs/metrics_summary.md` | Human-readable metric summary |

## Figures

| File | Description |
|---|---|
| `figures/make_figures.py` | Figure-generation script |
| `figures/figure_01_row_count_traceability.svg` | Draft Figure 1 |
| `figures/figure_02_high_risk_items.svg` | Draft Figure 2 |
| `figures/figure_03_m4_workflow.svg` | Draft Figure 3 workflow schematic |
