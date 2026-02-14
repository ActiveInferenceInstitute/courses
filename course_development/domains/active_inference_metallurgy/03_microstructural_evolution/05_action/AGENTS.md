# Station: Action (Microstructural Evolution)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Topics**: Action — Grain Growth and Coarsening as Microstructural Action
- **Lab Style**: Image Analysis Lab
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Grain growth and precipitate coarsening are the primary action modalities at the microstructural scale. Normal grain growth is the system's action to reduce total grain boundary energy — large grains consume small grains, simplifying the microstructure and minimizing the free energy associated with boundary area. Ostwald ripening operates on the same principle for precipitates: large particles grow at the expense of small ones, driven by the Gibbs-Thomson effect (curvature-dependent solubility). Abnormal grain growth represents a pathological action where a single grain violates the normal coarsening statistics, analogous to an agent whose action overwhelms the collective.

## Key Mappings

| FEP Concept | Grain Growth/Coarsening Translation |
|-------------|--------------------------------------|
| Action | Grain boundary migration; precipitate growth/dissolution |
| Driving Force | Curvature-driven boundary energy reduction; Gibbs-Thomson capillarity |
| Action Rate | Grain boundary mobility x driving force; coarsening rate constant |
| Normal Action | Normal grain growth following parabolic kinetics (d^2 ~ t) |
| Pathological Action | Abnormal grain growth (single grain dominates the population) |
| Action Constraint | Zener pinning; solute drag; texture-dependent mobility anisotropy |

## Content Guidelines

- Frame the parabolic grain growth law (d^2 - d0^2 = kt) as the kinetics of free energy minimization at the microstructural scale
- Treat Ostwald ripening as competitive inference among precipitates — each particle's solubility depends on its curvature, and the Gibbs-Thomson effect ensures that larger particles are more stable (lower prediction error)
- Connect abnormal grain growth to breakdown of the collective inference assumption — one agent escapes the constraints that govern the population
- Emphasize that the LSW (Lifshitz-Slyozov-Wagner) theory of coarsening provides the kinetic law for how the system's action rate depends on particle size distribution

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
