# Learning Pathways

> **Quick Navigation**: [Curriculum Home](../README.md) | [Notation Table](./notation_table.md) | [Glossary](./glossary.md) | [References](./references.md) | [Cross-Course Map](./cross_course_map.md)

Suggested pathways through the Active Inference curriculum based on your background and goals. The curriculum consists of 4 courses × 8 modules, all covering the same 8 topics from different disciplinary angles.

---

## Prerequisite Chain

```text
Course 1: Philosophy ──→ Course 2: Cognitive Science ──→ Course 3: Mathematics ──→ Course 4: Computer Science
                                                              ↑                           ↑
                                                              │                           │
                                                     Requires calculus,          Requires Python,
                                                     linear algebra basics       NumPy, basic OOP
```

Courses are designed to be taken in order. Each builds on concepts introduced in the previous course.

---

## Pathway by Background

### Philosophy / Humanities Background

| Phase | Courses | Rationale |
|-------|---------|-----------|
| Start here | Course 1 (Philosophy) | Builds on existing philosophical training |
| Then | Course 2 (Cognitive Science) | Empirical grounding for philosophical concepts |
| Supplement | [notation_table.md](./notation_table.md) Sections 1-3 | Learn the mathematical notation at your own pace |
| When ready | Course 3 (Mathematics) Modules 1-2 | Build formal foundations before full derivations |
| Optional | Course 4 (Computer Science) | Computational implementation |

### Cognitive Science / Neuroscience Background

| Phase | Courses | Rationale |
|-------|---------|-----------|
| Start here | Course 2 (Cognitive Science) | Connects FEP to familiar neural mechanisms |
| Then | Course 1 (Philosophy) | Deepens understanding of conceptual foundations |
| Next | Course 3 (Mathematics) | Formalize the intuitions from CogSci |
| Finally | Course 4 (Computer Science) | Implement what you've learned |

### Mathematics / Physics Background

| Phase | Courses | Rationale |
|-------|---------|-----------|
| Start here | Course 3 (Mathematics) | Engage with the formalism directly |
| Supplement | Course 1, Module 1-3 | Philosophical context for the math |
| Then | Course 4 (Computer Science) | Implement the equations you've derived |
| Deepen | Course 2 (Cognitive Science) | See how the math maps to neural data |

### Computer Science / ML Background

| Phase | Courses | Rationale |
|-------|---------|-----------|
| Start here | Course 4 (Computer Science) Module 1-3 | Hands-on agent building |
| Supplement | Course 3 (Mathematics) Modules 3-5 | Understand VFE, EFE derivations behind the code |
| Broaden | Course 1 (Philosophy) | Conceptual foundations and implications |
| Deepen | Full Course 3, then Course 4 Modules 4-8 | Complete formal + computational mastery |

---

## Module Dependency Graph

Within each course, modules build on each other:

```text
M1: Systems ──→ M2: Agents ──→ M3: Perception ──→ M4: Cognition
                                                        │
                                                        ↓
                M8: Planning ←── M7: Communication ←── M6: Learning ←── M5: Action
```

- **M1-M2**: Foundation — what is a system, what is an agent
- **M3-M4**: Perception and cognition — how agents model the world
- **M5-M6**: Action and learning — how agents act and adapt
- **M7-M8**: Communication and planning — multi-agent and temporal extensions

---

## Cross-Course Deep Dives

For a deep understanding of a single topic, study the corresponding module across all four courses:

| Topic | Pathway | Key Insight |
|-------|---------|-------------|
| Perception | Phil M3 → CogSci M3 → Math M3 → CS M3 | From "what is perception?" to implementing belief updates |
| Action | Phil M5 → CogSci M5 → Math M5 → CS M5 | From affordances to EFE computation |
| Learning | Phil M6 → CogSci M6 → Math M6 → CS M6 | From epistemic growth to Dirichlet updates |
| Planning | Phil M8 → CogSci M8 → Math M8 → CS M8 | From teleology to deep temporal models |

See [cross_course_map.md](./cross_course_map.md) for full details on all 8 cross-course pathways.
