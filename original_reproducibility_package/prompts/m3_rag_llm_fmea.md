# M3 Prompt Protocol: RAG-LLM FMEA

Purpose:

Generate a DFMEA table using the evidence corpus as retrieval context in a single LLM workflow, without multi-agent decomposition or critic review.

## Inputs Allowed

- System boundary from `dfmea_schema.md`
- Required DFMEA columns
- S/O/D scoring anchors
- Evidence corpus excerpts and source IDs

## Inputs Not Allowed

- Multi-agent role separation
- Separate critic review
- Iterative adversarial revision

## Evidence Pack

Use a compact evidence pack extracted from `evidence_corpus.md`. Each evidence item should include:

- Source ID
- 1-3 sentence evidence summary
- Relevance to braking system, FMEA, RAG, or agentic workflow

## Procedure

1. Read the evidence pack.
2. Generate 12-20 DFMEA rows.
3. Cover all included subsystems.
4. Link each row to at least one source ID when possible.
5. Mark engineering inferences explicitly as `engineering_inference:Sxx`.
6. Do not run a separate critic pass.

## Output Requirements

Set:

- `method_id = M3`
- `critic_notes = not_applicable`

Rows with no evidence support should use:

- `evidence_trace = unsupported_candidate`

## Prompt Text

You are an expert mechanical design engineer preparing a design FMEA for an electric scooter mechanical braking subsystem. Use the provided evidence pack and the required DFMEA schema. Generate 12-20 DFMEA rows covering brake lever, cable or hydraulic transmission path, brake caliper, brake pads, disc rotor, mounting hardware, and wheel-level braking response. Each row must include an evidence trace using source IDs when possible. If a row is an engineering inference rather than directly supported, mark it as `engineering_inference:Sxx`. Use the S/O/D anchors and calculate RPN as S x O x D. Do not perform a separate critic or multi-agent review.

