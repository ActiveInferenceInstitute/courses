# Notation Table: Active Inference for Robotics

> Standard symbols and notation used throughout the curriculum.
> Level: Robotics engineers and researchers

## Core Active Inference Symbols

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| F | Free energy | Variational free energy, upper bound on surprise | Course 1, M1 |
| G | Expected free energy | Predicted free energy under a policy | Course 1, M8 |
| mu | Belief | Approximate posterior expectation | Course 1, M2 |
| pi | Policy | Sequence of planned actions | Course 1, M8 |
| epsilon | Prediction error | Difference between predicted and observed | Course 1, M3 |
| Pi (capital) | Precision | Inverse variance, confidence in a signal | Course 1, M3 |
| C | Prior preferences | Preferred observations (goals) | Course 1, M2 |
| theta | Model parameters | Learnable parameters of the generative model | Course 1, M6 |
| eta | Learning rate | Step size for parameter updates | Course 1, M6 |

## Robotics-Specific Symbols

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| q | Joint angles | Robot configuration vector | Course 1, M1 |
| u | Control input | Motor commands (torques, voltages) | Course 1, M5 |
| z | Observation | Sensor measurement vector | Course 1, M3 |
| x | State | Hidden state vector (pose, velocity) | Course 1, M1 |
| A, B, C, D | State-space matrices | System dynamics and observation matrices | Course 3, M1 |
| Q | Process noise covariance | Uncertainty in dynamics model | Course 3, M3 |
| R | Observation noise covariance | Uncertainty in sensor measurements | Course 3, M3 |
| K | Kalman gain / Control gain | Weighting matrix for updates | Course 3, M3 |
| J | Cost function | Objective to minimize in optimal control | Course 3, M5 |
| tau | Time horizon | Planning depth in timesteps | Course 1, M8 |

## System Architecture Symbols

| Symbol | Plain English | Formal Meaning | First Introduced |
| --- | --- | --- | --- |
| System | A thing with a boundary | An entity with internal and external states | Course 1, M1 |
| Agent | Something that acts | A system that minimizes free energy | Course 1, M2 |
| Prediction | A guess about what will happen | Expected sensory input under the model | Course 1, M3 |
| Surprise | When reality differs from expectation | Negative log probability of observations | Course 1, M3 |
| Action | Making something happen | Changing the world to match predictions | Course 1, M5 |
| Learning | Getting better over time | Updating model parameters to reduce F | Course 1, M6 |

## Conventions

- Vectors are lowercase bold: **x**, **z**, **u**
- Matrices are uppercase bold: **A**, **B**, **K**
- Scalar quantities are italic: *F*, *G*, *J*
- Time indices are subscripts: x_t, z_{t+1}
- Derivatives use dot notation for time: x_dot = dx/dt
- Partial derivatives: dF/dmu, dF/dtheta

## Navigation

- [Glossary](./glossary.md)
- [References](./references.md)
- [Home](../README.md)
