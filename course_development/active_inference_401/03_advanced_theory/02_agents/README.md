# Module 02: Agents

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Information Geometry and Natural Gradients

Part of **Advanced Theory**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Information Geometry and Natural Gradients |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Statistical Manifolds and Natural Gradient Descent |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Analyze** the geometry of probability distributions as a Riemannian manifold: define the Fisher information metric g_ij(theta) = E[d_i ln p(x|theta) d_j ln p(x|theta)], prove it is positive semi-definite, and compute it for canonical exponential families
2. **Derive** the natural gradient as the steepest descent direction on the statistical manifold, proving that the natural gradient is F^{-1} nabla_theta L where F is the Fisher information matrix
3. **Evaluate** how Active Inference operates on curved statistical manifolds, showing that belief dynamics follow natural gradient flows and that this ensures reparameterization invariance of the inference process
4. **Examine** the consequences of information geometry for inference speed and stability: prove that natural gradient descent achieves Fisher efficiency and connect this to the asymptotic optimality of Active Inference

## Prerequisites

- Differential geometry (Riemannian metrics, geodesics, connections, curvature tensors)
- Mathematical statistics (Fisher information, Cramer-Rao bound, exponential families)
- Linear algebra at the level of matrix calculus and spectral theory

## Key References

- Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- Ay, N. et al. (2017). *Information Geometry*. Springer.
- Sakthivadivel, D. (2022). Towards a geometry and analysis for Bayesian mechanics. *arXiv:2204.11900*.
- Ollivier, Y. (2018). Online natural gradient as a Kalman filter. *Electronic Journal of Statistics*, 12(2), 2930--2961.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
