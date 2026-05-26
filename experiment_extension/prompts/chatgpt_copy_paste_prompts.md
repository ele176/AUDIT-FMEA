# ChatGPT Copy-Paste Prompts for AUDIT-FMEA

Use one prompt per new ChatGPT conversation.

Important:

- Output CSV only.
- Do not include Markdown explanations.
- Do not include code fences if possible.
- Use the exact CSV header provided.
- Use 12-20 rows for each output.
- Use unique item IDs for each run.

## Shared Schema and Evidence Pack

Use this schema:

```csv
method_id,item_id,subsystem,function,requirement_or_evidence_anchor,potential_failure_mode,potential_effect,severity_s,potential_cause,occurrence_o,current_control,detection_d,rpn,recommended_action,responsible_role,evidence_trace,critic_notes,status
```

System boundary:

- System: e-scooter mechanical braking subsystem.
- Included: brake lever; cable or hydraulic transmission path; brake caliper; brake pads; disc rotor; mounting hardware; wheel-level braking response.
- Excluded: battery; motor controller; regenerative braking logic unless directly interacting with mechanical braking; full vehicle dynamics; ABS control; road testing; physical measurement.

S/O/D anchors:

- Severity 8-10: severe braking loss, near-total braking failure, or catastrophic braking failure with crash/injury potential.
- Occurrence 1-3: rare or low; 4-6: plausible/moderate; 7-10: common or expected without controls.
- Detection 1-3: likely detected before use; 4-6: moderate detection; 7-10: difficult or hidden until braking demand.
- RPN = severity_s x occurrence_o x detection_d.
- High-risk threshold: RPN >= 180.
- High-severity threshold: severity_s >= 8.

Evidence pack for M3, M4, and ablations:

- S01: CPSC micromobility safety report. E-scooter safety is a substantial public safety issue. CPSC investigations associated brake problems with 40 e-scooter incidents. Reported brake-related scenarios included brakes not engaging, sporadic engagement, delayed or excessive engagement, and cable attachment problems.
- S02: UK Department for Transport e-scooter construction standards report. Braking requirements emphasize reliable stopping performance, brake-device presence, and braking performance under defined conditions.
- S03: EN 17128:2020 preview. Defines braking-system terminology for personal light electric vehicles, including brake, braking force, braking distance, braking device, and service brake system.
- S04: El Hassani et al. 2024 LLM-FMEA. LLMs have been explored for improving FMEA workflows. Manual FMEA is time-consuming and prone to omissions or inconsistency. LLM outputs still require engineering oversight and structured evaluation.
- S05: Knowledge graph-enhanced RAG for FMEA. RAG and structured knowledge representations have been proposed for FMEA-related generation and retrieval. Retrieval can improve grounding but does not guarantee complete or consistent risk analysis.
- S06: LLM plus RAG FMEA automation framework. Recent work proposes automating FMEA using LLMs and retrieval-augmented generation.
- S09: Seven failure points in RAG systems. RAG systems can fail through retrieval failures, missing content, wrong context, unsupported generation, or poor answer synthesis. Grounding must be paired with validation and traceability checks.
- S10: MechAgents. Multi-agent LLM collaboration has been explored for mechanics-related problem solving and knowledge integration. Agent role separation can support complex engineering reasoning but does not remove the need for validation.
- S11: Agentic LLMs for conceptual systems engineering and design. Agentic LLM workflows can support conceptual systems engineering and design tasks and should be evaluated for fidelity and consistency.

Evidence rules:

- For M3 and M4 variants, each row should contain source IDs or `engineering_inference:Sxx`.
- Use `engineering_inference:Sxx` when a row is a plausible inference from a source rather than directly stated.
- Do not claim physical braking-performance validation.
- If no source supports a row even indirectly, use `unsupported_candidate`.

---

## Prompt: M2_run02

You are generating `M2_run02.csv` for an experiment on LLM-assisted design FMEA.

Generate a single-LLM DFMEA for the e-scooter mechanical braking subsystem. Use only general engineering knowledge, the system boundary, the schema, and the S/O/D anchors. Do not use source IDs, retrieved evidence, evidence pack items, critic review, or multi-agent role separation.

Requirements:

- Generate 12-20 rows.
- Use `method_id = M2`.
- Item IDs must be `M2R2-001`, `M2R2-002`, etc.
- Set `evidence_trace = none`.
- Set `critic_notes = not_applicable`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M2_run03

You are generating `M2_run03.csv` for an experiment on LLM-assisted design FMEA.

Generate a single-LLM DFMEA for the e-scooter mechanical braking subsystem. Use only general engineering knowledge, the system boundary, the schema, and the S/O/D anchors. Do not use source IDs, retrieved evidence, evidence pack items, critic review, or multi-agent role separation.

Requirements:

- Generate 12-20 rows.
- Use `method_id = M2`.
- Item IDs must be `M2R3-001`, `M2R3-002`, etc.
- Set `evidence_trace = none`.
- Set `critic_notes = not_applicable`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M3_run02

You are generating `M3_run02.csv` for an experiment on RAG-LLM design FMEA.

Generate a RAG-grounded DFMEA for the e-scooter mechanical braking subsystem. Use the shared evidence pack and the required DFMEA schema. This is a single-workflow RAG baseline: do not perform separate critic review, mitigation review, or multi-agent role separation.

Requirements:

