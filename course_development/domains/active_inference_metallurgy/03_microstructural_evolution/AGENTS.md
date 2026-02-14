# Microstructural Evolution — Agent Guidelines

> **Quick Navigation**: [Unit README](./README.md) | [Course AGENTS](../AGENTS.md)

## Overview

This unit treats the microstructure as a living inference system. Grain boundaries define Markov blankets at the mesoscale. Nucleation events are Bayesian model selection — the material "deciding" whether a new phase is warranted by the thermodynamic evidence. Grain growth, coarsening, and precipitation are all processes by which the microstructure updates its internal states to minimize free energy. Characterization techniques (microscopy, EBSD, synchrotron tomography) are the sensory modalities through which the metallurgist perceives microstructural states.

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Lab Style**: Image Analysis Lab — micrograph interpretation, EBSD data processing, stereological measurement, and phase-field visualization
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused with emphasis on visual and spatial reasoning

## Domain-Specific Active Inference Mappings

| FEP Concept | Microstructural Evolution Translation |
|-------------|--------------------------------------|
| Markov Blanket | Grain boundary, phase interface, precipitate-matrix interface |
| Generative Model | Ideal microstructure model (equilibrium grain size, expected phase fractions) |
| Prediction Error | Deviation from equilibrium grain size distribution, unexpected phase morphology |
| Model Selection | Nucleation as Bayesian decision — does the evidence support forming a new phase? |
| Free Energy Minimization | Grain boundary area reduction (normal grain growth), Ostwald ripening |
| Active Sensing | Choosing microscopy mode, magnification, and sample preparation to resolve uncertainty |
| Hierarchical Models | Nested scales: precipitate < grain < colony < component |
| Precision | EBSD angular resolution, TEM spatial resolution, stereological sampling adequacy |

## Key Parallels to Emphasize

1. **Nucleation as Bayesian model comparison**: The classical nucleation barrier represents the evidence threshold — only when the thermodynamic driving force (model evidence) exceeds the interfacial energy penalty (model complexity) does the new phase nucleate.
2. **Grain growth as free energy minimization**: Normal grain growth reduces total grain boundary energy, directly analogous to a system minimizing its variational free energy by simplifying its internal structure.
3. **EBSD as active perception**: Choosing scan parameters (step size, accelerating voltage, tilt) is active sensing — the microscopist optimizing measurement precision to resolve microstructural uncertainty.
4. **Microstructure as encoded history**: The final microstructure is a compressed record of the thermal and mechanical history — a posterior distribution over all the processing the material has experienced.

Ensure all content adheres to [../resources/notation_table.md](../resources/notation_table.md).
