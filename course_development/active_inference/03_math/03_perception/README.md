# Module 3: Perception — Variational Free Energy, KL Divergence, and Recognition Density

> **Quick Navigation**: [← Agents](../02_agents/) | [Up](../) | [Cognition →](../04_cognition/)

## The Mathematics of Active Inference

---

## Contents

| File | Description |
|------|-------------|
| [module.md](./module.md) | Full lecture content |
| [questions.md](./questions.md) | 20 study questions |
| [practice_quiz.md](./practice_quiz.md) | Quiz (7 MC + 3 FR) |
| [lab.md](./lab.md) | Derivation lab activity |
| [dashboard.html](./dashboard.html) | Interactive dashboard |

---

## Learning Objectives

By the end of this module, you should be able to:

1. **Derive** the Variational Free Energy `F` from `D_KL[q(s) || p(s|o)]` and show it upper-bounds surprisal (ELBO)
2. **Decompose** VFE into three equivalent forms: divergence + surprisal, complexity − accuracy, energy − entropy
3. **Compute** KL divergence for discrete and Gaussian distributions and prove its non-negativity via Jensen's inequality
4. **Apply** precision-weighted belief updating to hierarchical inference and predict convergence behavior

---

## Cross-Course Links

See this topic from other perspectives:

| Course | Focus |
|--------|-------|
| [Philosophy](../../01_philosophy/03_perception/) | Direct Perception, Inferentialism, and the User-Interface Theory |
| [Cognitive Science](../../02_cognitive_science/03_perception/) | Predictive Coding, Sensory Attenuation, and Hallucinations |
| [Mathematics](../../03_math/03_perception/) | Variational Free Energy, KL Divergence, and Recognition Density ← **You are here** |
| [Computer Science](../../04_computer_science/03_perception/) | A-Matrix and B-Matrix: Likelihood, Transitions, State Estimation |

---

## Resources

- [Notation Table](../../resources/notation_table.md) — Symbol definitions
- [Glossary](../../resources/glossary.md) — Term definitions
- [References](../../resources/references.md) — Key citations for this module

---

[← Agents](../02_agents/) | [Up](../) | [Cognition →](../04_cognition/)
