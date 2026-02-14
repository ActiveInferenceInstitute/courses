# Station: Communication (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Communication — Diffusion as Atomic Communication
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Diffusion is the fundamental communication mechanism in metallurgical systems. Atoms transmit information about local chemical potential through concentration gradients, and neighboring regions update their composition in response. Fick's first law (J = -D dC/dx) is a message-passing equation: the flux J carries information from high-concentration regions to low-concentration regions, reducing the prediction error (concentration gradient) over time. The Kirkendall effect demonstrates that different atomic species communicate at different rates, leading to net mass transport and marker migration — a vivid illustration of asymmetric message passing between coupled agents.

## Key Mappings

| FEP Concept | Diffusion Communication Translation |
|-------------|-------------------------------------|
| Message Passing | Atomic flux carrying compositional information between regions |
| Communication Channel | Diffusion pathway (bulk, grain boundary, surface, pipe) |
| Bandwidth | Diffusivity D (higher D = faster information transfer) |
| Prediction Error | Concentration gradient (dC/dx) driving the diffusion flux |
| Signal Attenuation | Diffusion distance scaling as sqrt(Dt) — information degrades with distance |
| Multi-Agent Communication | Interdiffusion in multicomponent systems; uphill diffusion as counter-intuitive signaling |

## Content Guidelines

- Frame Fick's second law as a prediction error relaxation equation — the system evolves toward uniform composition (zero prediction error)
- Treat grain boundary diffusion as a high-bandwidth communication channel compared to slower bulk diffusion
- Connect the Kirkendall effect to differential message-passing rates between species
- Emphasize that uphill diffusion (spinodal decomposition) occurs when the system's generative model predicts that phase separation reduces free energy — information flows against the naive concentration gradient

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
