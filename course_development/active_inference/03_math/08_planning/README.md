# Module 8: Planning — Recursive Belief Updating, Sophisticated Inference, Tree Search

> **Quick Navigation**: [← Communication](../07_communication/) | [Up](../) | [Course Home →](../)

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

1. **Derive** the recursive EFE for deep policies `G(π) = Σ G_τ(π)` with forward belief propagation through transition matrices
2. **Formulate** the sophisticated inference recursion and prove it subsumes naive EFE evaluation as a special case
3. **Analyze** the computational complexity of policy tree evaluation as `O(|A|^T)` and derive speedups from beam search and E-vector pruning
4. **Apply** temporal abstraction to reduce planning complexity from `O(|A|^{T_H·T_L})` to `O(|A_H|^{T_H} + T_H|A_L|^{T_L})`

---

## Cross-Course Links

See this topic from other perspectives:

| Course | Focus |
|--------|-------|
| [Philosophy](../../01_philosophy/08_planning/) | Teleology, Future-Oriented Behavior, and the Phenomenology of Time |
| [Cognitive Science](../../02_cognitive_science/08_planning/) | Executive Function and Decision Making Under Uncertainty |
| [Mathematics](../../03_math/08_planning/) | Recursive Belief Updating, Sophisticated Inference, Tree Search ← **You are here** |
| [Computer Science](../../04_computer_science/08_planning/) | Deep Temporal Models: T-Mazes and Gridworlds |

---

## Resources

- [Notation Table](../../resources/notation_table.md) — Symbol definitions
- [Glossary](../../resources/glossary.md) — Term definitions
- [References](../../resources/references.md) — Key citations for this module

---

[← Communication](../07_communication/) | [Up](../) | [Course Home →](../)
