# Station: Planning (Control & Estimation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Kalman filters, PID, MPC, active inference
- **Topics**: MPC formulation, receding horizon, constraint handling, tree search, Active Inference equivalences
- **Lab Style**: Simulation Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting mathematical control and estimation theory to Active Inference

## Content Guidelines

All content in this module must:

1. Present planning through rigorous mathematical formulations with explicit equations and derivations.
2. Show the formal relationship between classical planning approaches and Active Inference, including conditions under which they are equivalent.
3. Use standard control theory notation (A, B, C, D matrices; Q, R cost matrices) alongside Active Inference notation (F, G, mu, pi).
4. Include concrete numerical examples with specific robot parameters to make abstract planning concepts tangible.
5. Emphasize computational implementation: pseudo-code, algorithm complexity, and real-time feasibility for robotic applications.

## Active Inference Integration

- **Sensorimotor loops**: Frame planning as part of the continuous perception-action cycle where the robot generates predictions, computes prediction errors, and updates beliefs or actions to minimize free energy.
- **Proprioceptive inference**: Connect planning to the robot's self-model -- its understanding of its own body, capabilities, and limitations as maintained through proprioceptive prediction errors.
- **Motor commands as predictions**: Relate planning to the Active Inference principle that motor commands are predictions about desired sensory outcomes, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
