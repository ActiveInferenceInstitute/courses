# Active Inference for Middle School — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Real Life Skills](./01_real_life_skills/) | [Body Science](./02_body_science/) | [Math Detectives](./03_math_detectives/) | [Code & Create](./04_code_create/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for middle school students (grades 6-8) with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain consistency in terminology, notation, and pedagogical structure while keeping content relatable, engaging, and connected to real-life experiences.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_real_life_skills/` | Directory | Unit 1: Real Life Skills — Active Inference in Daily Life (8 modules) |
| `02_body_science/` | Directory | Unit 2: Body Science — How Your Body Predicts (8 modules) |
| `03_math_detectives/` | Directory | Unit 3: Math Detectives — Patterns and Probability (8 modules) |
| `04_code_create/` | Directory | Unit 4: Code & Create — Building Smart Systems (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any math or symbols |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, accurate content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Real Life Skills | Everyday intuition | Group Challenge | "Why does your phone's autocorrect sometimes guess wrong? What prediction did it make?" |
| Body Science | Biological mechanisms | Investigation Lab | "Test your reaction time — how does your brain predict when to catch a ball?" |
| Math Detectives | Pattern recognition & probability | Guided Worksheet | "Flip a coin 20 times. How close is your result to 50/50?" |
| Code & Create | Block coding & simple programming | Guided Coding Lab | "Use Scratch to build a creature that learns to avoid obstacles" |

### 4. Write for Middle School Students (Grades 6-8)

- Use relatable, real-world examples (social media, phones, sports, school)
- Be curious and slightly irreverent — match the energy of a 12-year-old
- Light math only: fractions, percentages, basic probability, ratios
- Introduce coding through block-based tools (Scratch) before text-based
- Define technical terms with everyday parallels
- Use "you" and direct questions to keep engagement high

---

## Notation Standards

All units use the notation defined in [resources/notation_table.md](./resources/notation_table.md). Key concepts:

| Symbol/Concept | Kid-Friendly Version | Formal Meaning |
|---------------|---------------------|----------------|
| Probability (%) | "How likely is it?" | P(event) expressed as percentage |
| 50/50 | "Equal chance either way" | P = 0.5 |
| Prediction | "Your brain's best guess" | Expected value from generative model |
| Prediction error | "When your guess is wrong" | Difference between predicted and actual observation |
| Feedback loop | "When the result changes your next guess" | Recursive model updating |
| Pattern | "Something that repeats in a predictable way" | Statistical regularity |

---

## Terminology Standards

| Preferred Term | Simpler Alternative Used First | Formal Meaning |
|----------------|-------------------------------|----------------|
| Generative Model | Brain's prediction machine | Internal model that generates predictions |
| Prediction Error | Being wrong (and that's OK!) | Mismatch between expected and actual input |
| Markov Blanket | System boundary, bubble | Statistical boundary separating inside from outside |
| Precision | How sure you are | Inverse variance — weight on a signal |
| Free Energy | Overall wrongness score | Variational free energy (upper bound on surprisal) |
| Policy | Game plan, strategy | Sequence of actions |
| Epistemic | "Finding out" | Related to gaining information |
| Pragmatic | "Getting what you want" | Related to achieving goals |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Middle school version of the dependency chain:
- What's a system? (Systems) → What makes you an agent? (Agents) → How do you notice stuff? (Perception) → How does your brain figure things out? (Cognition) → What do you decide to do? (Action) → How do you get better at stuff? (Learning) → How do you share what you know? (Communication) → How do you make plans? (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Hook/Introduction → Learning Objectives → Key Vocabulary → Core Concepts (5 subsections with real-life examples) → Try This → Summary → References |
| `questions.md` | `# Course — Module — Study Questions` + simple numbered list (15-20 questions). Mix of factual and "what do you think?" |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Short Answer` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → `<!-- lab:reflection -->` / `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#2dd4bf` teal accent), concept cards with progress meters, quiz with JS answer checking |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_real_life_skills/03_perception/module.md to the body science version: -->
See [How Your Body Predicts](../../02_body_science/03_perception/module.md) for the science behind how your brain senses things.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- From any module to the root README: -->
See the [Curriculum Overview](../../README.md) for the full course map.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Language is appropriate for grades 6-8
- [ ] Examples are relatable (phones, social media, sports, school life)
- [ ] Math uses only fractions, percentages, basic probability
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions mix factual recall with "what do you think?" prompts
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 questions
- [ ] Lab is hands-on and collaborative
- [ ] Content is engaging — would a 12-year-old stay interested?

---

## Dashboard Color Identity

- **Accent**: Teal `#2dd4bf`
- **Gradient**: Teal → Blue
- **Semantic**: Curious, explorative
