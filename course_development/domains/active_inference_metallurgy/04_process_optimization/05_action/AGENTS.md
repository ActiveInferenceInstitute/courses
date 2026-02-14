# Station: Action (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Action — Heat Treatment and Quenching as Process Action
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Heat treatment schedules are the action policies of metallurgical process optimization. Austenitizing temperature, hold time, quench medium, and tempering conditions form a multi-dimensional policy vector that the process engineer selects to achieve target mechanical properties. Each step is an action that changes the material's internal state: austenitizing dissolves carbides and homogenizes the austenite (resetting the generative model), quenching freezes the high-temperature state (preventing the system from reaching its thermodynamic preferred state), and tempering partially relaxes the quenched state toward equilibrium (controlled prediction error reduction). The quench severity (H-value) determines how aggressively the process forces the material away from equilibrium.

## Key Mappings

| FEP Concept | Heat Treatment Action Translation |
|-------------|-----------------------------------|
| Action Policy | Heat treatment schedule (temperatures, times, cooling rates) |
| Action Execution | Furnace heating, quench immersion, tempering hold |
| Action Outcome | Resulting microstructure (martensite, bainite, tempered martensite) and properties |
| Action Intensity | Quench severity (H-value); cooling rate; heating rate |
| Policy Constraint | Equipment capability, part geometry (ruling section), distortion limits |
| Sequential Action | Multi-step heat treatment: austenitize -> quench -> temper -> stress relieve |

## Content Guidelines

- Frame quenching as the most aggressive process action — forcing the material into a highly non-equilibrium state (martensite) by preventing the diffusion-controlled transformations that would minimize thermodynamic free energy
- Treat tempering as controlled relaxation: allowing the quenched material to partially reduce its prediction error by precipitating fine carbides and recovering dislocations
- Connect quench severity selection to the trade-off between hardness (more aggressive quench) and distortion/cracking risk (gentler quench)
- Emphasize that aging treatments in precipitation-hardened alloys are time-controlled actions where the material progressively forms strengthening precipitates — overaging occurs when the action continues past the optimal duration

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
