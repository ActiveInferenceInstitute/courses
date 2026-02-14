# Module 06: Learning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Bayesian Model Selection and Structure Learning

Part of **Advanced Theory**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Bayesian Model Selection and Structure Learning |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Model Evidence Computation and Structure Discovery |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Derive** Bayesian Model Selection from first principles: starting from the marginal likelihood p(o|m) = integral p(o|s, m) p(s|m) ds, prove that model evidence naturally balances accuracy against complexity (the Occam factor)
2. **Analyze** Bayesian Model Reduction (BMR) as a computationally efficient method for pruning model parameters, deriving the closed-form expression for the change in log model evidence when parameters are removed under Laplace approximation
3. **Formalize** structure learning as discovering the topology of the generative model (which variables exist, which connections are present), showing how BMR enables exhaustive search over nested model spaces without refitting
4. **Evaluate** the relationship between BMR, minimum description length (MDL), and variational model selection, proving equivalences and characterizing the conditions under which each approach is appropriate

## Prerequisites

- Bayesian statistics (marginal likelihood, Bayes factors, Laplace approximation, BIC/AIC)
- Model selection theory (cross-validation, information criteria, minimum description length)
- Linear algebra (matrix inversion lemma, Woodbury identity, determinant identities)

## Key References

- Friston, K. & Penny, W. (2011). Post hoc Bayesian model selection. *NeuroImage*, 56(4), 2089--2099.
- Friston, K. J. et al. (2018). Bayesian model reduction. *arXiv:1805.07092*.
- Schwarz, G. (1978). Estimating the dimension of a model. *Annals of Statistics*, 6(2), 461--464.
- Grunwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
