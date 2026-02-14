# Station: Learning (Process Optimization)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Heat treatment, welding, additive manufacturing, Industry 4.0
- **Topics**: Learning — Closed-Loop Control and Adaptive Manufacturing
- **Lab Style**: Digital Twin Lab
- **Audience**: Process engineers, manufacturing engineers, and Industry 4.0 specialists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Closed-loop control and adaptive manufacturing implement learning in industrial processes. Statistical process control (SPC) detects when the process drifts beyond expected bounds — this is prediction error monitoring. When SPC signals an out-of-control condition, the process engineer investigates root causes and updates the process model (learning). Bayesian optimization enables systematic process improvement by selecting the next experiment to maximally reduce uncertainty about the optimal process parameters. Reinforcement learning applied to manufacturing (e.g., adaptive welding, AM process control) implements the full Active Inference loop: sense state, evaluate prediction error, select action, observe outcome, update model.

## Key Mappings

| FEP Concept | Adaptive Manufacturing Translation |
|-------------|-------------------------------------|
| Learning | Updating process model parameters based on production data |
| Prediction Error Monitoring | SPC control charts detecting process drift |
| Model Update | Adjusting control setpoints, PID gains, or digital twin parameters |
| Active Learning | Bayesian optimization selecting next experiment to maximize information gain |
| Reinforcement Learning | Adaptive control policies that improve with production experience |
| Transfer Learning | Applying process knowledge from one alloy or geometry to a new one |

## Content Guidelines

- Frame SPC as the production-floor implementation of prediction error monitoring — control limits define the acceptable range of prediction error before model update is triggered
- Treat Bayesian optimization as Active Inference in the experimental design domain: the acquisition function balances exploitation (testing near known good parameters) and exploration (probing uncertain regions)
- Connect adaptive control in AM (adjusting laser power, scan speed in real time) to online model learning — the controller updates its process model during the build
- Emphasize that the goal of adaptive manufacturing is to reduce the need for post-process inspection by building quality in through real-time learning and correction

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
