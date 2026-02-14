# Station: Communication (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: Multi-agent simulation, coupled agents, shared environment, communication channel, belief alignment metrics
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements multi-agent Active Inference, where two agents communicate through a shared environment. Content should:

1. **Implement a two-agent simulation**: Two agents share an environment where each agent's actions are part of the other agent's observations. This creates the coupled inference dynamic.
2. **Define key implementation concepts**:
   - **Multi-agent environment**: A simulation environment that manages two (or more) agents and routes one agent's actions as observations to the other
   - **Communication channel**: The mechanism by which agent A's actions become part of agent B's observation vector and vice versa
   - **Belief alignment metric**: KL divergence between the two agents' belief states, measuring how similar their internal models are
   - **Shared vs. private states**: Some hidden states are common to both agents; others are private to each
3. **Visualize belief convergence**: Plot both agents' beliefs over time, showing how they converge (or fail to converge) through communication.
4. **Experiment with communication noise**: Add noise to the communication channel and show how it affects belief alignment.

## Active Inference Integration

- Multi-agent Active Inference is implemented as two coupled POMDP agents sharing an environment
- Belief alignment corresponds to generalized synchrony from the Mathematical Frameworks course
- Communication noise maps to reduced precision on the communication channel

## Assessment Alignment

Questions should test the ability to:
- Implement the two-agent simulation loop with coupled observations
- Measure and plot belief alignment between agents
- Predict how communication noise affects convergence

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
