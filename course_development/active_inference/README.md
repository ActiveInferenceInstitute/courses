# Active Inference Curriculum

> **Quick Navigation**: [Philosophy](./01_philosophy/) | [Cognitive Science](./02_cognitive_science/) | [Mathematics](./03_math/) | [Computer Science](./04_computer_science/) | [Resources](./resources/) | [Agent Guidelines](./AGENTS.md)

## Overview

A comprehensive, 4-course curriculum on **Active Inference** and the **Free Energy Principle (FEP)**. Each course revisits the same 8 core topics from a different disciplinary lens, creating a spiral learning experience that deepens understanding with each pass. A shared `resources/` directory provides the canonical notation, glossary, references, and cross-course map used by all courses.

Active Inference is a unifying framework from theoretical neuroscience that casts perception, action, learning, and planning as forms of approximate Bayesian inference. Originally proposed by Karl Friston, it has expanded into philosophy of mind, cognitive science, robotics, and artificial intelligence. This curriculum provides a comprehensive, multi-perspective introduction.

---

## Curriculum Statistics

| Metric | Value |
|--------|-------|
| **Courses** | 4 (Philosophy → CogSci → Math → CS) |
| **Modules per Course** | 8 |
| **Total Modules** | 32 |
| **Files per Module** | 7 (module, questions, quiz, lab, dashboard, README, AGENTS) |
| **Total Content Files** | 224+ (modules + documentation + resources) |
| **Shared Resources** | 6 (notation table, glossary, references, cross-course map, learning pathways, FAQ) |
| **Total References** | 82 canonical citations |
| **Glossary Terms** | 65+ definitions with per-course usage |

---

## Courses

| # | Course | Focus | Prerequisites | Key Thinkers |
|---|--------|-------|---------------|-------------|
| 1 | [Philosophy](./01_philosophy/) | Philosophical foundations: pragmatism, phenomenology, enactivism, 4E cognition | None | Friston, Merleau-Ponty, Varela, Clark, Hohwy |
| 2 | [Cognitive Science](./02_cognitive_science/) | Neural and behavioral science: predictive coding, plasticity, clinical applications | Course 1 | Rao & Ballard, Seth, Feldman, Adams |
| 3 | [Mathematics](./03_math/) | Formal definitions and derivations: VFE, EFE, Langevin dynamics, BMR | Courses 1-2 | Friston, Da Costa, Parr, Pezzulo |
| 4 | [Computer Science](./04_computer_science/) | Python implementation: custom `active_inference` library (agent/, math/, visualization/), simulations, multi-agent | Courses 1-3 | Heins, Sajid, Smith |

---

## Core Topics (Consistent Across All Courses)

| Module | Topic | Philosophy | CogSci | Math | CS |
|--------|-------|------------|--------|------|-----|
| 1 | **Systems** | Markov Blankets & boundaries | Neural assemblies & integration | Mathematical foundations & Bayesian reasoning | Generative process vs model |
| 2 | **Agents** | Autopoiesis & agency | Self-model & interoception | Stochastic systems & Fokker-Planck | Agent class in pymdp |
| 3 | **Perception** | Inferentialism & user-interface theory | Predictive coding & hallucination | VFE, KL divergence, recognition density | A-matrix & B-matrix |
| 4 | **Cognition** | Embodied mind & belief | Precision weighting & attention | Precision matrices & message passing | C, D, E matrices |
| 5 | **Action** | Affordances & epistemic action | Motor control & habits | EFE (G): risk & ambiguity | Policy selection |
| 6 | **Learning** | Epistemic growth & niche construction | Synaptic plasticity & dopamine | Gradient descent & BMR | Parameter learning (pA, pB) |
| 7 | **Communication** | Intersubjectivity & alignment | Theory of Mind & social cognition | Generalized synchrony & MI | Multi-agent simulations |
| 8 | **Planning** | Teleology & phenomenology of time | Executive function & prospection | Recursive & sophisticated inference | Deep temporal models |

See [resources/cross_course_map.md](./resources/cross_course_map.md) for full cross-course navigation with direct links to every module.

---

## Learning Pathway

```text
                    ┌──────────────────────────────┐
                    │  1. Philosophy                │
                    │  Big picture: What & Why      │
                    │  No prerequisites              │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  2. Cognitive Science         │
                    │  Neural implementation: How    │
                    │  Requires: Course 1            │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  3. Mathematics               │
                    │  Formal derivation: Prove it   │
                    │  Requires: Courses 1-2         │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  4. Computer Science          │
                    │  Implementation: Build it      │
                    │  Requires: Courses 1-3         │
                    └──────────────────────────────┘
```

Each course revisits the same 8 topics. By the end, students have seen Systems, Agents, Perception, Cognition, Action, Learning, Communication, and Planning from four complementary angles.

---

## Module Structure

Each module folder contains 7 files:

| File | Description | Format |
|------|-------------|--------|
| `module.md` | Full lecture content with learning objectives, key terms, core concepts, examples, and references | 7 sections, ~90 lines |
| `questions.md` | 20 study questions (biol-1 format: simple numbered list) | Numbered list, course-specific |
| `practice_quiz.md` | Part A: Multiple Choice (7 questions, A-D format) + Part B: Free Response (3 questions) | Formal quiz format |
| `lab.md` | Multi-part structured lab with learning goals, `{fill:textarea}` fields, and summary table | Course-specific activity type |
| `dashboard.html` | Interactive HTML5 dashboard with concept cards, progress meters, and quiz | Dark theme, JS-powered |
| `README.md` | Module overview with cross-references and navigation | Standard navigation layout |
| `AGENTS.md` | Agent guidelines for content generation | Convention documentation |

