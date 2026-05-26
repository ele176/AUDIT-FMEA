# Repeated-Run Protocol for AUDIT-FMEA

Purpose: test whether LLM-assisted DFMEA outputs are structurally stable across repeated runs under the same documented prompt protocol.

## Variants

Run these variants at least three times each:

1. `M2`: single-LLM DFMEA without retrieved evidence.
2. `M3`: RAG-LLM DFMEA using the compact evidence pack.
3. `M4_full`: full AUDIT-FMEA with evidence role, critic role, mitigation refinement, and integrity checking.

## Constants

Use the same:

- system boundary;
- DFMEA schema;
- S/O/D anchors;
- evidence pack version;
- output column schema;
- requested row range;
- model/provider if possible.

Record the model name, provider, date, temperature, top-p, seed/session ID if available, and any interface limitations in `data/run_manifest.csv`.

## Output format

Each run must be normalized into the CSV schema:

```text
method_id,item_id,subsystem,function,requirement_or_evidence_anchor,potential_failure_mode,potential_effect,severity_s,potential_cause,occurrence_o,current_control,detection_d,rpn,recommended_action,responsible_role,evidence_trace,critic_notes,status
```

Use variant-specific IDs:

- `M2R1-001`, `M2R1-002`, ...
- `M3R1-001`, `M3R1-002`, ...
- `M4R1-001`, `M4R1-002`, ...

The `method_id` field should be one of:

- `M2`
- `M3`
- `M4`

The variant is tracked by the file name and run manifest.

## M2 prompt

You are an expert mechanical design engineer preparing a design FMEA for an electric scooter mechanical braking subsystem. The included components are brake lever, cable or hydraulic transmission path, brake caliper, brake pads, disc rotor, mounting hardware, and wheel-level braking response. Generate 12-20 DFMEA rows using the required schema. Use the provided S/O/D anchors and calculate RPN as S x O x D. Do not cite sources, retrieve documents, or perform a separate critique. Make the entries specific enough to support design review. Output only the normalized CSV rows.

## M3 prompt

You are an expert mechanical design engineer preparing a design FMEA for an electric scooter mechanical braking subsystem. Use the provided evidence pack and the required DFMEA schema. Generate 12-20 DFMEA rows covering brake lever, cable or hydraulic transmission path, brake caliper, brake pads, disc rotor, mounting hardware, and wheel-level braking response. Each row must include an evidence trace using source IDs when possible. If a row is an engineering inference rather than directly supported, mark it as `engineering_inference:Sxx`. Use the S/O/D anchors and calculate RPN as S x O x D. Do not perform a separate critic or multi-agent review. Output only the normalized CSV rows.

## M4_full prompt

You are executing AUDIT-FMEA, an evidence-grounded multi-agent DFMEA workflow for an electric scooter mechanical braking subsystem. Follow the eight-step protocol: function decomposition, evidence retrieval, failure-mode generation, cause-effect reasoning, risk scoring, critic review, mitigation refinement, and integrity check. Use the provided evidence pack, source IDs, system boundary, DFMEA schema, and S/O/D anchors. The final DFMEA rows must be specific, traceable, mechanically plausible, and suitable for early-stage design review. Do not claim physical braking-performance validation. Output only the normalized final CSV rows after critic review and integrity checking.

