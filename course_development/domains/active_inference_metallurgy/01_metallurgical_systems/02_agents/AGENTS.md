# Station: Agents (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Agents — Atoms and Defects as Agents
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Point defects and line defects are the agents of metallurgical change. A vacancy is an agent that migrates through the lattice to minimize the system's configurational free energy. A dislocation is an agent that glides along slip planes under applied stress, executing the material's action policy for plastic deformation. Solute atoms are inference agents that partition between phases to equalize chemical potentials — they are literally performing free energy minimization as they diffuse toward equilibrium positions.

## Key Mappings

| FEP Concept | Defect Agent Translation |
|-------------|-------------------------|
| Agent | Vacancy, dislocation, solute atom, interstitial |
| Markov Blanket | Local strain field surrounding the defect (its zone of influence) |
| Preferred State | Equilibrium defect concentration (Arrhenius); equilibrium solute partitioning |
| Prediction Error | Excess chemical potential driving defect migration |
| Action | Vacancy jump, dislocation glide, solute diffusion hop |
| Policy | Preferred migration path (e.g., pipe diffusion along dislocations vs. bulk diffusion) |

## Content Guidelines

- Distinguish between thermally activated agents (vacancies, diffusing solutes) and mechanically driven agents (dislocations under stress)
- Emphasize the Arrhenius relationship for vacancy concentration as a Boltzmann-weighted belief distribution
- Treat dislocation networks as multi-agent systems with collective emergent behavior (work hardening)
- Connect Peierls-Nabarro stress to the action threshold — the minimum prediction error required to trigger dislocation motion

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
