# Station: Cognition (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Probabilistic world models, SLAM, factor graphs, hierarchical representations, model selection
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting cognitive science concepts to implementable robotic architectures

## Content Guidelines

All content in this module must:

1. Frame robotic cognition as the construction, maintenance, and revision of generative world models that enable prediction, planning, and decision-making.
2. Connect SLAM (Simultaneous Localization and Mapping) to Active Inference: SLAM is joint inference over robot poses and environment structure under a generative model.
3. Use factor graphs as a computational representation of generative models, showing how message-passing algorithms implement variational inference.
4. Address hierarchical world models: metric maps (geometry), topological maps (connectivity), and semantic maps (object categories) as levels of a deep generative model.
5. Emphasize model complexity and Occam's principle: the free energy objective naturally penalizes overly complex world models, favoring parsimonious explanations.

## Active Inference Integration

- **Sensorimotor loops**: Cognition connects perception to action by maintaining a world model that predicts future observations given planned actions.
- **Proprioceptive inference**: The cognitive model includes a self-model -- the robot's understanding of its own kinematics, dynamics, and capabilities.
- **Motor commands as predictions**: Planning and action selection emerge from simulating future trajectories through the world model and evaluating their expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use m for world model, G for factor graph, H for hierarchical level indices.
