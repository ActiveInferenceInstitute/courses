# Module 02: Agents

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Variational Inference and the Recognition Model

Part of **Mathematical Frameworks** -- this module introduces variational inference as the tractable approximation to exact Bayesian inference that defines agency.

## Learning Objectives

By the end of this module, students will be able to:

1. **Explain** why exact Bayesian inference is often intractable and how variational inference provides an approximation
2. **Compute** KL divergence between two simple probability distributions by hand
3. **Derive** the relationship between variational free energy, accuracy, and complexity (F = -Accuracy + Complexity)
4. **Analyze** the Evidence Lower Bound (ELBO) and its equivalence to negative free energy
5. **Evaluate** the mean-field approximation as a simplifying assumption for the recognition model q(s)

## Prerequisites

- Mathematical Frameworks Module 01: Systems (probability, Bayes' theorem, generative models)

## Key Concepts

- **Recognition model q(s)**: The approximate posterior -- the agent's tractable estimate of hidden states
- **KL divergence D_KL(q||p)**: Information-theoretic distance between two distributions; always >= 0
- **Evidence Lower Bound (ELBO)**: The quantity maximized in variational inference, equivalent to -F
- **Variational free energy F**: The quantity minimized by agents; F = Energy - Entropy = -Accuracy + Complexity
- **Mean-field approximation**: Assuming the posterior factorizes into independent components

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Variational Inference and the Recognition Model |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Computing Free Energy and KL Divergence |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Recommended Readings

- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapter 3. MIT Press.
- Blei, D. M. et al. (2017). Variational inference: A review for statisticians. *JASA*, 112(518), 859-877.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
