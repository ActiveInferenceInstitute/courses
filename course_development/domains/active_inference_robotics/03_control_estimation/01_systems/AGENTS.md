# Station: Systems (Control & Estimation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Kalman filters, PID, MPC, active inference
- **Topics**: state-space models, transfer functions, system identification, Active Inference equivalences
- **Lab Style**: Simulation Lab
- **Audience**: Robotics engineers and researchers
- **Tone**: Engineering-focused, connecting mathematical control and estimation theory to Active Inference

## Content Guidelines

All content in this module must:

1. Present systems through rigorous mathematical formulations with explicit equations and derivations.
2. Show the formal relationship between classical systems approaches and Active Inference, including conditions under which they are equivalent.
3. Use standard control theory notation (A, B, C, D matrices; Q, R cost matrices) alongside Active Inference notation (F, G, mu, pi).
4. Include concrete numerical examples with specific robot parameters to make abstract systems concepts tangible.
5. Emphasize computational implementation: pseudo-code, algorithm complexity, and real-time feasibility for robotic applications.

## Active Inference Integration

- **Sensorimotor loops**: Frame systems as part of the continuous perception-action cycle where the robot generates predictions, computes prediction errors, and updates beliefs or actions to minimize free energy.
- **Proprioceptive inference**: Connect systems to the robot's self-model -- its understanding of its own body, capabilities, and limitations as maintained through proprioceptive prediction errors.
- **Motor commands as predictions**: Relate systems to the Active Inference principle that motor commands are predictions about desired sensory outcomes, selected to minimize expected free energy.

## Notation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
