# M1 Prompt Protocol: Template-Only FMEA

Purpose:

Create a baseline DFMEA table using only the predefined system boundary and generic FMEA structure. This condition should not use retrieved evidence or LLM creative expansion beyond the template.

## Inputs Allowed

- System boundary from `dfmea_schema.md`
- Required DFMEA columns
- S/O/D scoring anchors
- General engineering knowledge at a basic level

## Inputs Not Allowed

- Evidence corpus
- Source IDs
- Retrieved document excerpts
- Multi-agent critique

## Procedure

1. Create one row for each included subsystem:
   - Brake lever
   - Cable or hydraulic transmission path
   - Brake caliper
   - Brake pads
   - Disc rotor
   - Mounting hardware
   - Wheel-level braking response
2. Use one representative failure mode per subsystem.
3. Fill all required columns.
4. Do not cite sources.
5. Do not add critic notes.

## Output Requirements

Output a markdown table and a CSV-compatible version with the schema in `dfmea_schema.md`.

Set:

- `method_id = M1`
- `evidence_trace = none`
- `critic_notes = not_applicable`

## Prompt Text

You are preparing a baseline design FMEA for the mechanical braking subsystem of an electric scooter. Use only the system boundary and generic FMEA structure provided. Do not use retrieved evidence or cite sources. Create one representative DFMEA row for each subsystem. Use the provided S/O/D anchors and calculate RPN as S x O x D. Keep the output concise and mechanically plausible.

