# Learning Pathways: Active Inference 101: College First Semester

> Suggested routes through the curriculum for College 1st semester undergraduates.
> Choose the pathway that best matches your background, goals, and available time.

## Overview

The Active Inference 101 curriculum consists of four parallel courses, each covering the same eight topics (Systems, Agents, Perception, Cognition, Action, Learning, Communication, Planning) from a different perspective:

| Course | Perspective | Best For Students Who |
| --- | --- | --- |
| 1. Cognitive Science | Mind, brain, behavior | Want to understand the "what" and "why" of Active Inference |
| 2. Computational Neuroscience | Neural circuits, dynamics | Want to understand the brain mechanisms |
| 3. Mathematical Frameworks | Probability, information theory | Want to understand the formal foundations |
| 4. Implementation & Simulation | Python, pymdp, coding | Want to build working agents |

---

## Pathway 1: Sequential (Recommended for Most Students)

Complete one course fully before starting the next. This builds understanding layer by layer.

**Sequence**: Cognitive Science -> Computational Neuroscience -> Mathematical Frameworks -> Implementation

```
Week 1-4:   Course 1 (Modules 1-8) -- Build conceptual foundation
Week 5-8:   Course 2 (Modules 1-8) -- Ground concepts in neural mechanisms
Week 9-12:  Course 3 (Modules 1-8) -- Formalize with mathematics
Week 13-16: Course 4 (Modules 1-8) -- Implement in code
```

**Advantages**: Each course provides context for the next. Concepts encountered in cognitive science become concrete in neuroscience, precise in mathematics, and executable in code.

**Best for**: Students new to Active Inference with no strong prior background in any single area.

---

## Pathway 2: Parallel (Comparative)

Study the same module topic across all four courses before moving to the next topic. This emphasizes connections between perspectives.

**Sequence**: For each module 1-8, read all four course versions.

```
Week 1-2:   Systems     (C1M1, C2M1, C3M1, C4M1)
Week 3-4:   Agents      (C1M2, C2M2, C3M2, C4M2)
Week 5-6:   Perception  (C1M3, C2M3, C3M3, C4M3)
Week 7-8:   Cognition   (C1M4, C2M4, C3M4, C4M4)
Week 9-10:  Action      (C1M5, C2M5, C3M5, C4M5)
Week 11-12: Learning    (C1M6, C2M6, C3M6, C4M6)
Week 13-14: Communication (C1M7, C2M7, C3M7, C4M7)
Week 15-16: Planning    (C1M8, C2M8, C3M8, C4M8)
```

**Advantages**: Deep understanding of each topic from multiple angles. Strong conceptual integration.

**Best for**: Students who prefer depth-first learning and can handle switching between perspectives frequently. Requires comfort with both informal and formal descriptions.

---

## Pathway 3: Interest-Driven

Start with whichever course matches your background, then explore connections using the cross-course map.

| Your Background | Start With | Then Try |
| --- | --- | --- |
| Psychology / Philosophy | Course 1 (Cognitive Science) | Course 2 -> Course 3 -> Course 4 |
| Biology / Pre-med | Course 2 (Comp. Neuroscience) | Course 1 -> Course 3 -> Course 4 |
| Mathematics / Physics | Course 3 (Math Frameworks) | Course 1 -> Course 2 -> Course 4 |
| Computer Science / Engineering | Course 4 (Implementation) | Course 3 -> Course 1 -> Course 2 |

**Advantages**: Builds on existing strengths and maintains motivation through familiar territory.

**Best for**: Students with strong prior background in one area who want to connect Active Inference to what they already know.

---

## Pathway 4: Essentials (Time-Limited)

For students who cannot complete all four courses, this pathway covers the minimum for a solid understanding.

**Core Modules** (complete all of these):

1. Course 1, Module 1 (Systems) -- Foundational concepts
2. Course 1, Module 2 (Agents) -- What is an agent?
3. Course 1, Module 3 (Perception) -- Predictive processing basics
4. Course 3, Module 4 (Cognition) -- Variational free energy (math)
5. Course 3, Module 5 (Action) -- Expected free energy (math)
6. Course 4, Module 1 (Systems) -- Setting up the toolkit
7. Course 4, Module 4 (Cognition) -- T-maze implementation
8. Course 4, Module 5 (Action) -- Policy selection implementation

**Advantages**: Covers the conceptual foundation, mathematical core, and a working implementation in 8 modules instead of 32.

**Best for**: Students auditing the course, those with time constraints, or those who want a quick overview before committing to a full pathway.

---

## Pathway 5: Research Preparation

For students intending to pursue Active Inference research.

**Phase 1** (Weeks 1-8): Complete Courses 1 and 3 in parallel (Pathway 2 style)
**Phase 2** (Weeks 9-12): Complete Course 4 with extra time on labs
**Phase 3** (Weeks 13-16): Complete Course 2, then revisit Course 3 labs with research-level depth

**Supplementary readings**: After each module, read the original papers listed in [references.md](./references.md) at the "Advanced" and "Specialist" levels.

**Best for**: Students considering graduate work in Active Inference, computational neuroscience, or related fields.

---

## Tips for All Pathways

- **Use the glossary** ([glossary.md](./glossary.md)) whenever you encounter unfamiliar terms
- **Use the notation table** ([notation_table.md](./notation_table.md)) to decode mathematical symbols
- **Use the cross-course map** ([cross_course_map.md](./cross_course_map.md)) to find related content in other courses
- **Complete labs and practice quizzes** -- active engagement is far more effective than passive reading
- **Revisit earlier modules** after completing later ones; your understanding will deepen

## Navigation

- [Cross-Course Map](./cross_course_map.md)
- [References](./references.md)
- [Glossary](./glossary.md)
- [Home](../README.md)
