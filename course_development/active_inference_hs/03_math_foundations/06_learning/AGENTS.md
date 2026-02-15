# Station: Learning (Math Foundations)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mathematical reasoning -- parameter estimation, learning rates, and prediction error minimization
- **Topics**: Running Averages, Learning Rate Updates, Curve Fitting, Overfitting vs. Generalization
- **Lab Style**: Guided worksheet with computation exercises and worked examples

## Content Guidelines

- Start with running averages as the simplest learning rule before introducing learning rates.
- Use quiz scores as a relatable scenario for parameter estimation.
- Curve fitting exercises should use graph paper or hand-drawn plots.
- Overfitting should be explained through the concrete tradeoff between fitting training data and predicting new data.

## Active Inference Integration

- Learning in Active Inference means updating the parameters of the generative model.
- The learning rate corresponds to precision -- how much weight new evidence receives.
- Prediction error minimization is the core objective: the agent adjusts its model to reduce the gap between predictions and observations.
- Free energy = accuracy (prediction error) + complexity -- this naturally prevents overfitting.

## Lab Design Principles

- Running average exercises should show stabilization over 5+ data points.
- Learning rate comparison should use two extreme values (e.g., 0.1 vs. 0.5) on the same data.
- Curve fitting should use 5 data points that are roughly linear with some noise.
- Overfitting discussion should compare a 2-parameter model vs. a 5-parameter model on the same data.

## Question Design Standards

- Computational questions should have definite numerical answers.
- Include at least one question comparing fast vs. slow learning rates.
- At least one question should involve computing prediction errors.
- Connect the accuracy-complexity tradeoff to free energy explicitly.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
