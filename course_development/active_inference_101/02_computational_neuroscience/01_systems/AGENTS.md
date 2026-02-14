# Station: Systems (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Dynamical systems, neural populations, oscillations, attractors, neural Markov blankets
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module introduces the brain as a dynamical system, building on the general systems concepts from Cognitive Science Module 01. Content should:

1. **Ground systems in neuroscience**: Move from abstract systems to concrete neural systems. Neurons, populations, oscillations, and attractors are the building blocks.
2. **Define key terms precisely**:
   - **Dynamical system**: A system whose state evolves over time according to deterministic or stochastic rules
   - **Neural population**: A group of neurons whose collective activity encodes information
   - **Attractor**: A stable pattern of neural activity that the system tends to settle into (fixed-point, limit-cycle, or strange)
   - **Neural oscillation**: Rhythmic patterns of firing (alpha, beta, gamma, theta) that coordinate activity across brain regions
3. **Connect to the Markov blanket at neural scales**: A neuron's dendrites are sensory states, its axon terminals are active states, and its membrane potential is the internal state.
4. **Use dynamical systems language**: State space, trajectory, attractor landscape, basin of attraction.

## Active Inference Integration

- Neural attractors implement beliefs: memory recall is the brain being attracted to a stored pattern
- Oscillations coordinate precision weighting across neural populations
- The hierarchical structure of cortical Markov blankets enables hierarchical inference (Friston, 2010)

## Assessment Alignment

Questions should test the ability to:
- Describe the brain as a dynamical system with concrete examples of states, rules, and trajectories
- Identify the Markov blanket of a neuron or brain region
- Explain how attractor dynamics relate to perception and memory

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
