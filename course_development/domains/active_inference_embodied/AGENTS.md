# Active Inference: Embodied Experience — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Felt Sense](./01_felt_sense/) | [Living Presence](./02_living_presence/) | [Intuitive Knowing](./03_intuitive_knowing/) | [Moving Through World](./04_moving_through_world/) | [Domain AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for somatic practitioners, movement therapists, contemplatives, and anyone seeking qualitative, felt understanding of inference. Agents working in this repository must maintain a somatic, experiential, first-person tone — the body is the primary text. No equations, no code. Everything is felt, sensed, and embodied.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_felt_sense/` | Directory | Unit 1: Felt Sense — The Body's First Language (8 modules) |
| `02_living_presence/` | Directory | Unit 2: Living Presence — Being Here Now (8 modules) |
| `03_intuitive_knowing/` | Directory | Unit 3: Intuitive Knowing — Wisdom Without Words (8 modules) |
| `04_moving_through_world/` | Directory | Unit 4: Moving Through the World — Embodied Action (8 modules) |

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

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, experiential content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Felt Sense | Interoceptive awareness | Somatic Exercise | "Close your eyes. Notice the quality of your breathing. Is it tight? Open? Where do you feel it most?" |
| Living Presence | Present-moment awareness | Mindfulness Practice | "Sit with your feet on the floor. Feel the contact. What does 'boundary' feel like from the inside?" |
| Intuitive Knowing | Pre-reflective intelligence | Reflective Journaling | "Recall a time you 'just knew' something before you could explain it. What was happening in your body?" |
| Moving Through World | Embodied action & locomotion | Movement Lab | "Walk slowly across the room. Notice the moment of weight transfer. Where is the prediction?" |

### 4. Write for Embodied Practitioners

- Use first-person and second-person voice ("Notice..." "Feel..." "Allow...")
- **No formulas, no equations, no code, no Greek letters**
- Write poetically but precisely — somatic language has its own rigor
- Ground every Active Inference concept in a bodily experience
- Respect the intelligence of the body — don't reduce it to computation
- Reference somatic traditions (Gendlin, Feldenkrais, Alexander, mindfulness) alongside FEP literature

---

## Notation Standards

This curriculum uses **no mathematical notation**. Concepts are expressed through felt experience:

| FEP Concept | Embodied Translation | Experiential Cue |
|-------------|---------------------|-------------------|
| Generative Model | The body's felt map of the world | "The way your body already knows the shape of a staircase before you step" |
| Prediction Error | Felt surprise, disruption | "That jolt when you miss a step — your body expected something that wasn't there" |
| Markov Blanket | Skin, breath, the felt boundary | "Where do you end and the room begin? Feel the edge." |
| Precision | Attention, salience, vividness | "Notice what your body is drawn to right now. That's precision." |
| Active Inference | Moving to meet expectation | "Reaching for the cup — your hand already knows the shape before it arrives" |
| Free Energy | Felt tension, dis-ease | "That uncomfortable feeling when something doesn't fit — the body wants to resolve it" |

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
|----------------|-------|--------|
| Felt sense | Internal model | Gendlin's term; honors the experiential quality |
| Body's knowing | Computation, processing | Bodies know — they don't compute |
| Boundary | Markov blanket | Use the felt experience of edges and surfaces |
| Attention | Precision weighting | Use the phenomenological experience |
| Surprise (felt) | Prediction error | Use the qualitative experience of disruption |
| Settling | Free energy minimization | The body "settles" into coherence |
| Reaching toward | Policy selection | The felt experience of action as reaching |
| Resonance | Model alignment | When inner and outer match, there is felt resonance |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Embodied version of the dependency chain:
- What holds together (Systems) → What moves and chooses (Agents) → What is sensed and felt (Perception) → What is known without words (Cognition) → What the body does (Action) → How the body deepens its knowing (Learning) → How bodies meet and attune (Communication) → How the body anticipates (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Invitation/Opening → Learning Intentions → Key Phrases → Core Explorations (5 subsections, each with a somatic prompt) → Closing Reflection → Summary → References |
| `questions.md` | `# Course — Module — Reflections` + numbered list (10-15 contemplative questions) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Reflective Response` (3 questions) |
| `lab.md` | `Invitation` → multi-part with `> **Intention:**` blockquotes → somatic prompts → `{fill:textarea}` reflection fields → `What Emerged` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#fb7185` rose accent), concept cards with gentle animations, quiz with supportive feedback |
| `README.md` | Quick Navigation header, overview, module contents table, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_felt_sense/03_perception/module.md to the presence version: -->
See [Perception as Presence](../../02_living_presence/03_perception/module.md) for how awareness deepens sensing.

<!-- From any module to the glossary: -->
See the [Glossary](../../resources/glossary.md) for term definitions.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Tone is somatic, experiential, and respectful of embodied intelligence
- [ ] No formulas, equations, code, or Greek letters appear
- [ ] Every concept is grounded in a felt, bodily experience
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions are contemplative and open-ended
- [ ] Lab involves actual somatic practice (not just reading)
- [ ] Content honors multiple somatic traditions without privileging one

---

## Dashboard Color Identity

- **Accent**: Rose `#fb7185`
- **Gradient**: Rose → Purple
- **Semantic**: Somatic, felt, intuitive
