# Station: Action (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Action — Phase Transformation Kinetics as Thermodynamic Action
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Phase transformations are the actions through which a metallurgical system minimizes its thermodynamic free energy. The nucleation barrier is an action threshold — the system must accumulate sufficient driving force (supercooling or supersaturation) before it can act to form a new phase. Johnson-Mehl-Avrami-Kolmogorov (JMAK) kinetics describe how the transformation fraction evolves as the system progressively acts to replace the metastable parent phase. TTT curves map the timescale of action as a function of temperature, revealing the competition between thermodynamic driving force and atomic mobility.

## Key Mappings

| FEP Concept | Transformation Kinetics Translation |
|-------------|-------------------------------------|
| Action | Phase transformation (nucleation + growth) |
| Action Threshold | Nucleation barrier (critical free energy of formation) |
| Driving Force | Gibbs energy difference between parent and product phases |
| Action Rate | JMAK transformation rate; growth velocity |
| Policy | Transformation pathway (diffusional vs. displacive; continuous vs. discontinuous) |
| Action Outcome | New phase fraction, composition, morphology |

## Content Guidelines

- Frame the classical nucleation barrier as the cost of action — the interfacial energy penalty that must be overcome before the system can reduce its bulk free energy
- Present JMAK kinetics as the temporal dynamics of action: incubation (planning), acceleration (committed action), saturation (task completion)
- Connect TTT diagram nose temperature to the optimal action policy — the temperature that maximizes transformation rate by balancing driving force and diffusivity
- Treat martensitic transformation as a special case of impulsive action — no diffusion, purely displacive, triggered when driving force exceeds a critical threshold

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
