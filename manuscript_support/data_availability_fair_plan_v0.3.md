# Data Availability and FAIR Plan v0.3

Date: 2026-05-26

Skill basis: `nature-data`

## Dataset inventory

| Material | Current location in project | Access route before submission | Notes |
|---|---|---|---|
| Evidence pack | `AUDIT_FMEA_public_artifact_v0.1/original_reproducibility_package/data/evidence_pack.md` | Public repository | Compact public-source evidence only |
| Normalized DFMEA outputs | `original_reproducibility_package/method_outputs/` | Public repository | M1-M4 normalized outputs |
| Combined DFMEA table | `original_reproducibility_package/data/dfmea_entries_all_methods.csv` | Public repository | Supports structural metric recomputation |
| Metric scripts | `original_reproducibility_package/scripts/metrics.py` and `experiment_extension/scripts/stability_metrics.py` | Public repository | Python scripts for recomputing metrics |
| Repeated-run and ablation outputs | `experiment_extension/data/runs/` | Public repository | AI-generated research artifacts |
| Run manifest | `experiment_extension/data/run_manifest.csv` | Public repository | Required provenance file |
| Summary data | `experiment_extension/data/stability_summary.json` and `.md` | Public repository | Used for repeated-run and ablation table |
| Expert scoring data | Not available | Not applicable in current version | Must not be implied |
| Physical braking-test data | Not available | Not applicable in current version | Must not be implied |

## Recommended repository route

Selected route:

1. Create a GitHub repository for the artifact package.
2. Create a versioned release, for example `v0.1`.
3. Archive the release in Zenodo to obtain a DOI.
4. Use Zenodo's reviewer-access/private-link workflow if the venue needs anonymous review before publication.

Current status:

The GitHub repository and `v0.3` release have been created, and the repository is now public. Zenodo DOI minting is pending GitHub-Zenodo integration and archive triggering.

Alternative route:

Use OSF if a simpler project page and anonymous review link are more convenient. A DOI should still be minted before final publication if the venue permits.

Avoid:

- personal cloud-drive links as the only archive;
- temporary Google Drive or Baidu Netdisk links;
- GitHub-only availability without a release DOI for the final version;
- claiming `Supplementary File 1` if the submission system does not actually upload it.

## Ready-to-paste Data Availability statement

Data Availability

The data and code supporting this study are available in a public versioned GitHub release and will be archived on Zenodo. The repository package includes the evidence pack, prompts, normalized DFMEA outputs, repeated-run and role-ablation outputs, metric scripts, run manifest, generated summary tables, figure source data, and generated figure files. The Zenodo DOI will be added here after archiving: [ZENODO DOI]. These materials support recomputation of the structural auditability metrics reported in the manuscript. They do not contain expert validation data, physical braking-test data, or safety-certification evidence.

## Dataset citation template

Use this after the repository record exists:

Chris Wei (2026). AUDIT-FMEA reproducibility artifact for auditable multi-agent design failure analysis, version 0.3. Zenodo. [DOI].

## FAIR checklist

| FAIR item | Status | Action |
|---|---|---|
| Persistent identifier | Missing | Deposit in Zenodo, OSF, Figshare, Dryad, or institutional repository |
| Public landing page | Missing | Create repository record with title, abstract, creator, affiliation, and date |
| File manifest | Present | Keep `ARTIFACT_MANIFEST.md` and `SUPPLEMENTARY_FILE_MANIFEST.md` |
| README | Present | Ensure it explains how to recompute each table |
| Licence | Present | Confirm licence matches intended reuse |
| Provenance | Partial | Keep run manifest; add model/interface/date notes where available |
| Source-data mapping | Partial | Map each manuscript table/figure to source files |
| Versioning | Partial | Use release tag `v0.1`; update to `v1.0` before final submission if files change |
| Reviewer access | Missing | Generate anonymous reviewer link before double-blind submission |

## Risk flags

1. A manuscript that promises a supplementary file without an uploaded file or repository link is at risk of desk rejection or administrative query.
2. A repository link that contains the author's identity may conflict with double-blind review; use anonymous reviewer access when needed.
3. The current package supports structural reproducibility only. It cannot be described as validation, safety testing, or expert-confirmed FMEA truth.
