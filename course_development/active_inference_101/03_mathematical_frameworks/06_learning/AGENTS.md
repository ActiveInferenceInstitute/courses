# Station: Learning (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Dirichlet distributions, parameter learning, concentration parameters, Bayesian model reduction, model evidence
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module formalizes learning as inference over model parameters. Content should:

1. **Introduce Dirichlet distributions**: The A, B, and D matrices are learned through Dirichlet priors, where concentration parameters accumulate evidence from experience.
2. **Define key terms precisely**:
   - **Dirichlet distribution**: A distribution over probability vectors, parameterized by concentration parameters; the conjugate prior for categorical distributions
   - **Concentration parameters**: Numbers that encode how many times each state-observation pair has been experienced; higher values = more confidence
   - **Bayesian Model Reduction (BMR)**: A method for evaluating whether parts of the model contribute to model evidence, pruning those that do not
   - **Model evidence P(o)**: The probability of observations under the model; higher evidence = better model
3. **Show parameter learning as accumulation**: Each observation increments the corresponding concentration parameter, making the learned distribution increasingly peaked.
4. **Derive BMR**: Show how comparing model evidence with and without a parameter determines whether to keep or prune it.

## Active Inference Integration

- Parameter learning is inference on a slow timescale, updating Dirichlet hyperparameters (Friston et al., 2017)
- BMR provides a principled method for structure learning (model simplification) without exhaustive model comparison
- The interplay between parameter learning and structure learning implements the accuracy-complexity trade-off over developmental timescales

## Assessment Alignment

Questions should test the ability to:
- Update Dirichlet concentration parameters given a sequence of observations
- Compare model evidence for two models to determine which is better supported
- Explain how BMR prunes unnecessary model complexity

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
