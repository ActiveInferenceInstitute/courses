# The Mathematics of Active Inference — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Syllabus](./syllabus.md) | [Curriculum AGENTS](../AGENTS.md) | [Resources](../resources/)

## Overview

Agents working on this course (Mathematics) should approach all content from a **mathematical** perspective while maintaining consistency with the curriculum-wide notation, terminology, and format standards.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Course overview and navigation |
| `AGENTS.md` | File | This file — course-specific agent guidelines |
| `syllabus.md` | File | Full course syllabus with schedule and assessment |
| `01_systems/` | Directory | Module 1: Systems — Mathematical Foundations: Matrices, Probability, and Bayesian Reasoning |
| `02_agents/` | Directory | Module 2: Agents — Stochastic Systems: Random Processes, Differential Equations, and Steady States |
| `03_perception/` | Directory | Module 3: Perception — Variational Free Energy, KL Divergence, and Recognition Density |
| `04_cognition/` | Directory | Module 4: Cognition — Precision Matrices, Hierarchical Gaussian Filters, Message Passing |
| `05_action/` | Directory | Module 5: Action — Expected Free Energy (G): Risk and Ambiguity Decomposition |
| `06_learning/` | Directory | Module 6: Learning — Gradient Descent on VFE, Bayesian Model Reduction |
| `07_communication/` | Directory | Module 7: Communication — Generalized Synchrony, Mutual Information, Coupled Systems |
| `08_planning/` | Directory | Module 8: Planning — Recursive Belief Updating, Sophisticated Inference, Tree Search |

---

## Course-Specific Conventions

- **Perspective**: All content should be framed from a **mathematical** perspective.
- **Lab Type**: Labs use **Derivation Exercise** format — proof construction, equation manipulation, and worked examples.
- **Notation**: Use notation from [resources/notation_table.md](../resources/notation_table.md).
- **Terminology**: Use terms from [resources/glossary.md](../resources/glossary.md).
- **References**: Cite from [resources/references.md](../resources/references.md).

---

## Content Generation Standards

- All content uses **real methods** — no mocks, stubs, or placeholder implementations.
- Module content should be **modular, functional, and documented**.
- Questions must be **20 per module**, formatted as a simple numbered list.
- All 20 questions must reflect the **mathematical** perspective of this course.
- Quizzes must have **Part A: 7 multiple choice** + **Part B: 3 free response**.
- Labs must have **structured parts** with learning goals and `{fill:textarea}` fields.
- Lab summary tables must have **complete, untruncated** skill descriptions.
- Dashboards must be **interactive HTML5** with working JavaScript.
- Cross-references to parallel modules in other courses should use relative paths.

---

## Quality Checklist

Before considering any module complete in this course:

- [ ] Content reflects the **mathematical** perspective (not generic)
- [ ] All 7 files are present and substantive
- [ ] No placeholder brackets `[...]` remain
- [ ] Notation matches `resources/notation_table.md`
- [ ] Terms match `resources/glossary.md`
- [ ] Lab summary table is complete (not truncated)
- [ ] Quiz questions are answerable from the module lecture
- [ ] Cross-references use correct relative paths
