# Lab: Active Inference Control vs. Classical Motor Control

## Objective

Compare PID control, Model Predictive Control (MPC), and Active Inference control for a robotic manipulator task. You will design controllers for a 2-DOF planar arm performing a reaching task, analyze their behavior under perturbation, and evaluate how Active Inference unifies perception and action in a single objective.

## Prerequisites

- Understanding of basic control theory (PID, feedback loops)
- Familiarity with robot kinematics (forward/inverse kinematics)
- Module 04: Cognition (world models that support action selection)

## Part 1: Task Specification

A 2-DOF planar robot arm must reach from an initial configuration (q1=0, q2=0) to a target end-effector position (x_target=0.5m, y_target=0.3m). The arm has link lengths L1=0.4m and L2=0.3m.

1. Write the forward kinematics equations mapping joint angles (q1, q2) to end-effector position (x, y).
2. Compute the target joint angles using inverse kinematics.
3. Define the observation model: the robot observes joint angles via encoders (with noise sigma_q = 0.01 rad) and end-effector position via a camera (with noise sigma_xy = 0.005 m).

{fill:textarea}

## Part 2: PID Controller Design

Design a joint-space PID controller for the reaching task:

1. Specify the error signal: e(t) = q_target - q_measured.
2. Choose PID gains (Kp, Ki, Kd) and justify your choices.
3. Describe the controller output: torque commands tau = Kp*e + Ki*integral(e) + Kd*de/dt.
4. What happens if an unexpected load is placed on the end-effector during the reach? How does the PID controller respond?

{fill:textarea}

## Part 3: Active Inference Controller Design

Design an Active Inference controller for the same reaching task:

1. **Generative model**: Specify prior preferences over observations (desired joint angles and end-effector position).
2. **Prediction errors**: Define sensory prediction errors (difference between predicted and observed joint angles) and active prediction errors (difference between desired and predicted proprioceptive states).
3. **Action as reflex arc**: In Active Inference, motor commands arise from proprioceptive prediction errors -- the arm moves to fulfill its own predictions. Write the update equation:
   - u = -dF/da (action minimizes free energy by changing sensory input)
4. How does the Active Inference controller handle the unexpected load? Compare with PID.

{fill:textarea}

## Part 4: Perturbation Analysis

Compare all three controllers (PID, MPC, Active Inference) under three perturbation scenarios:

| Scenario | PID Response | MPC Response | Active Inference Response |
| --- | --- | --- | --- |
| External force on end-effector | {fill} | {fill} | {fill} |
| Encoder noise increases 10x | {fill} | {fill} | {fill} |
| Joint 2 motor loses 50% torque | {fill} | {fill} | {fill} |

For each scenario, describe qualitatively how the controller adapts (or fails to adapt).

{fill:textarea}

## Part 5: Unified Perception-Action Pseudocode

Write pseudocode for a complete Active Inference control loop that unifies perception and action:

```
function active_inference_control(dt):
    while not reached_target:
        # Perception: update beliefs about joint angles
        mu_q += dt * (d_mu_q - kappa * prediction_error_proprio)

        # Perception: update beliefs about end-effector
        mu_x += dt * (d_mu_x - kappa * prediction_error_visual)

        # Action: generate motor commands from prediction errors
        torque = -kappa_a * (mu_q - q_desired)

        # Apply torque and read new sensors
        apply(torque)
        q_obs, x_obs = read_sensors()
```

Extend this pseudocode to handle the perturbation scenarios from Part 4.

{fill:textarea}

## Summary Table

| Feature | PID | MPC | Active Inference |
| --- | --- | --- | --- |
| Objective function | Error minimization | Cost over horizon | Free energy minimization |
| Perception integration | None (assumes known state) | State estimator separate | Unified with control |
| Adaptation | Requires gain scheduling | Requires model updates | Precision learning |
| Computational cost | {fill} | {fill} | {fill} |
| Robustness to noise | {fill} | {fill} | {fill} |

## References

- Pio-Lopez, L., Nizard, A., Friston, K., & Pezzulo, G. (2016). Active Inference and robot control. *Journal of the Royal Society Interface*, 13(122).
- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Oliver, G., Lanillos, P., & Cheng, G. (2021). An empirical study of active inference on a humanoid robot. *IEEE Transactions on Cognitive and Developmental Systems*.
