# Active Inference for Families — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Growing Together](./01_growing_together/) | [Tiny Bodies, Big Brains](./02_tiny_bodies_big_brains/) | [Patterns in Play](./03_patterns_in_play/) | [Screens, Toys & Tools](./04_screens_toys_tools/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for parents, grandparents, nannies, doulas, family educators, and pediatric professionals — anyone caring for children ages 0–6. It has 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain warm, nurturing, evidence-based content that translates neuroscience into everyday parenting wisdom.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_growing_together/` | Directory | Unit 1: Growing Together — Family Rhythms & Routines (8 modules) |
| `02_tiny_bodies_big_brains/` | Directory | Unit 2: Tiny Bodies, Big Brains — Inside Your Baby's World (8 modules) |
| `03_patterns_in_play/` | Directory | Unit 3: Patterns in Play — Learning Through Play (8 modules) |
| `04_screens_toys_tools/` | Directory | Unit 4: Screens, Toys & Tools — Navigating Modern Childhood (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before referencing any conceptual mapping |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, original content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Growing Together | Family systems & routines | Family Activity | "Track your family's daily rhythms for one day. Where are the routines? Where is the surprise?" |
| Tiny Bodies, Big Brains | Developmental neuroscience | Observation Journal | "Watch your baby explore a new object. What predictions are they testing?" |
| Patterns in Play | Play-based learning | Play Activity | "Sort a pile of socks together. Does your toddler notice the pattern before you do?" |
| Screens, Toys & Tools | Technology & tool use | Comparison Activity | "Offer the same toy in physical and digital form. What does your child do differently?" |

### 4. Write for Parents and Caregivers

- **Audience above all**: Every sentence must be written for a parent who is tired, loves their child, and has never taken a science course. If you wouldn't say it aloud to a new mom at 3 AM, don't write it.
- **No jargon without translation**: If a term from Active Inference is used (e.g., "prediction error," "generative model"), it must be immediately followed by a plain-language explanation or analogy.
- **Tone**: Warm, nurturing, practical, occasionally funny. Never condescending, never prescriptive. Frame everything as "here's one way to understand what's happening" rather than "you should do this."
- **Developmental sensitivity**: Always acknowledge the wide range of "normal" in child development. Never imply a child is "behind" or "advanced."
- **Evidence grounding**: All major claims must be traceable to peer-reviewed developmental psychology or neuroscience research listed in [resources/references.md](./resources/references.md).
- **Activities must be real**: Lab activities must be things a parent can actually do with a real baby or toddler in a real home. No idealized scenarios.

---

## Notation Standards

This curriculum uses **minimal notation** — almost everything is in plain language. Key concepts:

| Concept | Parent-Friendly Version | What It Really Means |
|---------|------------------------|---------------------|
| Generative Model | Your baby's inner map of the world | Internal model predicting observations from hidden states |
| Prediction Error | When something unexpected happens | Mismatch between expected and actual sensory input |
| Markov Blanket | The boundary between your baby and the world | Statistical boundary separating internal from external states |
| Precision | How much attention your baby gives something | Inverse variance — weight on a signal |
| Free Energy | That uncomfortable "something's off" feeling | Variational free energy (upper bound on surprisal) |
| Policy | What your baby decides to do next | Sequence of actions |

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
|----------------|-------|--------|
| Inner map / mental model | Generative model (alone) | Parents need the everyday version first |
| Surprise / mismatch | Prediction error (alone) | Use the felt experience |
| Boundary | Markov blanket (alone) | Introduce formal term after plain language |
| Attention / focus | Precision (alone) | Map to observable baby behavior |
| Routines as stability | Free energy minimization | Frame as what parents already do |
| Making choices | Policy selection | Frame as observable child agency |
| Sharing & turn-taking | Communication / shared models | Frame as recognizable parent-child interactions |
| Growing into plans | Planning / future states | Frame as developmental milestones |

---

## Key Parenting Concepts by Module

| Module | Active Inference Concept | Parenting Translation |
| --- | --- | --- |
| Systems | Markov blanket, boundaries | Routines, rhythms, family structure |
| Agents | Autonomy, goal-directedness | Your baby as an active explorer, not passive recipient |
| Perception | Prediction error, sensory input | Startle reflexes, novelty-seeking, sensory play |
| Cognition | Generative model, belief updating | Object permanence, categorizing, imaginative play |
| Action | Active inference, motor control | Reaching, crawling, trial-and-error |
| Learning | Model updating, habituation | Repetition, scaffolding, mastery |
| Communication | Shared models, social inference | Babbling, joint attention, turn-taking |
| Planning | Future states, policy selection | Milestones, routines as plans, growing independence |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Family version of the dependency chain:

- Your family is a system (Systems) → Your baby is an active explorer (Agents) → How babies sense and are surprised (Perception) → How little minds make big guesses (Cognition) → Reaching, crawling, doing (Action) → Getting better every day (Learning) → First words and sharing (Communication) → Growing into the future (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Story/Introduction → Learning Goals (parent-friendly) → Key Words → Core Ideas (5 subsections with parenting scenarios) → Try This at Home → Summary → References |
| `questions.md` | `# Course — Module — Reflection Questions` + numbered list (10-15 open-ended, personal reflection questions) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Tell Us What You Think` (3 questions) |
| `lab.md` | `What We'll Do` → multi-part with `> **Goal:**` blockquotes → parent-child activity prompts → `{fill:textarea}` reflection fields → `What We Learned` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#fb923c` orange accent), concept cards with click-to-flip, quiz with encouraging feedback |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_growing_together/03_perception/module.md to the bodies version: -->
See [How Tiny Brains Sense the World](../../02_tiny_bodies_big_brains/03_perception/module.md) for what's happening inside your baby.

<!-- From any module to the glossary: -->
See the [Glossary](../../resources/glossary.md) for what new words mean.

<!-- From any module to the root README: -->
See the [Curriculum Overview](../../README.md) for the full course map.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Language is warm, nurturing, and appropriate for parents with no science background
- [ ] No jargon appears without an immediate plain-language translation
- [ ] Activities are realistic for real parents with real babies/toddlers
- [ ] Developmental claims acknowledge the wide range of "normal"
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Questions are personal, reflective, and open-ended
- [ ] Quiz uses encouraging, non-judgmental language
- [ ] Lab activities involve real parent-child interaction
- [ ] Content is evidence-grounded (traceable to references)

---

## Dashboard Color Identity

- **Accent**: Orange `#fb923c`
- **Gradient**: Orange → Yellow
- **Semantic**: Warm, nurturing, practical
