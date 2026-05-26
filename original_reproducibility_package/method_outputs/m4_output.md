# M4 Evidence-Grounded Multi-Agent DFMEA Output

Method: M4 Proposed evidence-grounded multi-agent FMEA

Generation rule:

This output follows the eight-step multi-agent protocol: function decomposition; evidence retrieval; failure-mode generation; cause-effect reasoning; risk scoring; critic review; mitigation refinement; and integrity check.

## 1. Function-Component Map

| subsystem | primary function | interface | key requirement anchor |
|---|---|---|---|
| Brake lever | Convert rider hand input into controlled braking command | Rider hand; cable or hydraulic path | S02;S03 |
| Cable or hydraulic path | Transmit command force or pressure from lever to caliper | Lever; caliper | S01;S02;S03 |
| Brake caliper | Convert transmitted input into pad clamping force | Cable or hydraulic path; pads; mount | S02;S03 |
| Brake pads | Generate controlled friction against rotor | Caliper; rotor | S02;S03 |
| Disc rotor | Provide stable friction surface and heat capacity | Pads; wheel hub | S02;S03 |
| Mounting hardware | Preserve alignment and structural retention of brake components | Frame or fork; caliper; wheel assembly | S01;S02 |
| Wheel-level braking response | Convert brake torque into predictable deceleration | Tire-road interface; rider control | S01;S02 |

## 2. Evidence Coverage Table

| evidence item | coverage |
|---|---|
| S01 CPSC report | Safety context; brake problems; no engagement; sporadic engagement; delayed or excessive engagement; cable attachment problems |
| S02 UK DfT standards report | Braking requirements; standards comparison; construction safety expectations |
| S03 EN 17128 preview | Braking-system terminology and component boundary |
| S04 LLM-FMEA prior work | Motivation for structured LLM-assisted FMEA |
| S05 KG-RAG FMEA | RAG baseline and grounding comparison |
| S06 LLM+RAG FMEA framework | Direct prior art; novelty boundary |
| S09 RAG failure points | Need for critic review and traceability checks |
| S10 MechAgents | Multi-agent engineering reasoning context |
| S11 Agentic systems engineering | Agentic design workflow support and fidelity caution |

Coverage gaps:

- Public evidence supports braking hazards and design requirements but does not provide physical test data for this specific design.
- Several row-level mechanisms are engineering inferences grounded in braking-system logic rather than directly observed incidents.

## 3. Final Normalized DFMEA Table

