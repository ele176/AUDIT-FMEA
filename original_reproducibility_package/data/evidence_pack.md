# Compact Evidence Pack v0.1

Purpose:

This compact evidence pack is used only for M3 RAG-LLM and M4 multi-agent DFMEA generation. It condenses the seed corpus into short source-indexed statements. Final manuscript citations still require full metadata verification.

## Source IDs

### S01 - CPSC micromobility safety report

Type: Official U.S. government safety report

Evidence summary:

- E-scooter safety is a substantial public safety issue. The report estimates 380000 e-scooter emergency-department-treated injuries and 206 e-scooter fatalities from 2017 through 2024.
- In CPSC in-depth investigations brake problems were associated with 40 e-scooter incidents.
- Reported brake-related scenarios included brakes not engaging; sporadic engagement; delayed or excessive engagement; and cable attachment problems.

Use:

- Supports safety relevance.
- Supports failure modes involving failure to engage; intermittent engagement; over-aggressive engagement; cable or linkage problems.

### S02 - UK Department for Transport e-scooter construction standards report

Type: Government technical report

Evidence summary:

- E-scooter construction standards compare braking requirements across EN 17128 and national frameworks.
- Braking-device requirements emphasize reliable stopping performance; brake-device presence; and braking performance under defined conditions.
- Standards-based construction guidance is useful for defining system functions and safety expectations.

Use:

- Supports braking subsystem boundary and requirements.
- Supports recommended actions involving design review against relevant e-scooter standards.

### S03 - EN 17128:2020 preview

Type: Standard preview

Evidence summary:

- Defines braking-system terminology for personal light electric vehicles.
- Distinguishes direct and indirect braking systems.
- Defines brake; braking force; braking distance; braking device; and service brake system.

Use:

- Supports terminology and system boundary.
- Supports function decomposition and requirement anchors.

### S04 - El Hassani et al. 2024 LLM-FMEA

Type: Engineering design conference paper

Evidence summary:

- LLMs have been explored for improving FMEA workflows.
- Manual FMEA is time-consuming and prone to omissions or inconsistency.
- LLM outputs still require engineering oversight and structured evaluation.

Use:

- Supports related-work baseline and motivation for structured LLM-assisted FMEA.

### S05 - Knowledge graph-enhanced RAG for FMEA

Type: Journal article, Journal of Industrial Information Integration (2025)

Evidence summary:

- RAG and structured knowledge representations have been proposed for FMEA-related generation and retrieval.
- Retrieval can improve grounding but does not by itself guarantee complete or consistent risk analysis.

Use:

- Supports M3 as a meaningful baseline.
- Supports the need for evidence traceability and critic checks.

### S06 - LLM plus RAG FMEA automation framework

Type: Journal article landing page

Evidence summary:

- Recent work proposes automating FMEA using LLMs and retrieval-augmented generation.
- Such work establishes direct prior art for RAG-based FMEA table generation.

Use:

- Supports novelty boundary.
- Supports comparison with a RAG-LLM baseline.

### S09 - Seven failure points in RAG systems

Type: arXiv preprint

Evidence summary:

- RAG systems can fail through retrieval failures; missing content; wrong context; unsupported generation; or poor answer synthesis.
- Grounding must be paired with validation and traceability checks.

Use:

- Supports critic-agent and integrity-check design.

### S10 - MechAgents

Type: arXiv preprint

Evidence summary:

- Multi-agent LLM collaboration has been explored for mechanics-related problem solving and knowledge integration.
- Agent role separation can support complex engineering reasoning but does not remove the need for validation.

Use:

- Supports multi-agent workflow framing.

### S11 - Agentic LLMs for conceptual systems engineering and design

Type: arXiv / systems engineering design work

Evidence summary:

- Agentic LLM workflows can support conceptual systems engineering and design tasks.
- Such workflows must be evaluated for fidelity and consistency.

Use:

- Supports use of multi-agent decomposition in engineering design review.

## Evidence Use Constraints

1. Evidence source IDs support context and plausibility. They do not prove that a generated DFMEA row is correct.
2. Use `engineering_inference:Sxx` when the row is a plausible inference from a source rather than a directly reported failure.
3. Do not claim physical braking performance validation.
4. If no source supports a row even indirectly mark `unsupported_candidate`.
