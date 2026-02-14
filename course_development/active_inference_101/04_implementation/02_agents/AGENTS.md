# Station: Agents (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: Agent class implementation, perception-action loop, belief initialization, simulation harness, pymdp Agent class
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements the Active Inference agent as a Python class. Content should:

1. **Build the Agent class**: Implement an agent that holds a generative model, maintains beliefs q(s), and runs the perception-action loop.
2. **Define key implementation concepts**:
   - **Agent class**: A Python object encapsulating the generative model, current beliefs, and methods for inference and action
   - **Perception-action loop**: The main simulation loop: observe -> infer states -> select action -> act -> repeat
   - **Belief vector**: A NumPy array representing q(s), the agent's current beliefs about hidden states
   - **Environment class**: A separate object that maintains the true hidden state and generates observations
3. **Introduce pymdp**: Show how the pymdp library implements the same agent with less boilerplate code, comparing custom implementation to library usage.
4. **Run a basic simulation**: Execute the agent for multiple timesteps in a simple environment, recording beliefs and actions.

## Active Inference Integration

- The Agent class is the computational realization of the Active Inference agent from the Cognitive Science and Mathematical Frameworks courses
- The perception-action loop implements the predict-compare-update cycle in code
- pymdp provides a validated reference implementation for comparison

## Assessment Alignment

Questions should test the ability to:
- Implement the basic perception-action loop given a generative model and environment
- Compare custom agent implementation with pymdp's Agent class
- Debug issues in the simulation loop (incorrect belief updating, wrong observation indexing)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
