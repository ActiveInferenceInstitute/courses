# Station: Systems (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Random variables, probability distributions, Bayes' theorem, generative models, Hidden Markov Models
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module establishes the probabilistic language of Active Inference. Content should:

1. **Start from probability basics**: Random variables, discrete and continuous distributions, joint/marginal/conditional probability. Assume only basic algebra and intuitive understanding of probability.
2. **Define key terms precisely**:
   - **Random variable**: A quantity whose value is uncertain, described by a probability distribution
   - **Bayes' theorem**: P(s|o) = P(o|s)P(s)/P(o) -- the rule for updating beliefs given evidence
   - **Generative model**: The joint distribution P(o, s) = P(o|s)P(s) specifying how hidden states cause observations
   - **Hidden Markov Model (HMM)**: A dynamic generative model where states evolve over time and generate observations at each step
3. **Use concrete numerical examples**: Provide small-scale probability calculations (2-3 states, 2-3 observations) that students can verify by hand.
4. **Connect to previous courses**: The system, agent, and Markov blanket concepts from Cognitive Science now receive their mathematical formalization.

## Active Inference Integration

- The generative model P(o, s) is the mathematical core of Active Inference -- everything else derives from it
- Bayes' theorem is the ideal inference rule; variational inference (Module 02) approximates it when exact computation is intractable
- The HMM structure maps onto the POMDP framework used throughout the course

## Assessment Alignment

Questions should test the ability to:
- Apply Bayes' theorem to compute posterior probabilities in simple examples
- Write out the generative model P(o, s) for a given scenario
- Distinguish prior, likelihood, posterior, and evidence in a concrete problem

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
