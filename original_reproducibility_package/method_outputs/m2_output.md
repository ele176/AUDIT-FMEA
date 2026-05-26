# M2 Single-LLM DFMEA Output

Method: M2 Single-LLM FMEA

Generation rule:

The output simulates a single expert LLM generation using the system boundary and S/O/D anchors only. No evidence corpus, RAG source IDs, or separate critic pass were used.

| item_id | subsystem | function | potential_failure_mode | potential_effect | S | potential_cause | O | current_control | D | RPN | recommended_action |
|---|---|---|---|---|---:|---|---:|---|---:|---:|---|
| M2-001 | Brake lever | Convert hand force to brake input | Lever pivot binds | Delayed brake actuation or release | 6 | Corrosion dirt ingress or poor bearing tolerance | 4 | Assembly inspection | 6 | 144 | Add sealed pivot bushing and corrosion-resistant material |
| M2-002 | Brake lever | Provide ergonomic control | Lever cracks under repeated load | Sudden loss of rider input | 8 | Low material strength or stress concentration | 3 | Static load test | 7 | 168 | Increase section thickness and validate fatigue strength |
| M2-003 | Cable or hydraulic path | Transmit input force | Cable frays near anchor | Gradual loss of braking force | 7 | Sharp bend poor routing or fatigue | 5 | Visual cable inspection | 5 | 175 | Improve cable routing and add fray inspection interval |
| M2-004 | Cable or hydraulic path | Transmit input force | Cable detaches from lever or caliper | Sudden loss of braking | 9 | Incorrect clamp torque or missing retainer | 3 | Assembly torque check | 8 | 216 | Add positive retention feature and poka-yoke assembly |
| M2-005 | Cable or hydraulic path | Maintain hydraulic pressure | Fluid leaks from hose or fitting | Reduced braking force and longer stopping distance | 8 | Seal degradation or loose fitting | 3 | Leak inspection | 7 | 168 | Specify pressure-rated fittings and leak test |
| M2-006 | Brake caliper | Convert force to pad clamping | Caliper piston sticks | Uneven braking or brake drag | 7 | Dirt corrosion or seal swelling | 4 | Maintenance inspection | 6 | 168 | Improve dust sealing and define cleaning procedure |
| M2-007 | Brake caliper | Align pads with rotor | Caliper is misaligned | Uneven pad wear and reduced braking | 6 | Poor assembly tolerance or bent bracket | 5 | Visual alignment check | 5 | 150 | Add alignment fixture and service check |
| M2-008 | Brake pads | Provide friction | Pad material overheats and fades | Braking force drops during repeated braking | 8 | Inadequate pad compound or high heat | 4 | Material qualification | 7 | 224 | Use higher temperature pad material and thermal test |
| M2-009 | Brake pads | Provide friction | Pad contamination | Reduced friction and longer stopping distance | 7 | Oil water or debris exposure | 4 | Visual inspection | 6 | 168 | Add contamination guidance and shielding |
| M2-010 | Disc rotor | Provide friction surface | Rotor excessive wear | Reduced pad contact and braking performance | 7 | Abrasive debris or low hardness | 4 | Thickness inspection | 5 | 140 | Define minimum thickness and material hardness |
| M2-011 | Disc rotor | Maintain flat running surface | Rotor warpage | Pulsing vibration and inconsistent braking | 6 | Heat distortion or impact | 4 | Runout check | 6 | 144 | Improve rotor material and heat management |
| M2-012 | Mounting hardware | Retain caliper and rotor position | Caliper bolt loosens | Caliper shift or loss of braking alignment | 9 | Vibration insufficient torque or no threadlock | 3 | Torque audit | 6 | 162 | Use locking fastener and torque marking |
| M2-013 | Mounting hardware | Maintain structural support | Mounting bracket cracks | Loss of caliper support | 9 | Fatigue overload or poor casting | 2 | Visual inspection | 8 | 144 | Increase bracket safety factor and fatigue test |
| M2-014 | Wheel-level braking response | Produce controllable deceleration | Rear wheel locks too easily | Skid and rider fall | 8 | Aggressive brake bias or poor modulation | 4 | Functional brake test | 7 | 224 | Tune brake leverage and add modulation guidance |
| M2-015 | Wheel-level braking response | Produce controllable deceleration | Insufficient braking at maximum load | Excessive stopping distance | 9 | Undersized brake or low friction material | 3 | Design calculation | 7 | 189 | Verify brake capacity for rated load and slope |

