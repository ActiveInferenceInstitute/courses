# Unit 03: Control and Estimation — Overview

## Learning Objectives

1. Define the **control-estimation paradigm** as the engineering instantiation of the Active Inference perception-action loop in robotic systems.
2. Analyze how classical estimation (Kalman filtering, particle filtering) and control (PID, LQR, MPC) methods map onto Active Inference constructs.
3. Apply the integrated control-estimation framework to real robotic system design.

## Introduction

Control and estimation are the twin pillars of robotic engineering. **Estimation** answers: "Given noisy sensor data, what is the true state of the robot and its environment?" **Control** answers: "Given the estimated state and desired goals, what motor commands should be issued?" Together, they implement the perception-action loop that Active Inference formalizes as free energy minimization.

This unit demonstrates that classical control and estimation theory — Kalman filters, PID controllers, LQR, MPC, impedance control — are not merely *analogous* to Active Inference; they are **specific implementations** of Active Inference under particular mathematical assumptions (linearity, Gaussianity, quadratic costs). Understanding this relationship allows roboticists to move fluidly between classical and Active Inference formulations, choosing the most appropriate framework for each design problem.

## Key Concepts

### 1. The Perception-Action Loop in Hardware

The control-estimation loop has physically identifiable components:

- **Sensors** (perception): Encoders, cameras, LiDAR, IMUs, force/torque sensors — each implementing a specific observation model (A matrix)
- **Estimator** (inference): Kalman filter, particle filter, or optimization-based estimator — maintaining the probabilistic state belief
- **Controller** (action): PID, LQR, MPC, or Active Inference controller — computing motor commands from state beliefs and goals
- **Actuators** (execution): Motors, hydraulics, pneumatics — converting commands into physical forces and torques

The loop runs continuously at rates from 100 Hz (position control) to 10 kHz (current control), implementing real-time free energy minimization.

### 2. Classical-to-AIF Translation Table

| Classical Concept | Active Inference Equivalent |
|---|---|
| State estimate | Approximate posterior μ |
| Kalman gain | Precision-weighted prediction error gain |
| Process noise | B matrix uncertainty (transition precision) |
| Measurement noise | A matrix uncertainty (observation precision) |
| Setpoint / Reference | Preferred observation (C vector) |
| Control error | Proprioceptive prediction error |
| PID gains | Precision parameters (Kp ↔ ω_p, Ki ↔ ω_i, Kd ↔ ω_d) |
| Cost function (LQR) | Negative expected free energy |
| Model Predictive Control | EFE minimization over finite horizon |
| Impedance | Precision on proprioceptive vs. force predictions |

### 3. When to Use Classical vs. AIF Formulation

- **Use classical formulation** when: the system is linear or well-approximated as linear, the noise is Gaussian, the cost is quadratic, and real-time performance is critical. Classical methods are computationally efficient and well-understood.
- **Use AIF formulation** when: the system is highly nonlinear, multi-modal uncertainty matters, the agent must balance exploration and exploitation, or the system needs to adapt its own model online.

## Applications

- **Robot arm trajectory tracking**: A 6-DOF robot arm uses the classical control-estimation framework — joint encoders provide precise state observations (high-precision A matrix), a rigid-body dynamics model provides the B matrix, and cascaded PID controllers minimize proprioceptive prediction errors at each joint.
- **Autonomous drone with adaptive control**: A quadrotor in turbulent wind uses AIF-inspired adaptive estimation — the estimator detects rising prediction errors (unmodeled wind gusts) and automatically reduces the precision of the transition model (increasing process noise), allowing the estimator to weight observations more heavily than predictions.

## Conclusion

Control and estimation are Active Inference made engineering. This unit's 8 modules explore each component — systems, agents, perception, cognition, action, learning, communication, and planning — through the control-estimation lens, building the bridge between classical robotics and the Active Inference framework.
