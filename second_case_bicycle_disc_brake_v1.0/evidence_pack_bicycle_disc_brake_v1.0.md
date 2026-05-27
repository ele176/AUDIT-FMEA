# Second Case Evidence Pack v1.0

Case: bicycle/e-bike mechanical disc brake subsystem

Date: 2026-05-27

Skill route: deep-research -> academic-paper -> academic-pipeline -> nature-data

## Scope

This second case is a transfer-case extension for AUDIT-FMEA. It is designed to test whether the same evidence-labeled multi-agent DFMEA workflow can be applied to a related but distinct mechanical braking subsystem.

Included boundary:

- brake lever and lever-caliper compatibility
- mechanical cable and cable-fixing interface
- mechanical disc brake caliper and actuator arm
- caliper mounting hardware and frame/fork mounting interface
- brake pads and pad retention
- disc brake rotor and pad-rotor clearance
- wheel-level braking response associated with the mechanical brake
- assembly and service checks directly tied to brake function

Excluded boundary:

- motor control and regenerative braking
- battery and electrical safety
- frame fracture outside the brake mounting interface
- rider behavior modeling beyond brake-response effects
- physical stopping-distance testing
- safety certification or regulatory compliance determination

## Source IDs

### B1. CPSC Lectric e-bike mechanical disc brake caliper recall

URL: https://www.cpsc.gov/Recalls/2023/Lectric-Ebikes-Recalls-Disc-Brake-Calipers-Sold-on-Lectric-E-Bicycles-Due-to-Crash-and-Injury-Hazards-Recall-Alert

Source type: public safety recall.

Relevant evidence:

- Mechanical disc brake calipers on affected Lectric e-bike models could fail.
- The hazard is loss of control with crash and injury risk.
- The recall covered about 45,000 units.
- The firm had four reports of loss of braking power including two injuries.

Use in DFMEA:

- caliper failure
- loss of braking power
- loss-of-control effect
- high-severity wheel-level braking consequence

### B2. CPSC Tektro/TRP Spyre mechanical disc brake caliper recall

URL: https://www.cpsc.gov/Recalls/2014/Tektro-USA-and-TRP-Recall-Bicycle-Mechanical-Disc-Brake-Calipers

Source type: public safety recall.

Relevant evidence:

- Spyre and Spyre SLC dual-piston mechanical disc brake calipers were recalled.
- The brake cable actuator arm could over-rotate and dislocate parts.
- The resulting caliper failure could cause lack of brakes and loss of control.
- About 2,000 units were affected and one caliper-failure report was received.

Use in DFMEA:

- actuator-arm over-rotation
- dislocation of caliper parts
- loss of brake function
- mechanism-specific caliper failure row

### B3. 16 CFR 1512.5 bicycle braking-system requirements

URL: https://www.law.cornell.edu/cfr/text/16/1512.5

Source type: public regulatory text mirror for 16 CFR 1512.5.

Relevant evidence:

- Handbrakes are subject to loading and rocking tests.
- Brake components should show no visible fractures failures clamp movement or misalignment during the specified test context.
- A handbrake-only bicycle must meet a stopping-distance requirement.
- Brake assemblies should be securely attached with fasteners and locking devices.
- The cable anchor bolt should not cut cable strands.
- Brake pads and holders should be secure and retained under loading.

Use in DFMEA:

- attachment and locking-device rows
- cable-anchor damage row
- pad-retention row
- stopping-distance and loss-of-braking effects

### B4. Shimano DM-BR0007-04 mechanical disc brake dealer manual

URL: https://si.shimano.com/en/pdfs/dm/BR0007/DM-BR0007-04-ENG.pdf

Source type: manufacturer technical manual for BR-TX805 and BR-M375 mechanical disc brakes.

Relevant evidence:

- The manual is intended primarily for professional mechanics.
- Incorrect installation or adjustment can create serious injury risk.
- Oil or grease on the rotor or pads can prevent correct brake operation.
- Pads worn to the usable limit require clearance adjustment or replacement.
- Cable rust fraying and cracks can prevent correct brake operation.
- Excessive front brake force can lock the wheel and cause a fall.
- Wet conditions increase required braking distance and skid risk.
- Inner cable protrusion should be 20 mm or less because excess cable may catch in the rotor and lock the wheel.
- Lever mode and lever-caliper compatibility affect braking force.
- Caliper mounting bosses outside standard dimensions can cause rotor-caliper contact.
- Caliper fixing bolts and cable fixing bolts have specified torque ranges.
- Snap rings are used to prevent caliper bolts from coming loose.
- Pad-rotor clearances should be adjusted equally and within the stated range.
- Pads can be used while thickness is at least 0.5 mm.

Use in DFMEA:

- lever compatibility
- cable protrusion
- cable fixing
- caliper mounting
- snap ring retention
- pad clearance
- pad wear
- pad/rotor contamination
- rotor crack deformation and wear
- wet-road braking response

## Evidence-use rules for this case

1. A row can cite a source ID only when the failure mode or effect is directly grounded in the source or a close engineering translation of it.
2. A row that extends from subsystem function or mechanical reasoning must include an `engineering_inference:` tag.
3. A source ID is not a correctness certificate. It is a trace marker for reviewer inspection.
4. This case supports a structural transfer claim only. It does not validate S/O/D values or certify bicycle/e-bike braking safety.

