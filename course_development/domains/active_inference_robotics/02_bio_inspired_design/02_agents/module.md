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
*   **Specific Example 1**: A swarm of 100 Kilobot-sized robots inspired by ant colony behavior acts as a collective Active Inference agent -- each individual robot maintains a minimal generative model (sensing only local neighbor density and pheromone-analog IR signals), yet the swarm-level Markov blanket emerges from the aggregation of individual sensory and active states, enabling the collective to perform foraging and nest-construction tasks that no single unit could plan or execute.
*   **Specific Example 2**: An insect-inspired micro aerial vehicle (MAV) modeled on the hawkmoth implements agency through a tightly coupled sensorimotor loop where 200 Hz optic flow sensors (analogous to compound eyes) directly modulate wing kinematics without explicit state estimation, embodying the Active Inference principle that the simplest agents can minimize free energy through reactive policies when their generative model is implicit in the morphological coupling between body and environment.

## Conclusion

Understanding Agents allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
