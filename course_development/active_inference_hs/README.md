# Active Inference for High School

> **Quick Navigation**: [Everyday Life](./01_everyday_life/) | [Biology & Health](./02_biology_health/) | [Math Foundations](./03_math_foundations/) | [Technology & AI](./04_technology_ai/) | [Resources](./resources/) | [Agent Guidelines](./AGENTS.md)

## Overview

A comprehensive, 4-course curriculum introducing **Active Inference** and the **Free Energy Principle (FEP)** for high school students (grades 9–12). Each course revisits the same 8 core topics from a different angle, creating a spiral learning experience that builds understanding with every pass.

> [!IMPORTANT]
> **Active Inference** is a powerful framework from brain science: it suggests that all living things are constant **prediction machines**. This curriculum translates these advanced concepts into relatable, hands-on lessons for the next generation of scientists and thinkers.

### Why This Matters

Active Inference provides a unified theory for understanding:

- **Perception**: Why what we see is a "controlled hallucination."
- **Action**: Why we explore the unknown even when it's risky.
- **Learning**: How we update our internal "maps" of the world.
- **Social Life**: How we synchronize our minds to communicate.

---

## Curriculum Statistics

| Metric | Value |
| --- | --- |
| **Courses** | 4 (Everyday Life → Biology & Health → Math Foundations → Technology & AI) |
| **Modules per Course** | 8 |
| **Total Modules** | 32 |
| **Files per Module** | 7 (module, questions, quiz, lab, dashboard, README, AGENTS) |
| **Total Content Files** | 248+ (modules + documentation + resources) |
| **Shared Resources** | 6 (notation table, glossary, references, cross-course map, learning pathways, FAQ) |
| **Grade Level** | 9–12 (adaptable for advanced 8th graders) |

---

## Courses

| # | Course | Focus | Prerequisites | Key Ideas |
|---|--------|-------|---------------|-----------|
| 1 | [Everyday Life](./01_everyday_life/) | Real-world intuition: predictions, habits, emotions, social life | None | Prediction, surprise, habits, social understanding |
| 2 | [Biology & Health](./02_biology_health/) | How your body and brain use prediction: neurons, stress, health | Course 1 | Neurons, homeostasis, stress response, mental health |
| 3 | [Math Foundations](./03_math_foundations/) | The math behind prediction: probability, Bayes' rule, optimization | Courses 1–2 | Probability, Bayes' theorem, matrices, optimization |
| 4 | [Technology & AI](./04_technology_ai/) | Building prediction machines: Python, simulations, AI agents | Courses 1–3 | Python coding, simulations, AI agents, chatbots |

---

## Core Topics (Consistent Across All Courses)

| Module | Topic | Everyday Life | Biology & Health | Math Foundations | Technology & AI |
|--------|-------|--------------|-----------------|-----------------|----------------|
| 1 | **Systems** | What makes a system? | Cells, organs, body systems | Sets, variables, and graphs | Inputs, outputs, and programs |
| 2 | **Agents** | Are you an agent? Is your dog? | Living things as prediction machines | Random variables and probability | Objects and classes in Python |
| 3 | **Perception** | Why you see what you expect | How neurons process sensory signals | Conditional probability | Sensors and data processing |
| 4 | **Cognition** | How your brain builds a world-model | Brain regions and mental models | Bayes' theorem | Data structures and models |
| 5 | **Action** | Why you do what you do | Motor control and reflexes | Optimization and expected value | Decision loops and if-statements |
| 6 | **Learning** | How you get better at things | Synaptic plasticity and memory | Updating estimates with data | Training loops and parameters |
| 7 | **Communication** | How we understand each other | Mirror neurons and empathy | Information theory basics | Multi-agent messaging |
| 8 | **Planning** | Thinking ahead: imagining futures | Executive function and goal-setting | Sequential decisions | Planning algorithms and games |

See [resources/cross_course_map.md](./resources/cross_course_map.md) for full cross-course navigation with direct links to every module.

---

## Learning Pathway

```text
                    ┌──────────────────────────────┐
                    │  1. Everyday Life              │
                    │  Big picture: What & Why       │
                    │  No prerequisites              │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  2. Biology & Health           │
                    │  Your body: How it works       │
                    │  Requires: Course 1            │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  3. Math Foundations           │
                    │  The math: Prove it            │
                    │  Requires: Courses 1-2         │
                    └──────────┬───────────────────┘
                               │
                    ┌──────────▼───────────────────┐
                    │  4. Technology & AI            │
                    │  Build it: Code it             │
                    │  Requires: Courses 1-3         │
                    └──────────────────────────────┘
```

Each course revisits the same 8 topics. By the end, students have seen Systems, Agents, Perception, Cognition, Action, Learning, Communication, and Planning from four different perspectives.

---

## Module Structure

Each module folder contains 7 files:

