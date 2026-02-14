# Active Inference for Elementary School — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Story Time](./01_story_time/) | [Our Bodies](./02_our_bodies/) | [Counting & Patterns](./03_counting_patterns/) | [Robots & Helpers](./04_robots_helpers/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for elementary school students (grades K-5) with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain consistency in terminology and pedagogical structure while keeping all content age-appropriate, joyful, and grounded in play.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_story_time/` | Directory | Unit 1: Story Time — Learning Through Tales (8 modules) |
| `02_our_bodies/` | Directory | Unit 2: Our Bodies — Senses and Feelings (8 modules) |
| `03_counting_patterns/` | Directory | Unit 3: Counting & Patterns — Numbers in Nature (8 modules) |
| `04_robots_helpers/` | Directory | Unit 4: Robots & Helpers — Machines That Learn (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before using any symbols or simple math |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any concept |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, age-appropriate content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Story Time | Narrative & imagination | Storytime Activity | "Once upon a time, a little fish had to guess where the food was hiding..." |
| Our Bodies | Senses & feelings | Drawing & Coloring Lab | "Draw what happens when you touch something hot — what does your hand do?" |
| Counting & Patterns | Numbers & patterns | Hands-On Puzzle | "Count the petals on three flowers. Do you see a pattern?" |
| Robots & Helpers | Machines & helping | Build & Play | "Build a simple robot arm from cardboard that can pick up a cotton ball" |

### 4. Write for Elementary School Students (K-5)

- Use short, simple sentences (grade-level readability)
- **No formulas, no equations, no Greek letters**
- Use stories, animals, characters, and everyday scenarios
- Every concept gets a concrete, physical example first
- Use "you," "we," and direct address
- Include drawing, coloring, and movement activities
- Make it fun — wonder, surprise, and discovery are the primary pedagogical tools

---

## Notation Standards

This curriculum uses **minimal notation** — almost everything is in plain language. Key concepts:

| Concept | Kid-Friendly Version | What It Really Means |
|---------|---------------------|---------------------|
| System | "A group of things that work together" | A set of interacting elements with a boundary |
| Agent | "Something that can make choices" | A system that acts to minimize surprise |
| Prediction | "A guess about what will happen" | The brain's expectation about incoming sensory data |
| Surprise | "When something unexpected happens" | Prediction error (mismatch between expected and actual) |
| Learning | "Getting better at guessing" | Updating the generative model to reduce future prediction error |
| Boundary | "The edge of something — where it starts and stops" | Markov blanket |

---

## Terminology Standards

| Preferred Kid-Friendly Term | What It Maps To (FEP) | Usage Rule |
|----------------------------|----------------------|------------|
| Guess / Prediction | Generative model output | Always say "guess" first, then "prediction" |
| Surprise | Prediction error | Use "surprise" — never "surprisal" or "free energy" |
| Boundary | Markov blanket | Use "boundary" or "edge" — never "Markov blanket" |
| Senses | Sensory states | "What you see, hear, feel, taste, smell" |
| Choices | Policies / actions | "What you decide to do" |
| Getting better | Learning / model updating | "When your guesses get better over time" |
| Talking & sharing | Communication | "Telling someone what you know" |
| Making a plan | Planning | "Thinking about what to do next" |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Kid-friendly version of the dependency chain:
- Things that work together (Systems) → Things that make choices (Agents) → How they notice things (Perception) → How they think about it (Cognition) → What they decide to do (Action) → How they get better (Learning) → How they talk and share (Communication) → How they make plans (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Story/Introduction → Learning Goals (kid-friendly) → Key Words → Core Ideas (5 subsections with illustrations/scenarios) → Activities → Summary → References |
| `questions.md` | `# Course — Module — Think About It!` + simple numbered list (10-15 questions, open-ended and wonder-based) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Pick the Best Answer` (7 questions) → `Part B: Tell Us What You Think` (3 questions) |
| `lab.md` | `What We'll Do` → multi-part with `> **Goal:**` blockquotes → drawing/building/acting prompts → `{fill:textarea}` reflection → `What We Learned` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#4ade80` green accent), concept cards with fun icons, quiz with encouraging feedback |
| `README.md` | Quick Navigation header, overview, module contents table, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_story_time/03_perception/module.md to the bodies version: -->
See [How Our Bodies Notice Things](../../02_our_bodies/03_perception/module.md) to learn more about senses!

<!-- From any module to the glossary: -->
See the [Word List](../../resources/glossary.md) for what new words mean.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Language is appropriate for K-5 students
- [ ] No formulas, equations, or Greek letters appear
- [ ] Stories and characters are engaging and inclusive
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions are wonder-based and open-ended
- [ ] Quiz uses kid-friendly language ("Pick the Best Answer")
- [ ] Lab involves drawing, building, moving, or playing
- [ ] Content is fun — would a child enjoy this?

---

## Dashboard Color Identity

- **Accent**: Green `#4ade80`
- **Gradient**: Green → Cyan
- **Semantic**: Growth, playful, developmental
