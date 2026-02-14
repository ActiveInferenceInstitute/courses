# Station: Learning (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: Dirichlet parameter updates, learning rate, A-matrix learning, multi-trial learning curves, Bayesian model reduction in code
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements parameter learning (updating the generative model from experience). Content should:

1. **Implement Dirichlet updating**: After each trial, update the concentration parameters of the A and B matrices by incrementing counts for observed state-observation pairs.
2. **Define key implementation concepts**:
   - **Concentration parameter array**: A NumPy array (same shape as A or B matrix) storing accumulated counts; the learned matrix is computed by normalizing columns
   - **Learning rate (eta)**: A scalar controlling how much each new observation updates the concentration parameters
   - **Multi-trial simulation**: Running the agent across many trials and tracking how the learned model improves
   - **Learning curve**: A plot showing performance (e.g., reward rate, free energy) as a function of trial number
3. **Demonstrate A-matrix learning**: Start with a uniform A matrix and show how the agent learns the correct observation model from experience.
4. **Implement basic BMR**: Show how to compare model evidence with and without specific parameters and prune the model accordingly.

## Active Inference Integration

- Parameter learning in code directly implements the Dirichlet update rule from the Mathematical Frameworks course
- Learning curves show the transition from exploration-dominated to exploitation-dominated behavior as the model improves
- BMR implementation demonstrates structure learning (model simplification) computationally

## Assessment Alignment

Questions should test the ability to:
- Implement the Dirichlet update for the A matrix after a sequence of observations
- Generate and interpret learning curves across multiple trials
- Compare agent performance with and without parameter learning

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
