# Active Inference for Organizations — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Organizational Systems](./01_organizational_systems/) | [Collective Intelligence](./02_collective_intelligence/) | [Strategic Modeling](./03_strategic_modeling/) | [Digital Transformation](./04_digital_transformation/) | [Domain AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for business leaders, managers, consultants, and organizational scientists with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain a professional, strategic tone while connecting FEP theory to real organizational challenges.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_organizational_systems/` | Directory | Unit 1: Organizational Systems — Boundaries and Identity (8 modules) |
| `02_collective_intelligence/` | Directory | Unit 2: Collective Intelligence — Shared Models (8 modules) |
| `03_strategic_modeling/` | Directory | Unit 3: Strategic Modeling — Adaptive Strategy (8 modules) |
| `04_digital_transformation/` | Directory | Unit 4: Digital Transformation — AI-Augmented Organizations (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any formal concept or diagram |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, actionable content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Organizational Systems | Boundaries & structure | Case Study | "Map the Markov blanket of your department — what information crosses the boundary?" |
| Collective Intelligence | Shared models & alignment | Workshop | "Design a workshop that helps two teams align their generative models of a shared goal" |
| Strategic Modeling | Adaptive planning | Strategy Exercise | "Use expected free energy to evaluate three strategic options for market entry" |
| Digital Transformation | AI integration & change | Implementation Plan | "Draft an implementation plan for an AI copilot that reduces organizational prediction error" |

### 4. Write for Business Professionals

- Use business language and real organizational examples
- Light formalism only — diagrams and conceptual models, not dense math
- Every concept must connect to a recognizable organizational challenge
- Use case studies from real industries (anonymized as needed)
- Frame FEP as a lens for understanding organizations, not a prescriptive framework
- Balance theory with practical tools and exercises

---

## Notation Standards

This curriculum uses **light conceptual notation**. Key mappings:

| FEP Concept | Organizational Translation | Example |
|-------------|---------------------------|---------|
| Generative Model | Organization's mental model of its market/environment | "How does your org think the market works?" |
| Prediction Error | Strategic surprise, missed forecast | "Revenue fell short of forecast — what assumption was wrong?" |
| Markov Blanket | Organizational boundary, team boundary | "What information flows in and out of your department?" |
| Precision | Confidence in data/signals | "How much do you trust this market research?" |
| Active Inference | Strategic action to confirm/disconfirm models | "We launched the pilot to test our market hypothesis" |
| Free Energy | Organizational tension, misalignment | "The gap between our strategy and market reality" |
| Policy | Strategy, action plan | "Our three-year strategic plan" |
| Nested Systems | Divisions, departments, teams | "Teams within divisions within the enterprise" |

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
|----------------|-------|--------|
| Organizational model | Generative model (alone) | Contextualize for business audience |
| Strategic surprise | Prediction error (alone) | Business-friendly framing |
| Organizational boundary | Markov blanket (alone) | Introduce formal term after organizational concept |
| Signal confidence | Precision (alone) | Map to data quality and trust |
| Collective model | Shared generative model | Natural business language |
| Model alignment | Free energy minimization | Frame as reducing misalignment |
| Strategic options | Policies | Frame as business strategy |
| Information value | Epistemic value | Frame as business intelligence |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Organizational version of the dependency chain:
- What is the organization? (Systems) → Who are the agents within it? (Agents) → How does the org sense its environment? (Perception) → How does it make sense of signals? (Cognition) → How does it act on strategy? (Action) → How does it adapt and improve? (Learning) → How do teams and divisions coordinate? (Communication) → How does it plan for the future? (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Executive Summary → Learning Objectives → Key Concepts → Core Content (5 subsections with case examples) → Application → Summary → References |
| `questions.md` | `# Course — Module — Discussion Questions` + numbered list (15-20 questions, mix of analytical and applied) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Short Analysis` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → case study / workshop prompts → `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#fbbf24` amber accent), concept cards with progress meters, quiz with JS answer checking |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_organizational_systems/03_perception/module.md to the strategy version: -->
See [Strategic Perception](../../03_strategic_modeling/03_perception/module.md) for how organizations sense strategic opportunities.

<!-- From any module to the glossary: -->
See the [Glossary](../../resources/glossary.md) for term definitions.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Content is appropriate for business professionals (no unnecessary math)
- [ ] Every concept connects to a real organizational challenge
- [ ] Case studies are realistic and actionable
- [ ] No placeholder brackets `[...]` remain
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions mix analytical thinking with practical application
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 questions
- [ ] Lab involves collaborative, workshop-style activities
- [ ] FEP terminology is always introduced with organizational parallel first

---

## Dashboard Color Identity

- **Accent**: Amber `#fbbf24`
- **Gradient**: Amber → Red
- **Semantic**: Strategic, dynamic, decisive
