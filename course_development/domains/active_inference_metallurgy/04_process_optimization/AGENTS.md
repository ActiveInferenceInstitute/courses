# Process Optimization — Agent Guidelines

> **Quick Navigation**: [Unit README](./README.md) | [Course AGENTS](../AGENTS.md)

## Overview

This unit brings Active Inference to the factory floor. Manufacturing processes — furnaces, rolling mills, additive manufacturing systems — are bounded inference systems with sensors, controllers, and actuators that form agent architectures. Digital twins serve as explicit generative models. Statistical process control implements prediction error monitoring. Bayesian optimization and reinforcement learning close the loop from sensing to action. The metallurgist operating a process is an Active Inference agent embedded within a larger industrial inference hierarchy.

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Lab Style**: Digital Twin Lab — process simulation, sensor data analysis, control algorithm design, and Bayesian optimization exercises
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused with practical industrial emphasis

## Domain-Specific Active Inference Mappings

| FEP Concept | Process Optimization Translation |
|-------------|----------------------------------|
| Markov Blanket | Process boundary (furnace walls, build chamber, rolling stand) |
| Generative Model | Digital twin, FEA/CFD simulation, surrogate model |
| Prediction Error | Deviation between predicted and measured process output (temperature, hardness, dimensions) |
| Active Inference | Closed-loop process control: sense deviation, update model, adjust parameters |
| Policy Selection | Heat treatment schedule, cooling path, deposition strategy |
| Precision Weighting | Sensor accuracy and reliability weighting in multi-sensor fusion |
| Hierarchical Inference | Sensor -> controller -> plant -> enterprise (ISA-95 levels as inference hierarchy) |
| Expected Free Energy | Objective function in process optimization combining quality targets and uncertainty reduction |

## Key Parallels to Emphasize

1. **Digital twins as generative models**: A process digital twin generates predictions about material state given process inputs — this is exactly the role of a generative model in Active Inference.
2. **SPC as prediction error monitoring**: Control charts track the difference between observed output and the process model's prediction. Out-of-control signals are high prediction errors demanding model update or process intervention.
3. **Bayesian optimization as active inference**: Sequential experimental design in process optimization selects the next experiment to maximally reduce uncertainty — the definition of active sensing under the Expected Free Energy objective.
4. **ISA-95 as hierarchical inference**: The standard manufacturing hierarchy (sensor -> PLC -> SCADA -> MES -> ERP) maps directly onto nested Markov blankets with inference occurring at every level.

Ensure all content adheres to [../resources/notation_table.md](../resources/notation_table.md).
