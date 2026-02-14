# Station: Planning (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Path planning, mission planning, expected free energy, exploration-exploitation, hierarchical planning
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, bridging classical motion planning with Active Inference

## Content Guidelines

All content in this module must:

1. Frame planning as expected free energy minimization over future trajectories, where the robot evaluates candidate action sequences by their predicted consequences.
2. Decompose expected free energy into pragmatic value (goal-seeking, preference satisfaction) and epistemic value (information gain, uncertainty reduction).
3. Compare classical planning algorithms (A*, RRT, potential fields, MPC) with Active Inference planning, showing how AI naturally integrates exploration and exploitation.
4. Address hierarchical planning: task-level mission planning on topological graphs and navigation-level path planning on metric maps, connected through a hierarchical generative model.
5. Use concrete navigation and mission planning scenarios with realistic constraints (obstacle avoidance, energy budgets, time limits).

## Active Inference Integration

- **Sensorimotor loops**: Planning extends the perception-action loop into the future. The robot simulates future sensorimotor interactions to evaluate candidate policies before executing them.
- **Proprioceptive inference**: Plans must account for the robot's own capabilities and limitations (maximum speed, turning radius, battery level) as part of the self-model.
- **Motor commands as predictions**: A plan is a sequence of predicted future actions. The first action in the best plan is executed, and the plan is revised as new observations arrive (receding horizon).

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use G for expected free energy, pi for policy, tau for time horizon, and C for prior preferences.
