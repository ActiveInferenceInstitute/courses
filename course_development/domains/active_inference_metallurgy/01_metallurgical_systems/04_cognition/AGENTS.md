# Station: Cognition (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Cognition — Lattice Energy and First-Principles Cognition
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

First-principles calculations (DFT, molecular dynamics) are the computational cognition of metallurgy. Density Functional Theory solves for the electronic ground state by minimizing a total energy functional — a direct mathematical parallel to variational free energy minimization. The interatomic potential is the material's internal generative model: given atomic positions, it predicts forces and energies. When the predicted forces differ from the actual forces (prediction error), the system relaxes its atomic positions (perceptual inference) or the modeler updates the potential parameters (model learning).

## Key Mappings

| FEP Concept | First-Principles Translation |
|-------------|----------------------------|
| Generative Model | Interatomic potential; exchange-correlation functional in DFT |
| Variational Free Energy | DFT total energy functional (Kohn-Sham energy) |
| Perceptual Inference | Atomic relaxation to minimize forces (conjugate gradient, BFGS) |
| Prediction Error | Residual force on atoms; deviation between DFT and experimental lattice parameter |
| Model Complexity | Basis set size; k-point mesh density; number of potential parameters |
| Model Selection | Choosing between LDA, GGA, hybrid functionals based on predictive accuracy |

## Content Guidelines

- Draw explicit parallels between the self-consistent field (SCF) cycle in DFT and the perception-action cycle in Active Inference
- Treat the Born-Oppenheimer approximation as a hierarchical separation — electrons infer fast, nuclei infer slow
- Frame potential fitting (EAM, MEAM parameterization) as generative model learning from first-principles training data
- Emphasize that lattice energy minimization is not merely analogous to free energy minimization — it is the same mathematical operation applied to different state spaces

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
