# Known-Defect Stress Test v1.0

Purpose: test whether AUDIT-FMEA's critic and integrity defect classes flag deliberately injected DFMEA artifact defects.

This is a structural negative-control test. It does not validate braking safety, S/O/D calibration, mitigation effectiveness, or expert correctness.

## Summary

- Injected rows: 12
- Expected row-level defect labels: 12
- Detected expected defect labels: 12
- Row-level detection recall: 1.0
- Duplicate pairs detected: 1
- Integrity expected/detected: 7/7
- Critic expected/detected: 5/5
- False-negative rows: none

## Detection Results

| Item | Injected defect | Expected detector | Detected reasons | Result |
|---|---|---|---|---|
| KD-001 | missing_evidence_trace | integrity:missing_required_evidence_trace | missing_required_evidence_trace | PASS |
| KD-002 | wrong_rpn | integrity:rpn_mismatch | rpn_mismatch | PASS |
| KD-003A | duplicate_pair_member | critic:duplicate_pair_member | duplicate_pair_member | PASS |
| KD-003B | duplicate_pair_member | critic:duplicate_pair_member | duplicate_pair_member | PASS |
| KD-004 | generic_failure_label | critic:too_vague_failure_mode | too_vague_failure_mode | PASS |
| KD-005 | out_of_scope_boundary | critic:out_of_scope_boundary | out_of_scope_boundary | PASS |
| KD-006 | missing_high_severity_mitigation | integrity:missing_recommended_action | missing_recommended_action | PASS |
| KD-007 | mitigation_cause_mismatch | critic:mitigation_cause_mismatch | mitigation_cause_mismatch | PASS |
| KD-008 | invalid_severity | integrity:invalid_severity | invalid_severity | PASS |
| KD-009 | invalid_detection | integrity:invalid_detection | invalid_detection | PASS |
| KD-010 | missing_required_field | integrity:missing_current_control | missing_current_control | PASS |
| KD-011 | unsupported_candidate_evidence | integrity:missing_required_evidence_trace | missing_required_evidence_trace | PASS |

## Claim Boundary

Supports defect-detection and audit-protocol claims for injected structural/semantic artifact defects; does not validate real braking safety, S/O/D accuracy, or row correctness.
