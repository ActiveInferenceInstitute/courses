# Station: Agents (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Robotic agent definition, embodied agency, morphological computation, autonomy spectrum
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting formal agent theory to practical robot design

## Content Guidelines

All content in this module must:

1. Define a robotic agent as a system that actively minimizes variational free energy through its sensorimotor coupling with the environment.
2. Distinguish agents from passive systems by emphasizing autonomy, goal-directedness, and adaptive behavior.
3. Use concrete robot examples (mobile robots, manipulators, humanoids) to illustrate the spectrum of agency from reactive controllers to deliberative planners.
4. Address morphological computation: how the robot's physical body shape and material properties offload computation from the generative model.
5. Ground the discussion in practical concerns: what makes a robot an agent is not just software sophistication but the closed-loop coupling between its generative model and its physical embodiment.

## Active Inference Integration

- **Sensorimotor loops**: An agent is defined by its capacity to close the perception-action loop -- sensing the environment, updating beliefs, and acting to confirm predictions.
- **Proprioceptive inference**: The agent maintains a model of its own body (joint angles, end-effector pose) and infers its state from proprioceptive signals, a form of self-modeling essential to agency.
- **Motor commands as predictions**: Actions are selected to minimize expected free energy, meaning the agent acts to bring about observations that it expects (or prefers) under its generative model.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Distinguish between agent-level variables (belief states mu, policies pi) and system-level variables (sensor readings z, actuator commands u).
