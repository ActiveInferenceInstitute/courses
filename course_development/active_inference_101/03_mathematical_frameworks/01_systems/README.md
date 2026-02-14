# Module 01: Systems

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Probability and Generative Models

Part of **Mathematical Frameworks** -- this module establishes the probabilistic language of Active Inference, from random variables through Bayes' theorem to generative models.

## Learning Objectives

By the end of this module, students will be able to:

1. **Define** random variables, probability distributions, and the key operations (joint, marginal, conditional probability)
2. **Apply** Bayes' theorem to compute posterior probabilities in concrete numerical examples
3. **Construct** a generative model P(o, s) = P(o|s)P(s) for a given scenario, identifying prior, likelihood, and evidence
4. **Analyze** Hidden Markov Models as the dynamic extension of static generative models, adding temporal structure
5. **Evaluate** how the mathematical formalism of generative models formalizes the cognitive science concepts from Course 1

## Prerequisites

- Cognitive Science Modules 01-02 (conceptual understanding of systems and agents)
- Basic algebra and intuitive understanding of probability

## Key Concepts

- **Random variable**: A quantity whose value is uncertain, described by a probability distribution
- **Bayes' theorem**: P(s|o) = P(o|s)P(s)/P(o) -- the rule for updating beliefs given evidence
- **Generative model**: The joint distribution P(o, s) specifying how hidden states cause observations
- **Hidden Markov Model (HMM)**: A dynamic generative model with evolving hidden states generating observations over time
- **Prior, likelihood, posterior, evidence**: The four components of Bayesian inference

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Probability and Generative Models |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Computing Posterior Probabilities with Bayes' Theorem |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*, Chapter 2. Springer.
- MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 2. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
