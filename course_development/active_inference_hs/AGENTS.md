# Active Inference for High School — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Everyday Life](./01_everyday_life/) | [Biology & Health](./02_biology_health/) | [Math Foundations](./03_math_foundations/) | [Technology & AI](./04_technology_ai/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-course Active Inference curriculum for high school students with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain consistency in terminology, notation, and pedagogical structure across all courses while keeping content accessible for grades 9–12.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_everyday_life/` | Directory | Course 1: Everyday Life & Active Inference (8 modules) |
| `02_biology_health/` | Directory | Course 2: Biology, Health & Active Inference (8 modules) |
| `03_math_foundations/` | Directory | Course 3: The Math Behind Active Inference (8 modules) |
| `04_technology_ai/` | Directory | Course 4: Technology, AI & Active Inference (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any formula, symbol, or equation |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references between courses |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, accurate content.

### 3. Maintain Course-Specific Perspectives

| Course | Perspective | Lab Type | Example Content |
|--------|------------|----------|----------------|
| Everyday Life | Real-world intuition | Group Activity | "Think about a time you were surprised. What prediction did your brain make?" |
| Biology & Health | Biological mechanisms | Investigation Lab | "How does your pupil dilate in response to prediction errors?" |
| Math Foundations | Mathematical reasoning | Guided Worksheet | "Calculate P(rain \| clouds) using Bayes' theorem" |
| Technology & AI | Computational thinking | Guided Coding Lab | "Write a Python function that updates beliefs using new evidence" |

### 4. Write for High School Students

- Use everyday language first, then introduce technical terms
- Define every technical word when it first appears
- Use concrete examples before abstract concepts
- Keep sentences short and paragraphs focused
- Avoid assuming prerequisite knowledge beyond what previous modules cover

---

## Notation Standards

All courses use the notation defined in [resources/notation_table.md](./resources/notation_table.md). Key symbols:

| Symbol | Plain English | Formal Meaning |
|--------|--------------|----------------|
| `P(A)` | How likely is A? | Probability of event A |
| `P(A\|B)` | How likely is A, given B happened? | Conditional probability |
| `F` | Prediction error (overall) | Variational Free Energy |
| `G` | What will happen next? | Expected Free Energy |
| **A** | How observations relate to hidden states | Likelihood matrix |
| **B** | How states change over time | Transition matrix |
| **C** | What the agent prefers | Preference vector |
| **D** | What the agent initially believes | Prior beliefs |

---

## Terminology Standards

| Preferred Term | Simpler Alternative Used First | Formal Meaning |
|----------------|-------------------------------|----------------|
| Generative Model | Mental model, brain's model | The brain's internal model of how the world works |
| Prediction Error | Surprise | Difference between what was expected and what happened |
| Markov Blanket | Boundary, border | The statistical boundary between a system and its environment |
| Precision | Confidence, certainty | How much weight you put on a signal (inverse of noise) |
| Variational Free Energy (VFE) | Overall prediction error | A measure of how wrong your predictions are |
| Expected Free Energy (EFE) | Future prediction error | A measure of how wrong your predictions will be |
| Policy | Plan, strategy | A sequence of actions |
| Epistemic Value | Curiosity, exploration | The value of gaining information |
| Pragmatic Value | Usefulness, reward | The value of achieving a goal |

---

## Topic Order Convention

All 4 courses follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

This order reflects a logical progression:

- Systems (what things are) → Agents (which things act) → Perception (how they sense) → Cognition (how they think) → Action (how they act) → Learning (how they improve) → Communication (how they interact) → Planning (how they think ahead)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Introduction → Learning Objectives → Key Vocabulary → Core Concepts (5 subsections) → Examples → Summary → References |
| `questions.md` | `# Course — Module — Study Questions` + simple numbered list (20 questions). No section headers within the list. |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions, `**1.**` numbering, `A) ... B) ...` format) → `Part B: Short Answer` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → `<!-- lab:reflection -->` / `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme, concept cards with progress meters, quiz with JS answer checking, animated transitions |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between courses, use relative paths:

```markdown
<!-- From 01_everyday_life/03_perception/module.md to the biology version: -->
See [Perception in Biology & Health](../../02_biology_health/03_perception/module.md) for how neurons handle prediction.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- From any module to the root README: -->
See the [Curriculum Overview](../../README.md) for the full course map.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Language is appropriate for high school students (grades 9–12)
- [ ] No placeholder brackets `[...]` remain
- [ ] All notation matches `resources/notation_table.md`
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Questions are course-specific (not generic)
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 short answer questions
- [ ] Lab has structured parts with learning goals and `{fill:textarea}` fields
- [ ] Summary table in lab is complete

---

## Dashboard Color Identity

- **Accent**: Indigo `#818cf8`
- **Gradient**: Indigo → Violet
- **Semantic**: Energetic, youthful, aspirational
