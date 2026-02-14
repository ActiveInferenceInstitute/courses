# Station: Cognition (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Cognition — Phase Stability Computation and CALPHAD Cognition
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

CALPHAD (CALculation of PHAse Diagrams) is the cognitive engine of thermodynamic inference. The CALPHAD method constructs Gibbs energy functions for each phase, parameterized by temperature and composition, then minimizes the total system Gibbs energy to predict equilibrium. This is computationally identical to variational inference: the Gibbs energy function is the generative model, the Redlich-Kister interaction parameters are the model parameters, and the equilibrium calculation finds the state that minimizes the free energy functional. Tools like Thermo-Calc and PyCalphad are the computational substrates for this cognitive process.

## Key Mappings

| FEP Concept | CALPHAD Cognition Translation |
|-------------|------------------------------|
| Generative Model | Gibbs energy functions G(T, P, x) for each phase |
| Model Parameters | Redlich-Kister interaction parameters, end-member energies |
| Variational Inference | Gibbs energy minimization at fixed T, P to find equilibrium phase fractions |
| Cognition | Scheil solidification simulation, property diagram calculation |
| Internal Model | Sublattice model (compound energy formalism) encoding crystallographic site occupancy |
| Prediction | Equilibrium phase fractions, solidus/liquidus temperatures, driving forces |

## Content Guidelines

- Frame the Gibbs energy minimizer as performing gradient descent on the thermodynamic free energy landscape — the same optimization that variational inference performs on the variational free energy
- Present Scheil solidification as a sequential inference process — each temperature step updates the phase fractions given the current liquid composition
- Treat the compound energy formalism as a structured generative model that respects crystallographic constraints (sublattice occupancy)
- Connect driving force calculations to prediction error quantification — the driving force for a phase is its distance from the free energy minimum

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
