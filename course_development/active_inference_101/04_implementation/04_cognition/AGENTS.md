# Station: Cognition (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: T-maze task implementation, full POMDP setup, multi-step inference, free energy computation, visualization of agent behavior
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements the T-maze, the canonical Active Inference demonstration task. Content should:

1. **Implement the T-maze environment**: A simple grid world where the agent must infer which arm of the T contains a reward, with a cue location providing partial information.
2. **Define key implementation concepts**:
   - **T-maze**: A standard Active Inference benchmark with states (location x reward-location), observations (cue, reward, null), and actions (move left, move right, stay)
   - **Free energy computation**: The function that computes F = E_q[ln q(s) - ln P(o, s)] for the current beliefs and observations
   - **Multi-step inference**: Running the belief updating across multiple time steps within a trial, not just a single observation
   - **Visualization**: Plotting the agent's position, beliefs, and free energy over time to understand its behavior
3. **Walk through a complete trial**: From initial beliefs through cue observation to reward/no-reward outcome, showing all computations at each step.
4. **Compute and plot free energy**: Show how VFE decreases as the agent gathers information and resolves uncertainty.

## Active Inference Integration

- The T-maze is the standard benchmark task in the Active Inference literature (Friston et al., 2015; Parr et al., 2022)
- This implementation brings together all components: generative model, state inference, and (previewing Module 05) policy selection
- Free energy computation provides a single metric for tracking the agent's performance

## Assessment Alignment

Questions should test the ability to:
- Set up the A, B, C, D matrices for the T-maze
- Trace through a complete trial computing beliefs and free energy at each step
- Modify the T-maze to test different scenarios (e.g., ambiguous cue, no cue)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
