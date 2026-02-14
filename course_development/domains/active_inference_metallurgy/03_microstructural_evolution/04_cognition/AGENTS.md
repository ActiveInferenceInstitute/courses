# Station: Cognition (Microstructural Evolution)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Topics**: Cognition — Microstructure Prediction and Computational Modeling
- **Lab Style**: Image Analysis Lab
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Computational microstructure modeling is the cognitive capacity that allows the metallurgist to predict microstructural evolution without performing physical experiments. Phase-field models encode a generative model of interface dynamics — they simulate how grain boundaries, precipitate interfaces, and phase fronts evolve by minimizing a total free energy functional. Monte Carlo simulations of grain growth implement stochastic inference over local energy configurations. Cellular automata models of recrystallization apply local rules that capture the inference logic of individual grains deciding whether to be consumed by a growing neighbor.

## Key Mappings

| FEP Concept | Computational Modeling Translation |
|-------------|-----------------------------------|
| Generative Model | Phase-field free energy functional; Monte Carlo Hamiltonian; JMAK kinetic model |
| Cognition | Running a simulation to predict microstructural outcome given processing inputs |
| Variational Inference | Phase-field evolution minimizing the Cahn-Hilliard or Allen-Cahn free energy |
| Prediction | Simulated grain size distribution, precipitate morphology, recrystallization fraction |
| Prediction Error | Deviation between simulated and experimentally observed microstructure |
| Model Comparison | Evaluating phase-field vs. Monte Carlo vs. cellular automata for a given problem |

## Content Guidelines

- Frame the phase-field order parameter as encoding the system's belief about local phase identity (0 = matrix, 1 = precipitate, continuous values = interface uncertainty)
- Connect the Cahn-Hilliard equation to free energy minimization with a diffusion constraint — the system infers its equilibrium composition profile subject to mass conservation
- Treat Monte Carlo grain growth as a stochastic sampling algorithm that explores the space of possible microstructural configurations
- Emphasize that model validation against experimental micrographs is the prediction error assessment step that drives model refinement

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