| item_id | subsystem | function | evidence_trace | potential_failure_mode | potential_effect | S | potential_cause | O | current_control | D | RPN | recommended_action | critic_notes | status |
|---|---|---|---|---|---|---:|---|---:|---|---:|---:|---|---|---|
| M4-001 | Brake lever | Convert rider input into braking command | engineering_inference:S02;S03 | Lever pivot binds and prevents smooth actuation | Delayed braking command or delayed release | 6 | Dirt ingress corrosion poor pivot tolerance | 4 | Assembly inspection and service check | 6 | 144 | Use sealed bushing corrosion-resistant pivot and lever return test | Specific and plausible | keep |
| M4-002 | Brake lever | Maintain structural integrity under rider input | engineering_inference:S02 | Lever blade cracks near pivot | Sudden loss or reduction of rider brake input | 9 | Stress concentration low material strength impact damage | 2 | Static load test and visual inspection | 7 | 126 | Add fatigue assessment radius improvement and material specification | High severity but occurrence low; keep with S explanation | keep |
| M4-003 | Brake lever | Provide controllable modulation | engineering_inference:S02 | Lever ratio produces excessive mechanical advantage | Over-aggressive braking and wheel lock tendency | 8 | Poor leverage design inadequate modulation evaluation | 3 | Functional brake feel test | 7 | 168 | Tune lever ratio and validate modulation with defined load cases | Distinct from wheel-level lock because cause is lever design | keep |
| M4-004 | Cable or hydraulic path | Transmit lever force to caliper | S01;engineering_inference:S02 | Cable anchor slips or detaches | Sudden severe loss of braking force | 9 | Insufficient clamp torque missing retainer poor assembly | 3 | Torque check and functional brake test | 8 | 216 | Add positive retention feature torque marking and assembly poka-yoke | CPSC cable attachment anchor supports inclusion | keep |
| M4-005 | Cable or hydraulic path | Transmit force consistently | S01;engineering_inference:S02 | Cable frays or stretches at routing bend | Progressive reduction in braking force | 7 | Sharp bend fatigue abrasive housing poor routing | 5 | Visual cable inspection and adjustment check | 5 | 175 | Increase bend radius add liner and define replacement interval | Keep; not duplicate of detachment because progression differs | keep |
| M4-006 | Cable or hydraulic path | Maintain continuous force path | S01;engineering_inference:S03 | Intermittent cable or linkage movement | Sporadic brake engagement and unpredictable deceleration | 8 | Kinked cable sticking linkage housing contamination | 3 | Functional brake check | 8 | 192 | Add smooth-routing requirement and full-stroke return test | Directly aligned with sporadic engagement evidence | keep |
| M4-007 | Cable or hydraulic path | Maintain hydraulic pressure if hydraulic brake is used | engineering_inference:S02 | Hydraulic leak or air ingress reduces pressure | Reduced braking force and increased stopping distance | 8 | Seal degradation loose fitting poor bleeding | 3 | Leak inspection and bleed procedure | 7 | 168 | Specify pressure-rated fittings and production leak test | Conditional on hydraulic variant; mark as applicable when hydraulic | keep |
| M4-008 | Brake caliper | Convert input into pad clamping force | engineering_inference:S02;S03 | Caliper piston or slide sticks | Brake drag or delayed clamping response | 7 | Corrosion debris seal swelling poor lubrication | 4 | Maintenance inspection | 6 | 168 | Improve dust sealing specify compatible lubricant and cleaning guidance | Specific mechanical mechanism | keep |
| M4-009 | Brake caliper | Maintain pad-rotor alignment | engineering_inference:S02 | Caliper misalignment relative to rotor | Uneven pad wear noise and reduced braking consistency | 6 | Poor bracket tolerance loose mounting bent support | 4 | Alignment check | 5 | 120 | Add alignment fixture torque sequence and service tolerance | Lower severity justified; not primary loss of braking | keep |
| M4-010 | Brake pads | Generate friction against rotor | engineering_inference:S02;S03 | Pad wear below service limit | Longer stopping distance and reduced braking margin | 8 | Normal wear abrasive debris delayed replacement | 5 | Visual pad thickness inspection | 4 | 160 | Add wear indicator minimum thickness marking and maintenance interval | Important high-severity wear path | keep |
| M4-011 | Brake pads | Maintain stable friction coefficient | engineering_inference:S02 | Pad contamination by oil water or debris | Reduced friction and inconsistent braking | 7 | Environmental exposure cleaning residue road debris | 4 | Visual inspection | 6 | 168 | Add contamination warning shielding and replacement instruction | Evidence indirect but engineering plausible | keep |
| M4-012 | Brake pads | Maintain braking under thermal load | engineering_inference:S02 | Pad fade during repeated braking | Braking force decreases during repeated stops or slope descent | 8 | Inadequate compound heat buildup insufficient rotor heat capacity | 4 | Material qualification | 7 | 224 | Define thermal fade test and use higher-temperature pad compound | High-risk item; keep | keep |
| M4-013 | Disc rotor | Provide stable friction surface | engineering_inference:S02;S03 | Rotor warps or has excessive runout | Pulsation vibration and uneven braking | 6 | Heat distortion impact insufficient stiffness | 4 | Runout inspection | 6 | 144 | Specify runout limit rotor material and heat treatment control | Specific and measurable | keep |
| M4-014 | Disc rotor | Maintain thickness and heat capacity | engineering_inference:S02;S03 | Rotor wears below minimum thickness | Reduced heat capacity and degraded braking performance | 7 | Abrasive debris low hardness delayed replacement | 3 | Thickness measurement | 5 | 105 | Mark minimum thickness and include service gauge instruction | Keep; different from warpage | keep |
| M4-015 | Mounting hardware | Retain caliper and brake components | S01;engineering_inference:S02 | Caliper bolt loosens or retaining fastener backs out | Caliper shift misalignment or severe braking loss | 9 | Vibration insufficient torque no locking feature | 3 | Torque audit | 7 | 189 | Use locking fastener torque stripe and assembly verification | High-risk due to retention loss | keep |
| M4-016 | Mounting hardware | Preserve structural support under braking load | engineering_inference:S02 | Caliper bracket cracks under fatigue | Caliper displacement and reduced braking control | 9 | Fatigue overload casting defect sharp corner | 2 | Visual inspection | 8 | 144 | Increase fillet radius safety factor and fatigue analysis | High D because hidden crack may progress | keep |
| M4-017 | Wheel-level braking response | Produce predictable deceleration | S01;engineering_inference:S02 | Brake does not engage when commanded | Excessive stopping distance and collision risk | 10 | Cable detachment hydraulic leak seized linkage or severe pad failure | 2 | Functional brake test | 8 | 160 | Add pre-ride check procedure and design-level fail-safe review | General effect row kept as system-level hazard aggregator | keep |
| M4-018 | Wheel-level braking response | Produce controllable deceleration | S01;engineering_inference:S02 | Brake engages too aggressively or unexpectedly | Wheel lock skid and rider fall | 8 | Poor modulation sticking mechanism excessive leverage | 3 | Functional brake response test | 8 | 192 | Define modulation acceptance criteria and adjust leverage/friction pairing | Directly tied to excessive engagement scenario | keep |

## 4. Critic Review Summary

Findings:

1. Generic "brake failure" rows were rejected during generation and replaced with component-specific mechanisms.
2. Cable detachment; cable fraying; and intermittent cable motion were kept as separate rows because they differ in failure progression and effect timing.
3. Hydraulic leak was kept with conditional wording because not all e-scooter brakes are hydraulic.
4. System-level no-engagement row was retained as a hazard aggregator because it maps to CPSC evidence and high-level DFMEA reasoning.
5. No row claims physical validation or certified compliance.

Duplicate check:

- No intentional duplicate rows retained.

Unsupported candidate check:

- No row left as `unsupported_candidate`.
- Several rows are marked as `engineering_inference` to avoid overstating source support.

## 5. Integrity Checklist

| Check | Result |
|---|---|
| Every row has source trace or engineering inference | PASS |
| Every RPN equals S x O x D | PASS |
| Every subsystem in boundary is covered | PASS |
| Every high-severity row has mitigation | PASS |
| No physical braking performance validation claimed | PASS |
| Critic notes present for every M4 row | PASS |

