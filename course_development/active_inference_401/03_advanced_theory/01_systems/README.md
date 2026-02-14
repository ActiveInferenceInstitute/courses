# Module 01: Systems

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Variational Calculus and the Free Energy Functional

Part of **Advanced Theory**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Variational Calculus and the Free Energy Functional |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Deriving and Decomposing the Free Energy Functional |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Derive** the free energy functional F[q] = E_q[ln q(s) - ln p(o, s)] from first principles using variational calculus, proving that it constitutes an upper bound on negative log model evidence -ln p(o)
2. **Analyze** the mathematical decomposition of variational free energy into energy minus entropy, and equivalently into complexity (D_KL[q(s) || p(s)]) plus inaccuracy (-E_q[ln p(o|s)]), interpreting each term's role in inference
3. **Prove** the conditions under which free energy minimization is equivalent to exact Bayesian inference (namely, when the variational family is sufficiently expressive to contain the true posterior)
4. **Generalize** the variational framework to expected free energy G(pi) = E_q[ln q(s_tau|pi) - ln p(o_tau, s_tau|pi)], deriving its decomposition into pragmatic value and epistemic value (information gain)

## Prerequisites

- Graduate-level variational calculus (Euler-Lagrange equations, functional derivatives, stationary conditions)
- Measure-theoretic probability (KL divergence, absolute continuity, Radon-Nikodym theorem)
- Familiarity with exponential family distributions and their sufficient statistics

## Key References

- Friston, K. (2019). A free energy principle for a particular physics. *arXiv:1906.10184*.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press, chapters 4--6.
- Wainwright, M. J. & Jordan, M. I. (2008). Graphical models, exponential families, and variational inference. *Foundations and Trends in Machine Learning*, 1(1--2), 1--305.
- Beal, M. J. (2003). *Variational Algorithms for Approximate Bayesian Inference*. PhD thesis, UCL.

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
