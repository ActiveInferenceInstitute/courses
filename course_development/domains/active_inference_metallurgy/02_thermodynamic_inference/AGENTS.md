# Thermodynamic Inference — Agent Guidelines

> **Quick Navigation**: [Unit README](./README.md) | [Course AGENTS](../AGENTS.md)

## Overview

This unit exploits the deepest structural parallel in the entire curriculum: thermodynamic free energy minimization and variational free energy minimization share the same mathematical form. Phase diagrams function as generative models, chemical potentials encode prediction errors, and CALPHAD calculations perform the same computational role as variational inference. Every module should make this isomorphism explicit.

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Lab Style**: Calculation Lab — thermodynamic calculations using CALPHAD tools (Thermo-Calc, PyCalphad), lever rule, and kinetic models
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused with rigorous thermodynamic formalism

## Domain-Specific Active Inference Mappings

| FEP Concept | Thermodynamic Inference Translation |
|-------------|-------------------------------------|
| Generative Model | Phase diagram, CALPHAD database, Gibbs energy surface |
| Prediction Error | Chemical potential difference between phases, supersaturation |
| Free Energy Minimization | Gibbs energy minimization at constant T, P (thermodynamic equilibrium) |
| Variational Inference | CALPHAD optimization: fitting model parameters to minimize deviation from experimental data |
| Policy Selection | Cooling path selection on a CCT/TTT diagram |
| Active Sensing | DSC/DTA measurement — probing the system to resolve phase boundary uncertainty |
| Precision Weighting | Temperature measurement accuracy, compositional resolution of EDS/WDS |
| Model Evidence | Agreement between predicted and observed phase fractions |

## Key Parallels to Emphasize

1. **Gibbs energy surfaces as posterior landscapes**: The Gibbs energy G(T, P, x) defines a landscape over composition-temperature space. Equilibrium corresponds to the minimum — exactly as variational inference seeks the minimum of the variational free energy.
2. **Chemical potential as prediction error**: The difference in chemical potential between phases is the driving force for transformation — formally a prediction error that the system acts to minimize.
3. **CALPHAD as model fitting**: The CALPHAD method fits Gibbs energy parameters to experimental data, structurally identical to updating a generative model to minimize prediction error.
4. **TTT/CCT diagrams as policy spaces**: Each cooling trajectory through a TTT diagram represents a different policy, with the resulting microstructure as the outcome.

Ensure all content adheres to [../resources/notation_table.md](../resources/notation_table.md).