| File | Description | Format |
|------|-------------|--------|
| `module.md` | Full lesson content with learning objectives, key vocabulary, core concepts, examples, and references | 7 sections, ~100 lines |
| `questions.md` | 20 study questions (simple numbered list) | Numbered list, course-specific |
| `practice_quiz.md` | Part A: Multiple Choice (7 questions, A–D format) + Part B: Short Answer (3 questions) | Formal quiz format |
| `lab.md` | Multi-part structured lab with learning goals, `{fill:textarea}` fields, and summary table | Course-specific activity type |
| `dashboard.html` | Interactive HTML5 dashboard with concept cards, progress meters, and quiz | Dark theme, JS-powered |
| `README.md` | Module overview with cross-references and navigation | Standard navigation layout |
| `AGENTS.md` | Agent guidelines for content generation | Convention documentation |

### Lab Types by Course

| Course | Lab Type | Activity Style |
|--------|----------|---------------|
| Everyday Life | Group Activity | Discussions, real-world observations, reflection journals |
| Biology & Health | Investigation Lab | Case studies, data analysis, biological reasoning |
| Math Foundations | Guided Worksheet | Worked examples, fill-in derivations, graphing exercises |
| Technology & AI | Guided Coding Lab | Starter code, fill-in-the-blank coding, run-and-observe |

---

## Shared Resources

| Resource | Description |
|----------|-------------|
| [resources/notation_table.md](./resources/notation_table.md) | Key symbols explained in plain English with formal definitions |
| [resources/glossary.md](./resources/glossary.md) | 50+ terms with student-friendly definitions and per-course usage |
| [resources/references.md](./resources/references.md) | Curated references including videos, textbooks, and key papers |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | Complete cross-course navigation map for all 32 modules |
| [resources/learning_pathways.md](./resources/learning_pathways.md) | Suggested study orders by student interest and background |
| [resources/faq.md](./resources/faq.md) | Common questions about Active Inference for HS students and teachers |

---

## Design Principles

1. **Spiral Learning**: Each course revisits the same 8 topics at increasing depth and specificity.
2. **Accessibility First**: Course 1 starts with zero prerequisites — no math, no science background needed.
3. **Consistent Notation**: All mathematical symbols are defined once in [notation_table.md](./resources/notation_table.md).
4. **Consistent Terminology**: Preferred terms are defined in [glossary.md](./resources/glossary.md).
5. **Cross-References**: Every module links to its counterparts in all other courses.
6. **Real Content Only**: No mocks, stubs, or placeholder brackets in any file.
7. **NGSS Alignment**: Biology & Health course aligns with Next Generation Science Standards.
8. **Scaffolded Complexity**: Each course provides appropriate scaffolding for its grade level.

---

## Directory Map

```text
active_inference_hs/
├── README.md                          ← YOU ARE HERE
├── OVERVIEW.md                        → Curriculum overview, deep linking map
├── AGENTS.md                          → Agent guidelines, notation/terminology standards
├── audit_modules.sh                   → Structural audit script
├── resources/                         → Shared resources
│   ├── README.md                      → Resource directory overview
│   ├── AGENTS.md                      → Agent guidelines for resources
│   ├── notation_table.md             → Key symbols with HS-friendly explanations
│   ├── glossary.md                   → 50+ term definitions
│   ├── references.md                 → Curated references (videos, texts, papers)
│   ├── cross_course_map.md           → Cross-course navigation map
│   ├── learning_pathways.md          → Study orders by background
│   └── faq.md                        → Frequently asked questions
├── 01_everyday_life/                  → Course 1: Everyday Life (8 modules)
│   ├── README.md, AGENTS.md, syllabus.md
│   └── 01_systems/ ... 08_planning/  → Module directories
│       ├── module.md                  → Lesson content
│       ├── questions.md               → 20 study questions
│       ├── practice_quiz.md           → Part A (MC) + Part B (Short Answer)
│       ├── lab.md                     → Group Activity lab
│       ├── dashboard.html             → Interactive dashboard
│       └── README.md, AGENTS.md       → Module docs
├── 02_biology_health/                 → Course 2: Same structure (Investigation labs)
├── 03_math_foundations/               → Course 3: Same structure (Guided Worksheet labs)
└── 04_technology_ai/                  → Course 4: Same structure (Guided Coding labs)
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [AGENTS.md](./AGENTS.md) | Agent guidelines, conventions, notation, terminology, format standards |
| [resources/](./resources/) | Shared notation, glossary, references, cross-course map |
| [01_everyday_life/syllabus.md](./01_everyday_life/syllabus.md) | Everyday Life course syllabus |
| [02_biology_health/syllabus.md](./02_biology_health/syllabus.md) | Biology & Health course syllabus |
| [03_math_foundations/syllabus.md](./03_math_foundations/syllabus.md) | Math Foundations course syllabus |
| [04_technology_ai/syllabus.md](./04_technology_ai/syllabus.md) | Technology & AI course syllabus |

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-02-09 | Full 32-module HS curriculum with resources, syllabi, and shared notation |
