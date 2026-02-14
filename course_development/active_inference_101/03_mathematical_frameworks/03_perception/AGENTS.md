# Station: Perception (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Free energy minimization, belief updating equations, precision as inverse variance, gradient descent on free energy
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module derives the mathematics of perceptual inference. Content should:

1. **Derive the belief updating rule**: Show how minimizing variational free energy with respect to q(s) yields the optimal approximate posterior. For categorical distributions, this gives a softmax function over log-probabilities.
2. **Define key terms precisely**:
   - **Variational free energy F**: F = E_q[ln q(s) - ln P(o, s)] -- the quantity minimized during perception
   - **Belief updating**: The iterative process of adjusting q(s) to minimize F, converging on the best explanation of current observations
   - **Precision (pi)**: The inverse variance of a distribution; high precision = narrow/confident distribution, low precision = broad/uncertain distribution
   - **Gradient descent**: An optimization algorithm that iteratively reduces F by moving q(s) in the direction of steepest descent
3. **Work through a complete perceptual inference example**: Given A matrix, D vector, and an observation, compute the posterior belief step by step.
4. **Connect precision to the accuracy-complexity trade-off**: High precision on data favors accuracy; high precision on priors favors simplicity.

## Active Inference Integration

- Perception is the minimization of F with respect to q(s), holding actions fixed (Parr et al., 2022, Chapter 4)
- The belief updating equations for categorical distributions: q(s) = softmax(ln A[o,:] + ln D)
- Precision weighting enters through the relative weight of likelihood versus prior terms

## Assessment Alignment

Questions should test the ability to:
- Compute updated beliefs given an observation and a generative model
- Explain how changing precision affects the balance between prior and likelihood
- Derive the free energy for a simple two-state, two-observation model

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
