# Module 01: Systems in 101

## Learning Objectives

1.  Define **Systems** within the context of 101.
2.  Analyze how Systems interacts with other components of the Active Inference framework.
3.  Apply specific constraints of 101 to the formal definition of Systems.

## Introduction

This module explores **Systems**. In the **101** curriculum, we approach this topic with a focus on specific applications and theoretical depth appropriate for the audience. Systems is a critical component of the 8-part Active Inference spine, bridging the gap between the course introduction and Computational Neuroscience.

At the college introductory level, systems thinking provides the essential scaffolding for understanding Active Inference. Before we can discuss how agents perceive, think, or act, we must first establish what it means for something to be a system -- a collection of interacting components that maintains itself as a distinct entity within a larger environment. This unit grounds that intuition in the formalism of Markov blankets, variational free energy, and generative models, while keeping the mathematics accessible to students encountering these ideas for the first time.

Across the eight modules in this unit, you will move from a general systems perspective (how do we define and bound a system?) through the roles of agents, perception, cognition, action, learning, communication, and planning. Each module builds on the last, so that by the end of the unit you will have a working vocabulary for describing any adaptive system in Active Inference terms. The cognitive science lens used here emphasizes empirical findings from psychology and neuroscience that motivate the formal framework.

## Key Concepts

### 1. Systems as a Markov Blanket Boundary
How does Systems define the boundary between the agent and the environment?

### 2. Generative Models of Systems
What parameters involved in Systems must be optimized to minimize variational free energy?

### 3. Active Inference Dynamics
How does the process of Systems drive the perception-action loop?

## Applications

In 101, we see Systems manifest in:
*   **Specific Example 1**: Consider the thermostat as a minimal system. A thermostat maintains a Markov blanket between its internal state (the set-point temperature) and the external environment (the room temperature). Its sensory states are the thermometer readings, and its active states are the on/off signals to the heater. Despite its simplicity, a thermostat illustrates the core systems concept: an entity that maintains a boundary, senses deviations from expected states, and acts to minimize surprise. This example scales naturally into biological systems such as homeostatic regulation in the human body.
*   **Specific Example 2**: A university classroom itself can be viewed as a system in Active Inference terms. The classroom has internal states (the shared knowledge among students and instructor), sensory states (questions asked, facial expressions of confusion or understanding), and active states (lectures, discussions, assignments). The Markov blanket of the classroom separates its internal pedagogical dynamics from the broader campus environment. Students within the system form nested sub-systems, each with their own blankets, illustrating the hierarchical and multi-scale nature of systems that Active Inference formalizes.

## Conclusion

Understanding Systems allows us to better model complex adaptive systems. In the next module, we will expand on this foundation.
