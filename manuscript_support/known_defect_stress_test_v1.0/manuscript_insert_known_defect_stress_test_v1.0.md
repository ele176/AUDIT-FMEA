# Manuscript Insert: Known-Defect Stress Test v1.0

## Methods insert

### Known-defect stress test

To reduce the risk that the auditability metrics merely rewarded the workflow for emitting its own preferred artifact structure, a known-defect stress test was added as a negative control. Twelve deliberately corrupted DFMEA rows were constructed under the same normalized schema. Each row contained one expected artifact defect: missing evidence trace, incorrect RPN arithmetic, duplicate row membership, generic failure labeling, out-of-bound subsystem content, missing mitigation for a high-severity row, mitigation-cause mismatch, invalid S/O/D value, missing required field, or unsupported evidence marker. The stress test mapped these defects to the two post-generation gates used by AUDIT-FMEA: formal integrity checks and critic-style semantic checks. The test was deterministic and script-computed. It was designed to evaluate whether the audit protocol detects known artifact defects, not whether any generated DFMEA row is mechanically correct.

## Results insert

### Known-defect stress-test results

The known-defect stress test included 12 deliberately corrupted DFMEA rows. All 12 expected row-level defect labels were detected, giving a row-level detection recall of 1.000. The integrity-oriented checks detected 7/7 expected formal defects, including missing evidence traces, RPN mismatch, invalid S/O/D values, missing current control, missing recommended action, and an unsupported-candidate evidence marker. The critic-oriented checks detected 5/5 expected semantic defects, including duplicate pair membership, generic failure labeling, out-of-bound subsystem content, and mitigation-cause mismatch. One duplicate pair was detected as intended. These results strengthen the claim that AUDIT-FMEA's review gates can identify pre-specified structural and semantic artifact defects. They do not validate braking safety, calibrated S/O/D ratings, mitigation effectiveness, or the expert correctness of generated DFMEA rows.
