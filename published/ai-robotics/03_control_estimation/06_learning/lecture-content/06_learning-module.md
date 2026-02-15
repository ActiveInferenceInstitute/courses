# Module 06: Learning in Robotics

## Learning Objectives

1.  Define **Learning** within the context of Robotics.
2.  Analyze how Learning interacts with other components of the Active Inference framework.
3.  Apply specific constraints of Robotics to the formal definition of Learning.

## Introduction

This module explores **Learning**. In the **Robotics** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Learning is a critical component of the 8-part Active Inference spine, bridging the gap between Action and Communication.

## Key Concepts

### 1. Learning as a Markov Blanket Boundary
How does Learning define the boundary between the agent and the environment?

### 2. Generative Models of Learning
What parameters involved in Learning must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Learning drive the perception-action loop?

## Applications

In Robotics, we see Learning manifest in:
*   **Specific Example 1**: An adaptive control system on a robotic arm learns unknown payload mass and center-of-gravity parameters online using recursive least squares: as the arm moves and observes discrepancies between predicted and actual joint torques (prediction errors), it updates the inertial parameter estimates in its dynamics model, progressively reducing free energy so that after 10-15 seconds of motion, the controller compensates for the unknown payload as accurately as if the parameters had been known a priori.
*   **Specific Example 2**: A Gaussian Process (GP) regression model learns the residual dynamics of a quadrotor (unmodeled aerodynamic effects, motor asymmetries) from flight data, augmenting a nominal physics-based model; after each flight, the GP updates its posterior over the residual function, reducing the model's prediction error on subsequent flights -- this is parameter learning in the Active Inference sense, where the generative model's structure (nominal physics plus GP residual) is fixed but its parameters are optimized to minimize long-term variational free energy.

## Conclusion

Understanding Learning allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
