# Manuscript Insert: Second Mechanical Braking Case v1.0

Date: 2026-05-27

Purpose: provide ready-to-integrate text for adding a bicycle/e-bike mechanical disc brake transfer case to the AUDIT-FMEA manuscript.

## Abstract replacement sentence

Replace the current one-case result sentence with:

> In an electric-scooter braking-system case and a bicycle/e-bike mechanical disc brake transfer case, we evaluate whether the workflow preserves row-level evidence traces, required-field validity, duplicate control, and RPN arithmetic consistency under a shared DFMEA schema.

Add after the repeated-run sentence:

> The transfer case produced 18 author-verified DFMEA rows with full evidence traceability, zero duplicate pairs, zero invalid rows, and zero RPN arithmetic mismatches, supporting a bounded cross-case auditability claim rather than a braking-safety validation claim.

## Introduction addition

Add near the end of Section 1:

> To reduce dependence on a single micromobility braking example, the revised study adds a second mechanical braking case: bicycle/e-bike mechanical disc brakes. The second case uses independent public evidence from bicycle/e-bike brake recalls, bicycle braking requirements, and a mechanical disc brake technical manual. This extension tests whether AUDIT-FMEA can transfer its evidence-labeling and integrity-check pattern to a related but distinct mechanical brake architecture.

## Method addition

Add after the current case-boundary subsection:

### 4.7 Second mechanical braking transfer case

To test transferability beyond the electric-scooter braking case, a second case was constructed for bicycle/e-bike mechanical disc brakes. The included boundary covered brake levers, mechanical cable and housing, cable-fixing interfaces, caliper actuator arms, mechanical calipers, mounting hardware, pads, disc rotors, pad-rotor clearance, and wheel-level braking response. The excluded boundary covered motor control, regenerative braking, battery safety, non-brake frame failure, rider-behavior modeling, and physical stopping-distance testing.

The evidence pack was built from four public source groups: a CPSC recall involving e-bike mechanical disc brake calipers, a CPSC recall involving TRP/Tektro Spyre mechanical disc brake calipers, 16 CFR 1512.5 bicycle braking-system requirements, and a Shimano dealer manual for mechanical disc brakes. Each generated DFMEA row was required to include either a direct source identifier or an engineering-inference tag. The same normalized schema and structural metric script used in the first case were applied to the transfer case.

This transfer case was not designed as an independent safety validation. It was used to test whether the workflow can produce a structurally auditable DFMEA artifact when the subsystem, evidence sources, and mechanical details differ from the first case.

## Results addition

Add after the ablation results:

### 5.5 Transfer case: bicycle/e-bike mechanical disc brakes

The bicycle/e-bike mechanical disc brake transfer case produced 18 author-verified AUDIT-FMEA rows. The rows covered lever compatibility, cable protrusion, cable fixing, cable degradation, actuator-arm over-rotation, caliper failure, caliper mounting, mounting-interface alignment, pad clearance, pad wear, pad retention, friction contamination, rotor condition, rotor-side hardware interference, wet-condition response, front-wheel lock tendency, and final assembly verification.

The structural metrics were consistent with the intended auditability claim: row count = 18, invalid rate = 0.000, duplicate pair count = 0, evidence trace rate = 1.000, high-RPN item count = 6, high-severity item count = 14, and RPN arithmetic mismatch count = 0. These results do not show that the generated rows are complete or expert-correct. They show that the AUDIT-FMEA workflow can be transferred to a second mechanical braking subsystem while preserving row-level traceability and formal consistency.

## Discussion addition

Add to the limitations paragraph:

> The second case reduces but does not eliminate the single-case threat to validity. Both cases remain in the broader micromobility/mechanical braking family, and neither includes proprietary design records, physical braking tests, or expert-validated S/O/D scores. The revised claim is therefore cross-case structural auditability within related mechanical braking subsystems, not general validity across all mechanical systems.

## Data Availability addition

Update the Data Availability statement after the second-case folder is included in the public artifact:

> The repository package also includes the bicycle/e-bike mechanical disc brake transfer-case evidence pack, normalized DFMEA CSV, structural metric outputs, and manuscript-insert notes used for the cross-case auditability extension.

## Citation additions to reference matrix

Add the following public sources to the verified-reference matrix if they are cited in the manuscript:

- U.S. Consumer Product Safety Commission. Lectric Ebikes Recalls Disc Brake Calipers Sold on Lectric E-Bicycles Due to Crash and Injury Hazards. Recall Alert. September 7, 2023.
- U.S. Consumer Product Safety Commission. Tektro USA and TRP Recall Bicycle Mechanical Disc Brake Calipers. Recall Alert. March 6, 2014.
- 16 CFR 1512.5. Requirements for braking system.
- Shimano. Dealer's Manual: Mechanical Disc Brakes BR-TX805 and BR-M375. DM-BR0007-04.

## Integration note

Do not claim expert validation for this second case until returned blind-review forms are analyzed. Use the phrase "author-verified transfer case" or "structural transfer case" rather than "validated case".
