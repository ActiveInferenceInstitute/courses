# Active Inference: Crochet Circles — Agent Guidelines

> **Quick Navigation**: [OVERVIEW](./OVERVIEW.md) | [Resources](./resources/) | [Stitch & Structure](./01_stitch_and_structure/) | [Fiber & Flow](./02_fiber_and_flow/) | [Pattern & Prediction](./03_pattern_and_prediction/) | [Circle & Community](./04_circle_and_community/) | [Domain AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-course Active Inference curriculum for fiber artists, crafters, crochet circle participants, and the curious. Agents working in this repository must maintain a warm, crafty, hands-on, accessible tone — like learning from a knowledgeable crafter sitting next to you. Real craft knowledge and real science, woven together through stitch-based metaphors.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `OVERVIEW.md` | File | Curriculum overview, vision, course map, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_stitch_and_structure/` | Directory | Course 1: Stitch & Structure — Individual crocheter, stitch mechanics (8 modules) |
| `02_fiber_and_flow/` | Directory | Course 2: Fiber & Flow — Materials, yarn properties, creative flow (8 modules) |
| `03_pattern_and_prediction/` | Directory | Course 3: Pattern & Prediction — Pattern reading, design, math structure (8 modules) |
| `04_circle_and_community/` | Directory | Course 4: Circle & Community — Social dynamics, teaching, cultural transmission (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** — crochet abbreviations mapped to AI concepts | Before referencing any stitch or conceptual mapping |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** — crochet-AI term definitions | Before using or defining any term |
| [resources/references.md](./resources/references.md) | **Canonical references** — foundational and craft-specific sources | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** — how modules connect across all 4 courses | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real content** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, craft-grounded content.

### 3. Maintain Course-Specific Perspectives

| Course | Perspective | Lab Type | Example Content |
|--------|------------|----------|----------------|
| Stitch & Structure | Individual stitch mechanics | Hands-on Stitch Lab | "Pick up your hook. Chain 10. Feel the rhythm of yarn-over, pull-through. Where does the prediction live in your fingers?" |
| Fiber & Flow | Material properties & flow | Materials Exploration | "Hold two different yarns — one acrylic, one wool. Close your eyes. How does your hand's generative model adjust to each?" |
| Pattern & Prediction | Symbolic pattern structure | Pattern Design Workshop | "Read Row 3: *sc in next 2, inc in next*. Before you stitch it, can you see the shape it will make? That mental image is your generative model." |
| Circle & Community | Social crafting dynamics | Group Activity | "Notice who the newer crafter watches when they get stuck. That gaze is an epistemic action — actively sampling the environment for prediction-error reduction." |

### 4. Write for Crafters

- Use second-person voice ("Pick up your hook..." "Notice how..." "Try this...")
- **Use real crochet terminology** — chain, single crochet, double crochet, frogging, gauge, tension, WIP, FO
- Write warmly but precisely — craft language has its own rigor
- Ground every Active Inference concept in a concrete crochet experience
- Respect the intelligence of craft practice — crochet is sophisticated embodied cognition, not a trivial metaphor
- Reference craft traditions (stitch dictionaries, pattern conventions, circle culture) alongside FEP literature
- Use humor where natural — crafters know the pain of frogging and the joy of finishing

---

## Notation Standards

This curriculum uses crochet notation alongside plain-language Active Inference translations:

| Crochet Term | Active Inference Mapping | Craft Example |
|-------------|------------------------|---------------|
| Hook-yarn boundary | Markov blanket | "The point where hook meets yarn is where inside (your intention) meets outside (the material)" |
| Pattern | Generative model | "The written pattern is a compact model of the finished object — every row is a prediction" |
| Frogging | Prediction-error response | "Rip it, rip it — when the work diverges too far from the pattern, you undo and re-predict" |
| Gauge swatch | Prior precision tuning | "Testing your tension before committing — calibrating your generative model to this yarn" |
| Tension | Precision weighting | "How tightly you hold the yarn determines how much sensory detail each stitch carries" |
| Stitch marker | Epistemic action | "Placing a marker offloads counting to the environment — reducing cognitive free energy" |
| Stitch count | State estimation | "Counting stitches at the end of a row is comparing observed states to predicted states" |

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
|----------------|-------|--------|
| Pattern | Generative model (in isolation) | Use the craft term; connect to AI concept explicitly when teaching |
| Frogging / ripping back | Error correction | Use the crafter's own word for undoing work |
| Tension | Precision weighting (in isolation) | The physical experience of yarn tension grounds the abstract concept |
| Gauge | Calibration (in isolation) | Gauge is the crafter's word for ensuring predictions match reality |
| Reading the work | State estimation | Crafters "read" their fabric — this is active perceptual inference |
| Muscle memory | Habituated prior | The crafter's term for deeply learned stitch patterns |
| Stash | Resource model | A crafter's yarn collection — their model of available materials |
| WIP (work in progress) | Ongoing inference | The partially completed object embodies accumulated predictions |
| FO (finished object) | Converged model | The completed work where predictions and reality have been reconciled |

---

## Topic Order Convention

All 4 courses follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Crochet version of the dependency chain:
- What holds together as a system (Systems) → Who is the crocheter as an agent (Agents) → What is sensed through fingers and eyes (Perception) → What the crafter thinks and models (Cognition) → Every stitch as an action (Action) → How skill deepens over projects (Learning) → How crafters share and teach (Communication) → How projects and sessions are planned (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Opening/Hook → Learning Intentions → Key Terms → Core Explorations (5 subsections, each with a craft prompt) → Closing Reflection → Summary → References |
| `questions.md` | `# Course — Module — Reflections` + numbered list (10-15 craft-grounded questions) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Reflective Response` (3 questions) |
| `lab.md` | `Introduction` → multi-part with `> **Intention:**` blockquotes → craft prompts → `{fill:textarea}` reflection fields → `What Did You Notice` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#a78bfa` violet accent), concept cards with animations, quiz with supportive feedback |
| `README.md` | Quick Navigation header, overview, module contents table, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between courses, use relative paths:

```markdown
<!-- From 01_stitch_and_structure/03_perception/module.md to the pattern version: -->
See [Counting Stitches, Noticing Drift](../../03_pattern_and_prediction/03_perception/module.md) for how pattern-reading deepens perceptual inference.

<!-- From any module to the glossary: -->
See the [Glossary](../../resources/glossary.md) for term definitions.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Tone is warm, crafty, hands-on, and accessible
- [ ] Real crochet terminology is used correctly
- [ ] Every Active Inference concept is grounded in a concrete crochet experience
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions are craft-grounded and thought-provoking
- [ ] Lab involves actual crochet practice (not just reading)
- [ ] Content respects crochet as sophisticated embodied cognition

---

## Dashboard Color Identity

- **Accent**: Violet `#a78bfa`
- **Gradient**: Violet → Fuchsia
- **Semantic**: Creative, textured, handcrafted
