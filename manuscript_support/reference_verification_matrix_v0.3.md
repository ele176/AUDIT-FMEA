# Reference Verification Matrix v0.3

Date: 2026-05-27

Status: working citation-audit file. The GitHub artifact is public and archived by Zenodo.

## Artifact access status

| Item | Status |
|---|---|
| GitHub repository | Created and pushed |
| Repository URL | `https://github.com/ele176/AUDIT-FMEA` |
| Visibility | Public |
| Release | `v0.3.1` created to trigger Zenodo archiving |
| Release URL | `https://github.com/ele176/AUDIT-FMEA/releases/tag/v0.3.1` |
| Zenodo DOI | `10.5281/zenodo.20405407` |
| Zenodo record | `https://zenodo.org/records/20405407` |

## Verified reference candidates

| ID | Candidate reference | Verified metadata | Use in paper | Status |
|---|---|---|---|---|
| R1 | Charan, Singh, Redhu, Soni, RAG-FMEA | Springer page verifies title, venue, volume 17(5), pages 1495-1509, DOI `10.1007/s13198-026-03171-6` | Direct RAG-FMEA baseline | Keep |
| R2 | El Hassani, Masrour, Kourouma, Motte, Tavcar, LLM-FMEA | Design Society page verifies DESIGN 2024 paper, pages 2019-2028, DOI `10.1017/pds.2024.204` | Direct LLM-FMEA prior work | Keep |
| R3 | Bahr et al., KG-enhanced RAG for FMEA | Journal of Industrial Information Integration 45, 100807, DOI `10.1016/j.jii.2025.100807` | Direct KG-RAG-FMEA comparison | Keep |
| R4 | Barnett et al., RAG failure points | ACM/CAIN 2024 metadata verifies pages 194-199 and DOI `10.1145/3644815.3644945`; arXiv version `2401.05856` | Explain why RAG needs audit/evaluation gates | Keep |
| R5 | Ni and Buehler, MechAgents | ScienceDirect verifies Extreme Mechanics Letters article and DOI `10.1016/j.eml.2024.102131` | Multi-agent mechanics/engineering precedent | Keep |
| R6 | Li and Corney, MechRAG | Nature Communications Engineering / Edinburgh record verifies DOI `10.1038/s44172-025-00517-z` | Mechanical RAG and multimodal engineering context | Keep |
| R7 | IEC 60812:2018 | IEC webstore verifies standard title and FMEA/FMECA scope | FMEA/DFMEA standards background | Keep |
| R8 | AIAG and VDA FMEA Handbook | AIAG/VDA pages verify 2019 handbook and DFMEA/PFMEA/MSR use | Automotive DFMEA method context | Keep |
| R9 | Liu et al., FMEA with MCDM systematic review | ScienceDirect verifies Computers & Industrial Engineering DOI `10.1016/j.cie.2019.06.055` | FMEA risk-prioritisation background | Keep |
| R10 | UK DfT e-scooter construction standards report | GOV.UK PDF verifies EN 17128:2020 and braking-context material | Case boundary support only | Keep |
| R11 | U.S. CPSC micromobility hazard report | CPSC page verifies 2017-2024 micromobility hazard report | Case relevance support only | Keep |

## Recommended manuscript use

1. Use R1-R3 to position AUDIT-FMEA against LLM-FMEA, RAG-FMEA, and KG-RAG-FMEA.
2. Use R4 to justify why retrieval is not enough without audit gates.
3. Use R5-R6 to connect the paper to mechanical engineering LLM agents and mechanical RAG.
4. Use R7-R9 to show the paper respects FMEA/DFMEA methodology rather than replacing it.
5. Use R10-R11 only to motivate the braking-system case. Do not use them as validation evidence.

## Remaining citation work

1. Add 4-6 more intelligent-manufacturing / design-informatics references.
2. Add 2-3 references on evaluation and traceability for LLM/RAG systems.
3. Decide target venue before final citation style formatting.
4. Re-run reference audit after all references are integrated into the manuscript.

## Source URLs used in this audit

- https://link.springer.com/article/10.1007/s13198-026-03171-6
- https://www.designsociety.org/publication/48437/integrating_large_language_models_for_improved_failure_mode_and_effects_analysis_fmea_a_framework_and_case_study
- https://fis.uni-bamberg.de/entities/publication/c453c81f-6d5d-497e-ad09-2f72399e2b2f
- https://dl.acm.org/doi/10.1145/3644815.3644945
- https://www.sciencedirect.com/science/article/abs/pii/S2352431624000117
- https://www.nature.com/articles/s44172-025-00517-z
- https://webstore.iec.ch/en/publication/26359
- https://www.aiag.org/training-and-resources/manuals/details/FMEAAV-1
- https://www.sciencedirect.com/science/article/pii/S0360835219303857
- https://assets.publishing.service.gov.uk/media/67ac4d545d27cee6cccec4c3/technical-research-into-construction-standards-for-e-scooters.pdf
