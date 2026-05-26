# GitHub Upload Commands v0.3

Use these commands after GitHub CLI authentication is fixed.

Artifact repository directory:

`C:\aicoding\lihuilunwen\paper_project\08_top_conference_rework\AUDIT_FMEA_public_artifact_v0.3_for_github_zenodo`

## 1. Re-authenticate GitHub CLI

```powershell
gh auth login -h github.com
```

Choose:

- GitHub.com
- HTTPS
- Authenticate with browser

## 2. Create a private GitHub repository

```powershell
gh repo create AUDIT-FMEA --private --source "C:\aicoding\lihuilunwen\paper_project\08_top_conference_rework\AUDIT_FMEA_public_artifact_v0.3_for_github_zenodo" --remote origin --push
```

Use private first if the target venue requires double-blind review.

## 3. Create release v0.3

```powershell
gh release create v0.3 "C:\aicoding\lihuilunwen\paper_project\08_top_conference_rework\AUDIT_FMEA_public_artifact_v0.3_for_github_zenodo.zip" --title "AUDIT-FMEA reproducibility artifact v0.3" --notes-file "C:\aicoding\lihuilunwen\paper_project\08_top_conference_rework\release_notes_v0.3.md"
```

## 4. Zenodo

After the GitHub release exists:

1. Open Zenodo.
2. Connect GitHub.
3. Make the GitHub repository public if using the standard GitHub-Zenodo integration.
4. Enable archiving for `AUDIT-FMEA`.
5. Recreate or archive release `v0.3`.
6. Copy the DOI into the manuscript Data and Code Availability section.
