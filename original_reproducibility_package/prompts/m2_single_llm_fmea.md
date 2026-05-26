# M2 Prompt Protocol: Single-LLM FMEA

Purpose:

Generate a DFMEA table using a single LLM call with the system boundary and scoring anchors, but without retrieved evidence or agent critique.

## Inputs Allowed

- System boundary from `dfmea_schema.md`
- Required DFMEA columns
- S/O/D scoring anchors
- General model knowledge

## Inputs Not Allowed

- Evidence corpus excerpts
- Source IDs
- RAG retrieval
- Multi-agent role separation
- Critic review

## Procedure

1. Generate 12-20 plausible DFMEA rows.
2. Cover all included subsystems.
3. Provide S/O/D/RPN values.
4. Provide recommended actions.
5. Do not cite source IDs.
6. Do not self-critique after generation.

## Output Requirements

Set:

- `method_id = M2`
- `evidence_trace = none`
- `critic_notes = not_applicable`

## Prompt Text

You are an expert mechanical design engineer preparing a design FMEA for an electric scooter mechanical braking subsystem. The included components are brake lever, cable or hydraulic transmission path, brake caliper, brake pads, disc rotor, mounting hardware, and wheel-level braking response. Generate 12-20 DFMEA rows using the required schema. Use the provided S/O/D anchors and calculate RPN as S x O x D. Do not cite sources, retrieve documents, or perform a separate critique. Make the entries specific enough to support design review.

