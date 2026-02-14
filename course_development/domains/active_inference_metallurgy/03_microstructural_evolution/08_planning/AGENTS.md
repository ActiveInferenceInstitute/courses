# Station: Planning (Microstructural Evolution)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Topics**: Planning — Microstructure Engineering and Design
- **Lab Style**: Image Analysis Lab
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Microstructure engineering is planning at the mesoscale — designing thermo-mechanical processing routes to achieve a target microstructure that delivers specified mechanical properties. The metallurgist evaluates counterfactual processing paths: "If I anneal at this temperature for this duration, what grain size will I achieve?" This requires a generative model linking process parameters to microstructural outcomes (grain size equations, precipitation kinetics, recrystallization maps). The planning problem involves sequential decisions: deformation temperature, reduction per pass, inter-pass time, final annealing schedule, and aging treatment, each of which constrains the subsequent options.

## Key Mappings

| FEP Concept | Microstructure Design Translation |
|-------------|----------------------------------|
| Planning | Designing thermo-mechanical processing route to achieve target microstructure |
| Policy | Processing schedule: temperatures, times, deformation amounts, cooling rates |
| Expected Free Energy | Predicted property outcome + uncertainty about microstructural response |
| Generative Model | Process-structure-property linkage (Hall-Petch, Orowan, precipitation models) |
| Sequential Planning | Multi-pass rolling schedule; multi-step heat treatment |
| Constraint | Equipment limits, alloy composition, cost targets |

## Content Guidelines

- Frame the Hall-Petch relationship as the key linkage in the planning chain: grain size controls yield strength, and the processing route controls grain size
- Treat precipitation hardening schedule design (solutionize, quench, age) as a multi-step policy where timing and temperature at each stage are critical planning variables
- Connect thermo-mechanical controlled processing (TMCP) to process-structure planning — deformation in the non-recrystallization regime produces pancaked austenite that transforms to fine ferrite
- Emphasize that inverse microstructure design (specifying target properties and computing required processing) is the planning problem solved backward — from desired outcome to required policy

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
