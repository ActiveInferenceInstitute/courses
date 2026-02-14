# Station: Perception (Implementation & Simulation)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Python, pymdp, agent-based modeling
- **Topics**: State inference implementation, belief updating code, precision parameter, plotting posterior beliefs, comparison with exact Bayes
- **Lab Style**: Coding Assignment
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module implements perceptual inference (state estimation) in Python. Content should:

1. **Implement the belief updating function**: Given an observation, A matrix, and prior beliefs, compute the posterior using the softmax(ln A[o,:] + ln prior) formula.
2. **Define key implementation concepts**:
   - **infer_states()**: The function that updates beliefs given an observation and generative model
   - **Precision parameter (gamma)**: A scalar that scales the log-evidence, controlling confidence; implemented as a temperature parameter in the softmax
   - **Belief trajectory**: A time series of belief vectors across simulation steps, visualized as a plot
   - **Exact vs. approximate inference**: Comparing the softmax approximation to exact Bayesian computation for small state spaces
3. **Visualize inference dynamics**: Plot how beliefs evolve over time as the agent receives observations, showing convergence to the correct hidden state.
4. **Experiment with precision**: Show how changing the precision parameter affects the speed and accuracy of inference.

## Active Inference Integration

- The infer_states() function is the computational core of perceptual inference in Active Inference
- The precision parameter implements the precision weighting concept from the Cognitive Science and Computational Neuroscience courses
- Comparing exact and approximate inference illustrates why variational methods are necessary for larger state spaces

## Assessment Alignment

Questions should test the ability to:
- Implement the belief updating equation in NumPy
- Plot and interpret belief trajectories for different scenarios
- Predict how changing precision affects inference behavior

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
