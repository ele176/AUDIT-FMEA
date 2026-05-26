# GitHub and Zenodo Release Checklist v0.3

Date: 2026-05-26

Artifact directory:

`AUDIT_FMEA_public_artifact_v0.3_for_github_zenodo`

## Recommended GitHub repository

Repository name:

`AUDIT-FMEA`

Suggested description:

Reproducibility artifact for auditable multi-agent DFMEA workflows.

Visibility before submission:

- Use a private repository if double-blind review is required.
- Use an anonymous reviewer-access route if the venue requires blind review.
- Make public only when allowed by the target venue or after acceptance.

## Release settings

Release tag:

`v0.3`

Release title:

`AUDIT-FMEA reproducibility artifact v0.3`

Release notes:

```text
This release contains the AUDIT-FMEA reproducibility artifact for the manuscript
"AUDIT-FMEA: Auditable Multi-Agent Workflows for Design Failure Analysis".

It includes prompts, compact evidence material, normalized DFMEA outputs,
repeated-run and role-ablation outputs, metric scripts, generated figure files,
source data, and manuscript-supporting documentation.

The artifact supports structural auditability analysis only. It does not provide
expert validation, physical braking tests, safety certification, or validated
S/O/D scoring.
```

## Zenodo settings

1. Connect the GitHub repository to Zenodo.
2. Enable Zenodo archiving for the repository.
3. Create GitHub release `v0.3`.
4. Let Zenodo archive the release and mint a DOI.
5. Replace all manuscript placeholders with the Zenodo DOI.

## Files to keep in GitHub

Keep:

- README, CITATION, LICENSE, artifact manifest;
- prompts, CSV, JSON, Markdown source files;
- metric scripts;
- figure source data;
- SVG/PDF/PNG figure outputs.

Do not commit unless needed:

- large TIFF files;
- temporary submission proofs;
- local screenshots;
- files containing private reviewer identities or teacher comments.

## Manuscript placeholders to replace

After DOI exists, update:

1. `manuscript_AUDIT_FMEA_topconf_v0.3.md`
2. `data_availability_fair_plan_v0.3.md`
3. `.zenodo.json` related identifier URL
4. Cover letter and submission metadata, if later created

