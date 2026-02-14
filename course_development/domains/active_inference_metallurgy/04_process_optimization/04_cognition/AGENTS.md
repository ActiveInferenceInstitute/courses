# Station: Cognition (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Cognition — Digital Twin Cognition and Process Simulation
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

A digital twin is the explicit generative model of a manufacturing process. It takes process inputs (material composition, temperature setpoints, tool speeds) and generates predictions about process outputs (part dimensions, hardness, residual stress, microstructure). FEA thermal simulations predict temperature fields during heat treatment. CFD models predict melt pool dynamics in additive manufacturing. Surrogate models (Gaussian process, neural network) provide fast approximate predictions when full physics simulations are too slow for real-time control. The digital twin's value is measured by its prediction accuracy — the deviation between its predictions and measured outcomes is the prediction error that drives model refinement.

## Key Mappings

| FEP Concept | Digital Twin Translation |
|-------------|------------------------|
| Generative Model | Digital twin (FEA, CFD, or surrogate model of the process) |
| Cognition | Running the digital twin to predict process outcome before execution |
| Prediction | Simulated temperature field, stress distribution, phase fractions, dimensions |
| Prediction Error | Deviation between digital twin prediction and measured process output |
| Model Fidelity | Physics-based (high fidelity, slow) vs. surrogate (lower fidelity, fast) |
| Model Update | Calibrating digital twin parameters with real process data (data assimilation) |

## Content Guidelines

- Frame the digital twin as the process's internal model of itself — the computational representation that enables prediction, planning, and control
- Treat surrogate models as amortized inference: they trade some accuracy for the speed needed for real-time process control
- Connect data assimilation (Kalman filtering, ensemble methods) to perceptual inference: the digital twin updates its state estimate as new sensor data arrives
- Emphasize that the digital twin's value proposition is reducing physical experimentation by enabling virtual process exploration — counterfactual reasoning at scale

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
