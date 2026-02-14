# Station: Systems (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Systems — Phase Diagrams as Generative Models
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

A phase diagram is a generative model in the most literal sense: given inputs (temperature, pressure, composition), it generates predictions about the equilibrium phases, their compositions, and their relative amounts. The lever rule performs inference — computing the posterior phase fractions given the global composition and the phase boundary compositions. Tie lines encode the constraint that chemical potentials must be equal across coexisting phases, which is the system-level condition for zero prediction error. The entire CALPHAD framework is a machinery for building, refining, and querying thermodynamic generative models.

## Key Mappings

| FEP Concept | Phase Diagram Translation |
|-------------|--------------------------|
| Generative Model | Binary/ternary phase diagram; Gibbs energy surface |
| System Boundary | Phase field boundary on the diagram; miscibility gap |
| Inference | Lever rule calculation; common tangent construction |
| Prediction | Expected phases and compositions at given T and x |
| Model Parameters | Interaction parameters (L0, L1, ...) in Redlich-Kister polynomial |
| Nested Systems | Binary within ternary within multicomponent diagram hierarchy |

## Content Guidelines

- Present the common tangent construction as a graphical algorithm for free energy minimization — finding the composition pair that minimizes the total Gibbs energy
- Emphasize that invariant reactions (eutectic, peritectic, eutectoid) are critical points where the system's generative model predicts a qualitative phase change
- Frame the phase rule (F = C - P + 2) as a constraint on the system's degrees of freedom — the dimensionality of the inference problem
- Connect metastable extensions of phase boundaries to the system's approximate inference when kinetic constraints prevent reaching the global free energy minimum

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
