# Station: Perception (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Perception — In-Situ Monitoring and Non-Destructive Testing
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

In-situ monitoring and non-destructive testing (NDT) are the perceptual systems of manufacturing process control. In-situ XRD during heat treatment reveals real-time phase transformation progress. Infrared thermal imaging during welding or AM builds maps the temperature field. Ultrasonic testing after processing detects internal defects without destroying the part. Each technique is an active sensing modality: the engineer selects the inspection method, parameters, and sampling strategy to maximize information about the internal material state while minimizing inspection cost and time. NDT is inherently Bayesian — probability of detection (POD) curves quantify the reliability of perception as a function of defect size and inspection parameters.

## Key Mappings

| FEP Concept | In-Situ/NDT Perception Translation |
|-------------|-------------------------------------|
| Sensory Data | In-situ XRD pattern, thermal image, ultrasonic A-scan, eddy current signal |
| Generative Model | Expected signal for a defect-free part; physics of wave propagation and scattering |
| Prediction Error | Anomalous signal indicating defect, phase deviation, or dimensional error |
| Precision | Probability of detection (POD); signal-to-noise ratio; inspection resolution |
| Active Sensing | Choosing inspection frequency, probe position, scan pattern to resolve defect uncertainty |
| Multi-Modal Perception | Combining UT + radiography + eddy current for comprehensive defect characterization |

## Content Guidelines

- Frame probability of detection (POD) curves as the precision profile of an NDT perceptual system — they quantify how sensory reliability varies with defect size
- Treat in-situ monitoring during AM as real-time perception that enables closed-loop process control — defect detection during the build enables corrective action
- Connect melt pool monitoring (thermal imaging, photodiode signals) to active perception of the solidification process in real time
- Emphasize that NDT reliability depends on the inspector's generative model — experience and training improve the prior expectations that guide signal interpretation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
