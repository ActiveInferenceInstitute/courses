# Metallurgical Systems — Agent Guidelines

> **Quick Navigation**: [Unit README](./README.md) | [Course AGENTS](../AGENTS.md)

## Overview

This unit introduces metallurgical phenomena at the most fundamental level: crystal structures, point and line defects, and the thermodynamic driving forces that govern atomic-scale behavior. Every module in this unit should reinforce the parallel between a crystal lattice maintaining its structural identity and an Active Inference agent maintaining its generative model.

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Lab Style**: Simulation Lab — computational exercises using lattice models, interatomic potentials, and diffusion simulations
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused with explicit mathematical parallels

## Domain-Specific Active Inference Mappings

| FEP Concept | Metallurgical Systems Translation |
|-------------|----------------------------------|
| Markov Blanket | Unit cell boundary, crystal surface, grain boundary interface |
| Generative Model | Crystal structure (FCC, BCC, HCP) as expectation about atomic arrangement |
| Prediction Error | Lattice strain, point defect formation energy, deviation from ideal stoichiometry |
| Free Energy Minimization | Gibbs energy minimization driving phase stability and defect equilibria |
| Active States | Dislocation glide, vacancy migration, solute diffusion |
| Sensory States | Scattering signals (XRD peaks), spectroscopic signatures (EDS, XPS) |
| Precision | Crystallographic resolution, measurement signal-to-noise ratio |

## Key Parallels to Emphasize

1. **Phase transitions as state transitions**: A crystal transforming from BCC to FCC is formally analogous to an agent updating its generative model in response to overwhelming prediction error (supercooling as accumulated surprise).
2. **Thermodynamic free energy and variational free energy**: Gibbs free energy G = H - TS shares deep structural parallels with variational free energy F = E_q[log q(x) - log p(x,y)]. Both are minimized by the system's dynamics.
3. **Defects as prediction errors**: Vacancies, interstitials, and dislocations represent deviations from the ideal crystal model — the material's own "prediction errors" about its perfect lattice.
4. **Diffusion as inference**: Fick's laws describe how concentration gradients (prediction errors) are resolved through atomic migration (active inference).

Ensure all content adheres to [../resources/notation_table.md](../resources/notation_table.md).
