# Literature Search and Verification Plan v0.3

Date: 2026-05-26

Skill basis: `nature-academic-search`

## Purpose

The AEI rejection identified insufficient novelty for an engineering-informatics readership. The revised literature strategy must show that AUDIT-FMEA is not just another LLM-FMEA generator. The paper should position itself around auditable artifact workflows, role ablations, traceability, and integrity gates.

## Search concepts

| Concept | Search terms |
|---|---|
| LLM-assisted FMEA | `"large language model" FMEA`, `"LLM" "failure mode and effects analysis"`, `"generative AI" FMEA` |
| RAG for FMEA | `"retrieval augmented generation" FMEA`, `"RAG" FMEA`, `"knowledge graph" "FMEA"` |
| Agentic engineering workflows | `"multi-agent" "engineering design" LLM`, `"agentic" "intelligent manufacturing"`, `"foundation models" "manufacturing"` |
| Auditability and evaluation | `"LLM evaluation" "traceability"`, `"RAG evaluation" "failure points"`, `"AI-assisted engineering" "auditability"` |
| Standards and mechanical context | `DFMEA standard`, `SAE J1739`, `IEC 60812`, `AIAG VDA FMEA`, `e-scooter braking construction standard` |

## Source routing

Primary sources:

1. CrossRef and publisher pages for peer-reviewed articles.
2. SAE, IEC, AIAG/VDA, CPSC, and government pages for standards and safety context.
3. arXiv only for preprints that are directly relevant and clearly labelled as preprints.

Secondary sources:

1. Semantic Scholar for citation graph expansion.
2. Google Scholar manually if CrossRef/publisher search misses key engineering papers.

Avoid:

- citing blogs or Reddit;
- citing search snippets without checking the underlying page;
- using unverified AI-generated reference metadata.

## Verified seed references from current search

These are seed items found or checked during the v0.3 search pass. Full reference formatting still needs a citation audit.

| Topic | Verified seed | Why it matters |
|---|---|---|
| LLM-assisted FMEA | El Hassani et al., "Integrating large language models for improved failure mode and effects analysis (FMEA): a framework and case study", DESIGN 2024, DOI `10.1017/pds.2024.204`, Design Society page: https://www.designsociety.org/publication/48437/integrating_large_language_models_for_improved_failure_mode_and_effects_analysis_fmea_a_framework_and_case_study | Direct prior work on LLM-FMEA; must be distinguished from AUDIT-FMEA |
| RAG-FMEA | Charan et al., "A framework for automating failure modes and effects analysis (FMEA) using large language models (LLMs) and retrieval-augmented generation (RAG)", IJSAEM 17(5), 1495-1509, DOI `10.1007/s13198-026-03171-6`, RePEc/Springer metadata: https://ideas.repec.org/a/spr/ijsaem/v17y2026i5d10.1007_s13198-026-03171-6.html | Strong direct baseline for RAG-LLM FMEA |
| KG-RAG for FMEA | Bahr et al., "Knowledge graph enhanced retrieval-augmented generation for failure mode and effects analysis", Journal of Industrial Information Integration 45, 100807, DOI `10.1016/j.jii.2025.100807`, University of Bamberg record: https://fis.uni-bamberg.de/entities/publication/c453c81f-6d5d-497e-ad09-2f72399e2b2f | Shows graph/RAG prior art; AUDIT-FMEA must claim audit workflow rather than retrieval superiority |
| DFMEA standard | SAE J1739_202605, "Potential Failure Mode and Effects Analysis (FMEA) Including Design FMEA, Supplemental FMEA-MSR, and Process FMEA", DOI `10.4271/J1739_202605`, SAE Mobilus page: https://saemobilus.sae.org/standards/j1739_202605-potential-failure-mode-effects-analysis-fmea-including-design-fmea-supplemental-fmea-msr-process-fmea | Current DFMEA standard metadata; useful for terminology and audit framing |
| Micromobility safety context | U.S. CPSC, "Micromobility Products-Related Deaths, Injuries and Hazard Patterns 2017-2024", April 2026, CPSC page: https://www.cpsc.gov/content/Micromobility-Products-Related-Deaths-Injuries-and-Hazard-Patterns-2017-2024 | Supports case relevance, not technical validation |
| E-scooter construction context | UK Department for Transport, "Construction standards for e-scooters", 29 January 2025, GOV.UK page: https://www.gov.uk/government/publications/construction-standards-for-e-scooters | Supports braking-system boundary and public construction-standard context |

## Required expansion before submission

Minimum target for a serious conference/journal version:

| Category | Minimum count | Examples |
|---|---:|---|
| FMEA/DFMEA standards and methodology | 4-6 | IEC 60812, SAE J1739, AIAG/VDA FMEA, FMEA review papers |
| LLM/RAG for FMEA or reliability analysis | 5-8 | LLM-FMEA, RAG-FMEA, KG-RAG-FMEA |
| Multi-agent LLMs for engineering or scientific workflows | 5-8 | Agentic design, multi-agent critique, verification agents |
| RAG evaluation and failure modes | 4-6 | retrieval failures, hallucination, traceability, source attribution |
| Intelligent manufacturing / design informatics | 5-8 | AI-assisted design review, digital engineering, manufacturing knowledge systems |
| Micromobility/braking context | 3-5 | CPSC, DfT, EN 17128, braking requirements |

## Citation-audit checklist

1. Every reference must have a DOI, publisher URL, standard identifier, or official government URL where applicable.
2. Titles, authors, page ranges, volume, article number, and year must be checked against the publisher or official record.
3. Preprints must be labelled as preprints.
4. Standards must not be used as if they validate the case results.
5. No citation should be added only because it sounds relevant; it must support a specific claim in the manuscript.

