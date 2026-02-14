# Lab: Sensor Fusion and Bayesian State Estimation

## Objective

Implement and compare sensor fusion approaches for a mobile robot, framing multi-sensor integration as variational inference under a generative model. You will design observation models for multiple sensor modalities, implement precision-weighted fusion, and analyze how Active Inference naturally handles sensor degradation.

## Prerequisites

- Understanding of Bayesian state estimation (prior, likelihood, posterior)
- Familiarity with common robotic sensors (LIDAR, cameras, IMUs, encoders)
- Basic linear algebra and probability theory

## Part 1: Sensor Observation Models

For a mobile robot navigating an indoor environment, specify the observation model for each sensor:

1. **Wheel encoders**: Model the relationship between encoder ticks and robot displacement. Include systematic errors (wheel slip, diameter mismatch) and random noise.
2. **2D LIDAR**: Model range measurements as a function of robot pose and map geometry. Include beam noise, max-range returns, and short-range reflections.
3. **IMU**: Model accelerometer and gyroscope readings. Distinguish between bias drift (slowly varying) and white noise components.
4. **RGB camera**: Describe qualitatively how visual features (corners, edges) provide position information. What is the observation model structure?

For each sensor, specify: measurement rate, noise characteristics, and failure modes.

{fill:textarea}

## Part 2: Precision Weighting and Sensor Reliability

In Active Inference, each sensor channel has an associated precision (inverse variance) that determines its influence on belief updates.

1. Design a scenario where the robot traverses three zones:
   - **Zone A**: Well-lit, textured hallway (camera reliable, LIDAR reliable)
   - **Zone B**: Glass-walled corridor (LIDAR unreliable due to specular reflections, camera reliable)
   - **Zone C**: Dark warehouse section (camera unreliable, LIDAR reliable)

2. For each zone, specify qualitative precision values for each sensor and explain how the Active Inference agent automatically adjusts its reliance on different modalities.

3. How does this compare to a fixed-gain Kalman filter that cannot adjust sensor weights online?

{fill:textarea}

## Part 3: Prediction Error Analysis

Trace a perception cycle for the robot entering Zone B (glass corridor):

1. **Prior belief**: Robot at position (5.0, 2.0) with heading 0 rad, low uncertainty.
2. **Predicted observations**: Expected LIDAR ranges based on wall map; expected camera features based on hallway model.
3. **Actual observations**: LIDAR returns maximum range (beams pass through glass); camera sees corridor features normally.
4. **Prediction errors**: Compute qualitative errors for each sensor channel.
5. **Belief update**: How does the agent resolve the conflict? What role does precision play?

{fill:textarea}

## Part 4: Active Perception

Design a scenario where the robot actively moves to reduce perceptual uncertainty:

1. The robot detects an ambiguous object at the edge of its LIDAR range. Two hypotheses: (a) it is a person, (b) it is a pillar.
2. What actions could the robot take to disambiguate? (e.g., move closer, change viewpoint, activate a different sensor)
3. Frame this as expected free energy minimization: which action is predicted to yield the greatest reduction in uncertainty (epistemic value)?
4. Write pseudocode for an active perception routine:

```
function active_perception(belief, hypotheses, available_actions):
    for each action in available_actions:
        # Compute expected observation under each hypothesis
        # Compute expected information gain
    select action with highest expected information gain
    return selected_action
```

{fill:textarea}

## Part 5: Sensor Fusion Algorithm Design

Write pseudocode for a complete perception update step that fuses all four sensor modalities:

```
function perception_update(prior_belief, observations, precisions, model):
    # 1. Generate predictions from prior belief
    # 2. Compute prediction errors for each sensor
    # 3. Weight errors by sensor precisions
    # 4. Update belief (gradient descent on free energy)
    # 5. Update precision estimates (optional: learn sensor reliability)
    return posterior_belief
```

{fill:textarea}

## Summary Table

| Sensor | Observation Model | Typical Precision | Failure Mode | AI Adaptation |
| --- | --- | --- | --- | --- |
| Wheel encoders | Odometry integration | {fill} | Wheel slip | {fill} |
| 2D LIDAR | Range-bearing model | {fill} | Specular reflection | {fill} |
| IMU | Inertial kinematics | {fill} | Bias drift | {fill} |
| RGB Camera | Feature projection | {fill} | Low light | {fill} |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Thrun, S., Burgard, W., & Fox, D. (2005). *Probabilistic Robotics*. MIT Press, Chapters 2-7.
