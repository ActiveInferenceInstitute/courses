# Module 4: Cognition — Precision Matrices, Hierarchical Gaussian Filters, Message Passing

> **Quick Navigation**: [← Perception](../03_perception/) | [Up](../) | [Action →](../05_action/)

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

1. **Derive** the precision-weighted prediction error update `dF/dμ = -dg/dμ Πε + prior terms` and connect it to the Kalman filter
2. **Formulate** the Hierarchical Gaussian Filter and its recursive precision estimation across levels
3. **Prove** that belief propagation on a factor graph implements coordinate ascent on VFE
4. **Analyze** how precision modulation affects convergence, attention, and the explore-exploit balance

---

## Cross-Course Links

See this topic from other perspectives:

| Course | Focus |
|--------|-------|
| [Philosophy](../../01_philosophy/04_cognition/) | Beliefs as Physical States, the Embodied Mind, and Predictive Processing |
| [Cognitive Science](../../02_cognitive_science/04_cognition/) | Attention as Precision Weighting and Working Memory |
| [Mathematics](../../03_math/04_cognition/) | Precision Matrices, Hierarchical Gaussian Filters, Message Passing ← **You are here** |
| [Computer Science](../../04_computer_science/04_cognition/) | C, D, E Matrices: Configuring Precision and Attention |

---

## Resources

- [Notation Table](../../resources/notation_table.md) — Symbol definitions
- [Glossary](../../resources/glossary.md) — Term definitions
- [References](../../resources/references.md) — Key citations for this module

---

[← Perception](../03_perception/) | [Up](../) | [Action →](../05_action/)
