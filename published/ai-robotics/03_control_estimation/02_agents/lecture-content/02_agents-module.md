# Module 02: Agents in Robotics

## Learning Objectives

1.  Define **Agents** within the context of Robotics.
2.  Analyze how Agents interacts with other components of the Active Inference framework.
3.  Apply specific constraints of Robotics to the formal definition of Agents.

## Introduction

This module explores **Agents**. In the **Robotics** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Agents is a critical component of the 8-part Active Inference spine, bridging the gap between Systems and Perception.

## Key Concepts

### 1. Agents as a Markov Blanket Boundary
How does Agents define the boundary between the agent and the environment?

### 2. Generative Models of Agents
What parameters involved in Agents must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Agents drive the perception-action loop?

## Applications

In Robotics, we see Agents manifest in:
*   **Specific Example 1**: A PID-controlled robotic joint can be recast as a minimal Active Inference agent: the setpoint defines the agent's prior preference (desired joint angle), the encoder provides sensory states, the motor torque provides active states, and the PID gains implicitly encode the precision weighting of prediction errors -- the proportional gain weights the current position error, the integral gain weights accumulated error, and the derivative gain weights the rate of change, making classical PID control a special case of free energy minimization under a linear-Gaussian generative model.
*   **Specific Example 2**: A Model Predictive Control (MPC) agent on an autonomous ground vehicle defines its agency through a receding-horizon optimization that embodies the Active Inference perception-action loop: at each 50 ms control cycle, the vehicle's Kalman filter estimates the current state (perception), the MPC solver evaluates candidate control sequences over a 2-second prediction horizon against a cost function encoding lane-keeping and obstacle avoidance preferences (planning/action), and the first control input is applied, with the entire process repeating to close the loop.

## Conclusion

Understanding Agents allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