- Generate 12-20 rows.
- Use `method_id = M3`.
- Item IDs must be `M3R2-001`, `M3R2-002`, etc.
- Each row must include a source ID or `engineering_inference:Sxx` in `evidence_trace`.
- If a row is unsupported, use `unsupported_candidate`.
- Set `critic_notes = not_applicable`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M3_run03

You are generating `M3_run03.csv` for an experiment on RAG-LLM design FMEA.

Generate a RAG-grounded DFMEA for the e-scooter mechanical braking subsystem. Use the shared evidence pack and the required DFMEA schema. This is a single-workflow RAG baseline: do not perform separate critic review, mitigation review, or multi-agent role separation.

Requirements:

- Generate 12-20 rows.
- Use `method_id = M3`.
- Item IDs must be `M3R3-001`, `M3R3-002`, etc.
- Each row must include a source ID or `engineering_inference:Sxx` in `evidence_trace`.
- If a row is unsupported, use `unsupported_candidate`.
- Set `critic_notes = not_applicable`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M4_full_run02

You are generating `M4_full_run02.csv` for AUDIT-FMEA.

Execute the full AUDIT-FMEA workflow: function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, mitigation refinement, and integrity checking. Use the shared evidence pack, system boundary, schema, and S/O/D anchors.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4R2-001`, `M4R2-002`, etc.
- Each row must include source IDs or `engineering_inference:Sxx`.
- `critic_notes` must briefly state why the row was kept, revised, or bounded.
- Set `status = keep` unless a row is intentionally retained as `revise`.
- Calculate every RPN exactly as S x O x D.
- Do not claim physical braking-performance validation.
- Output CSV only with the exact header.

## Prompt: M4_full_run03

You are generating `M4_full_run03.csv` for AUDIT-FMEA.

Execute the full AUDIT-FMEA workflow: function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, mitigation refinement, and integrity checking. Use the shared evidence pack, system boundary, schema, and S/O/D anchors.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4R3-001`, `M4R3-002`, etc.
- Each row must include source IDs or `engineering_inference:Sxx`.
- `critic_notes` must briefly state why the row was kept, revised, or bounded.
- Set `status = keep` unless a row is intentionally retained as `revise`.
- Calculate every RPN exactly as S x O x D.
- Do not claim physical braking-performance validation.
- Output CSV only with the exact header.

## Prompt: M4_no_critic_run01

You are generating `M4_no_critic_run01.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the critic review stage. Do not perform a separate check for duplicates, unsupported rows, vague failure modes, boundary violations, or inconsistent S/O/D ratings. Keep evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, mitigation refinement, and final integrity checking.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NC1-001`, `M4NC1-002`, etc.
- Each row must include source IDs or `engineering_inference:Sxx`.
- Set `critic_notes = critic_ablation_not_performed`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M4_no_critic_run02

You are generating `M4_no_critic_run02.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the critic review stage. Do not perform a separate check for duplicates, unsupported rows, vague failure modes, boundary violations, or inconsistent S/O/D ratings. Keep evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, mitigation refinement, and final integrity checking.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NC2-001`, `M4NC2-002`, etc.
- Each row must include source IDs or `engineering_inference:Sxx`.
- Set `critic_notes = critic_ablation_not_performed`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M4_no_critic_run03

You are generating `M4_no_critic_run03.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the critic review stage. Do not perform a separate check for duplicates, unsupported rows, vague failure modes, boundary violations, or inconsistent S/O/D ratings. Keep evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, mitigation refinement, and final integrity checking.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NC3-001`, `M4NC3-002`, etc.
- Each row must include source IDs or `engineering_inference:Sxx`.
- Set `critic_notes = critic_ablation_not_performed`.
- Set `status = keep`.
- Calculate every RPN exactly as S x O x D.
- Output CSV only with the exact header.

## Prompt: M4_no_integrity_run01

You are generating `M4_no_integrity_run01.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the final integrity-check stage. Do not perform a final check for required fields, evidence traces, high-severity mitigation coverage, or RPN arithmetic. Keep function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, and mitigation refinement.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NI1-001`, `M4NI1-002`, etc.
- Each row should include source IDs or `engineering_inference:Sxx`, but do not run a final integrity pass.
- `critic_notes` must briefly state critic judgment.
- Set `status = keep`.
- Output CSV only with the exact header.

## Prompt: M4_no_integrity_run02

You are generating `M4_no_integrity_run02.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the final integrity-check stage. Do not perform a final check for required fields, evidence traces, high-severity mitigation coverage, or RPN arithmetic. Keep function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, and mitigation refinement.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NI2-001`, `M4NI2-002`, etc.
- Each row should include source IDs or `engineering_inference:Sxx`, but do not run a final integrity pass.
- `critic_notes` must briefly state critic judgment.
- Set `status = keep`.
- Output CSV only with the exact header.

## Prompt: M4_no_integrity_run03

You are generating `M4_no_integrity_run03.csv`, an ablation of AUDIT-FMEA.

Execute AUDIT-FMEA but omit the final integrity-check stage. Do not perform a final check for required fields, evidence traces, high-severity mitigation coverage, or RPN arithmetic. Keep function decomposition, evidence attribution, failure-mode generation, cause-effect reasoning, risk scoring, critic review, and mitigation refinement.

Requirements:

- Generate 12-20 final normalized rows.
- Use `method_id = M4`.
- Item IDs must be `M4NI3-001`, `M4NI3-002`, etc.
- Each row should include source IDs or `engineering_inference:Sxx`, but do not run a final integrity pass.
- `critic_notes` must briefly state critic judgment.
- Set `status = keep`.
- Output CSV only with the exact header.

