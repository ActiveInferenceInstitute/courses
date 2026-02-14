# Station: Perception (Robotic Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Sensors, actuators, embedded systems
- **Topics**: Sensor fusion, state estimation, observation models, precision weighting, active perception
- **Lab Style**: Hardware Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, bridging probabilistic robotics with Active Inference

## Content Guidelines

All content in this module must:

1. Frame robotic perception as variational inference: the robot infers hidden states (pose, map, object identity) from noisy sensor observations by minimizing variational free energy.
2. Emphasize multi-sensor fusion as precision-weighted prediction error minimization, connecting directly to Kalman filtering and particle filtering as special cases.
3. Use concrete sensor examples (LIDAR, cameras, IMUs, encoders, force-torque sensors) with realistic noise models and failure modes.
4. Distinguish between exteroceptive perception (sensing the external world) and proprioceptive perception (sensing the robot's own body state).
5. Address active perception: the agent moves and orients its sensors to reduce uncertainty, selecting actions with high epistemic value.

## Active Inference Integration

- **Sensorimotor loops**: Perception is not passive data collection but active hypothesis testing. The robot generates predictions about sensor readings and updates beliefs based on prediction errors.
- **Proprioceptive inference**: The robot infers its own joint angles, end-effector position, and body configuration from proprioceptive sensors (encoders, strain gauges), maintaining a self-model.
- **Motor commands as predictions**: Perception and action are dual aspects of the same process. Active perception selects movements that maximize information gain (minimize expected free energy).

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md). Use z for observations, s for hidden states, Pi (capital) for precision matrices, epsilon for prediction errors.
