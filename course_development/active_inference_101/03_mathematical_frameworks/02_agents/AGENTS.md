# Station: Agents (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Variational inference, recognition model q(s), KL divergence, evidence lower bound (ELBO), mean-field approximation
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module introduces variational inference as the mathematical engine of agency. Content should:

1. **Motivate variational inference**: Exact Bayesian inference (computing P(s|o) directly) is often intractable. Variational inference approximates it by finding a simpler distribution q(s) that is close to the true posterior.
2. **Define key terms precisely**:
   - **Recognition model q(s)**: The approximate posterior -- the agent's tractable estimate of what hidden states are most likely
   - **KL divergence D_KL(q||p)**: A measure of how different two probability distributions are; always non-negative, zero only when q = p
   - **Evidence Lower Bound (ELBO)**: The quantity maximized in variational inference; equivalent to minimizing variational free energy
   - **Mean-field approximation**: Assuming that the approximate posterior factorizes into independent components, simplifying computation
3. **Derive the free energy decomposition**: Show that F = -ELBO = Energy - Entropy = -Accuracy + Complexity.
4. **Provide worked numerical examples**: Walk through a simple variational inference problem with 2-3 states.

## Active Inference Integration

- An agent is a system that performs variational inference: maintaining q(s) and updating it to minimize free energy (Friston, 2010)
- The free energy bound F >= -log P(o) guarantees that minimizing F also reduces surprise
- The recognition model q(s) is the mathematical formalization of the agent's beliefs

## Assessment Alignment

Questions should test the ability to:
- Compute KL divergence between two simple distributions
- Derive the relationship between free energy, accuracy, and complexity
- Explain why variational inference is necessary when exact inference is intractable

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
