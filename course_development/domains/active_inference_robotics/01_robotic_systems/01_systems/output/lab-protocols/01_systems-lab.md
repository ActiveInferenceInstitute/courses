# Lab: Robotic Systems Architecture and Markov Blankets

## Objective

Analyze a robotic system by identifying its Markov blanket boundaries and mapping the sensor-actuator architecture to Active Inference components. You will decompose a mobile robot into internal states, sensory states, active states, and external states, then evaluate how this decomposition informs system design.

## Prerequisites

- Familiarity with basic robot architectures (sensors, actuators, controllers)
- Understanding of the Markov blanket formalism (internal, external, sensory, active states)
- Basic block diagram or pseudocode skills

## Part 1: System Boundary Identification

Consider a differential-drive mobile robot equipped with LIDAR, wheel encoders, an IMU, and two DC motors.

1. Draw or describe a block diagram that partitions the robot into Active Inference state types:
   - **Internal states**: onboard computation, belief states, generative model parameters
   - **Sensory states**: LIDAR range measurements, encoder ticks, IMU readings
   - **Active states**: motor voltage commands, LED indicators
   - **External states**: obstacles, floor surface, ambient lighting

2. For each sensory channel, specify the observation likelihood model p(o|s) in plain language. For example: "LIDAR returns a range measurement corrupted by Gaussian noise with variance proportional to distance."


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 2: Generative Model Specification

Design a simplified generative model for the robot's position estimation:

1. Define the hidden state vector (e.g., x, y, theta).
2. Write the state transition model as a difference equation: x_{t+1} = f(x_t, u_t) + w_t.
3. Write the observation model for at least two sensor modalities: z_t = h(x_t) + v_t.
4. Specify reasonable noise covariance matrices Q (process) and R (observation).


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 3: Sensor Fusion via Free Energy Minimization

Compare two approaches to fusing LIDAR and encoder data:

1. **Classical approach**: Describe how an Extended Kalman Filter would fuse these measurements.
2. **Active Inference approach**: Describe how variational free energy minimization over the generative model achieves the same fusion, emphasizing the role of precision weighting.
3. Under what conditions would the Active Inference approach weight LIDAR more heavily than encoders? When would it do the opposite?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 4: Architecture Trade-offs

Evaluate the following design decisions through the lens of Active Inference:

1. Adding a camera to the sensor suite: How does this change the generative model complexity? What is the trade-off between model accuracy and computational cost (model complexity term in free energy)?
2. Replacing DC motors with stepper motors: How does increased actuator precision affect the active states and the expected free energy of actions?
3. Moving computation from an onboard microcontroller to a cloud server: How does communication latency affect the temporal depth of the generative model?


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Part 5: Pseudocode Design

Write pseudocode for a single perception-action cycle of your robot system:

```
function active_inference_step(belief, observation, model):
    # Step 1: Prediction error
    # Step 2: Belief update (perception)
    # Step 3: Action selection (minimize expected free energy)
    # Step 4: Execute action
    # Return updated belief
```

Fill in each step with operations specific to your differential-drive robot scenario.


<div style="border: 1px solid #ccc; border-radius: 4px; min-height: 96px; padding: 8px; margin: 8px 0; background-color: #fafafa;"><em style="color: #999; font-size: 0.85em;">Write your response here</em></div>


## Summary Table

| Component | Classical Robotics Term | Active Inference Term | Your Robot Example |
| --- | --- | --- | --- |
| Sensors | Observation model | Likelihood mapping | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Actuators | Control input | Active states | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Controller | State estimator + planner | Free energy minimization | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| World model | Dynamics model | Generative model | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |
| Noise handling | Kalman gain | Precision weighting | <span style="border-bottom: 1px solid #999; display: inline-block; min-width: 200px;">&nbsp;</span> |

## References

- Lanillos, P., et al. (2021). Active Inference in Robotics and Artificial Agents. *Frontiers in Neurorobotics*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press, Chapters 2-3.