### Lab Types by Course

| Course | Lab Type | Activity Style |
|--------|----------|---------------|
| Philosophy | Thought Experiment | Philosophical argumentation, reading analysis, position papers |
| Cognitive Science | Case Study Analysis | Clinical cases, experimental data interpretation, neural correlate mapping |
| Mathematics | Derivation Exercise | Proof construction, equation manipulation, worked examples |
| Computer Science | Coding Lab | pymdp implementation, simulation, visualization |

---

## Shared Resources

| Resource | Description |
|----------|-------------|
| [resources/notation_table.md](./resources/notation_table.md) | Canonical notation: `F`, `G`, `π`, `A-E` matrices, Markov Blanket partition (`η, μ, σ, α`), information-theoretic quantities, VFE/EFE decompositions, temporal notation, conventions |
| [resources/glossary.md](./resources/glossary.md) | 50+ terms with canonical definitions, per-course usage table, alphabetical organization |
| [resources/references.md](./resources/references.md) | 82 canonical citations organized by module topic, foundational texts, software tools, supplementary philosophy references |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | Complete cross-course navigation map with subtitles, key concepts, and directory links for all 32 modules |
| [resources/learning_pathways.md](./resources/learning_pathways.md) | Suggested study orders by background, module dependencies, cross-course deep dives |
| [resources/faq.md](./resources/faq.md) | Common questions about Active Inference and this curriculum with module links |

---

## Design Principles

1. **Spiral Learning**: Each course revisits the same 8 topics at increasing depth and specificity.
2. **Consistent Notation**: All mathematical symbols are defined once in [notation_table.md](./resources/notation_table.md).
3. **Consistent Terminology**: Preferred terms are defined in [glossary.md](./resources/glossary.md).
4. **Cross-References**: Every module links to its counterparts in all other courses.
5. **Incremental Onboarding**: The philosophy course (Course 1) starts with big-picture concepts accessible to all learners, progressively introducing technical detail.
6. **biol-1 Format Compliance**: All content files follow the formatting conventions from `biol-1/course`.
7. **Real Content Only**: No mocks, stubs, or placeholder brackets in any file.

---

## Directory Map

```text
active_inference/
├── README.md                          ← YOU ARE HERE
├── OVERVIEW.md                        → Curriculum overview, deep linking map
├── AGENTS.md                          → Agent guidelines, notation/terminology standards
├── audit_modules.sh                   → Structural audit (sections, refs, cross-refs)
├── resources/                         → Shared resources
│   ├── README.md                      → Resource directory overview
│   ├── AGENTS.md                      → Agent guidelines for resources
│   ├── notation_table.md             → Canonical notation (180+ lines)
│   ├── glossary.md                   → 65+ term definitions
│   ├── references.md                 → 82 canonical citations
│   ├── cross_course_map.md           → Cross-course navigation map
│   ├── learning_pathways.md          → Study orders by background
│   └── faq.md                        → Frequently asked questions
├── 01_philosophy/                     → Course 1: Philosophy (8 modules)
│   ├── README.md, AGENTS.md, syllabus.md
│   └── 01_systems/ ... 08_planning/  → Module directories
│       ├── module.md                  → Lecture content
│       ├── questions.md               → 20 study questions
│       ├── practice_quiz.md           → Part A (MC) + Part B (FR)
│       ├── lab.md                     → Thought experiment lab
│       ├── dashboard.html             → Interactive dashboard
│       └── README.md, AGENTS.md       → Module docs
├── 02_cognitive_science/              → Course 2: Same structure (Case study labs)
├── 03_math/                           → Course 3: Same structure (Derivation labs)
└── 04_computer_science/               → Course 4: Same structure (Coding labs)
    ├── src/active_inference/           → Custom Python library (v0.4.0)
    │   ├── agent/                     → GenerativeModel, Agent, Environment
    │   ├── math/                      → free_energy, inference, learning
    │   └── visualization/             → plotting utilities
    └── tests/                         → 253 passing tests, 100% coverage
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [AGENTS.md](./AGENTS.md) | Agent guidelines, conventions, notation, terminology, format standards |
| [resources/](./resources/) | Shared notation, glossary, references, cross-course map |
| [01_philosophy/syllabus.md](./01_philosophy/syllabus.md) | Philosophy course syllabus with schedule and assessment |
| [02_cognitive_science/syllabus.md](./02_cognitive_science/syllabus.md) | Cognitive Science course syllabus |
| [03_math/syllabus.md](./03_math/syllabus.md) | Mathematics course syllabus |
| [04_computer_science/syllabus.md](./04_computer_science/syllabus.md) | Computer Science course syllabus |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 0.4.0 | 2026-02-08 | CS course: 253/253 tests passing, 100% coverage (1,250 stmts), zero mocks, full method-level audit |
| 0.3.0 | 2026-02-07 | CS course: subpackage reorganization (agent/, math/, visualization/), removed all backwards-compat shims |
| 0.2.0 | 2026-02-07 | Full 32-module curriculum with resources, syllabi, and shared notation |
| 0.1.0 | 2026-02-07 | Initial curriculum structure and course scaffolding |
