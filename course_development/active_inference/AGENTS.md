# Active Inference Curriculum — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Philosophy](./01_philosophy/) | [Cognitive Science](./02_cognitive_science/) | [Mathematics](./03_math/) | [Computer Science](./04_computer_science/)

## Overview

This directory contains a 4-course Active Inference curriculum with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain consistency in terminology, notation, and pedagogical structure across all courses.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_philosophy/` | Directory | Course 1: The Philosophy of Active Inference (8 modules) |
| `02_cognitive_science/` | Directory | Course 2: Cognitive Behavioral Science & Active Inference (8 modules) |
| `03_math/` | Directory | Course 3: The Mathematics of Active Inference (8 modules) |
| `04_computer_science/` | Directory | Course 4: Computational Active Inference (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|----|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any formula, symbol, or equation |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any paper or textbook |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references between courses |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, accurate content.

### 3. Maintain Course-Specific Perspectives

| Course | Perspective | Lab Type | Example Content |
|--------|------------|----------|----------------|
| Philosophy | Philosophical argumentation | Thought Experiment | "What does the Markov Blanket imply about the self?" |
| Cognitive Science | Neural correlates & clinical | Case Study Analysis | "How does predictive coding explain phantom limb pain?" |
| Mathematics | Formal derivation & proof | Derivation Exercise | "Derive the EFE decomposition into risk and ambiguity" |
| Computer Science | Custom `active_inference` library | Coding Lab | "Implement a T-maze agent and visualize its beliefs" |

---

## Notation Standards

All courses use the notation defined in [resources/notation_table.md](./resources/notation_table.md). Key symbols:

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| `F` | Variational Free Energy | `$F$` |
| `G` | Expected Free Energy | `$G$` |
| `π` | Policy (sequence of actions) | `$\pi$` |
| `q(s)` | Approximate posterior over states | `$q(s)$` |
| `p(o,s)` | Generative model (joint) | `$p(o,s)$` |
| **A** | Likelihood matrix | `$\mathbf{A}$` |
| **B** | Transition matrix | `$\mathbf{B}$` |
| **C** | Preference vector | `$\mathbf{C}$` |
| **D** | Prior state distribution | `$\mathbf{D}$` |
| **E** | Habit vector (prior over policies) | `$\mathbf{E}$` |
| `η, μ, σ, α` | External, internal, sensory, active states | `$\eta, \mu, \sigma, \alpha$` |
| `γ` | Policy precision (inverse temperature) | `$\gamma$` |
| `β` | Sensory precision (inverse variance) | `$\beta$` |
| `D_KL` | KL Divergence | `$D_{KL}$` |
| `S` | Surprisal: `-ln p(o)` | `$\mathfrak{S}$` |

For the full notation (including learned parameters, decompositions, temporal notation, and conventions), see [resources/notation_table.md](./resources/notation_table.md).

---

## Terminology Standards

| Preferred Term | Avoid | Reason |
|----------------|-------|--------|
| Generative Model | World model, internal model | Standard FEP terminology |
| Generative Process | Environment, true world | Distinguishes from Generative Model |
| Markov Blanket | Boundary, interface (informal) | Formal term from Bayesian statistics (Pearl) |
| Precision | Confidence, certainty | Precision = inverse variance (specific meaning) |

- **Rigor Note**: Always define VFE as a bound on *observation log-evidence* (past/present) and EFE as a functional of *policies* (future).
| Variational Free Energy (VFE) | Free energy (ambiguous) | Distinguishes from thermodynamic free energy; bound on `-ln p(o)` |
| Expected Free Energy (EFE) | Future free energy | Functional of policies `π`; components: Risk + Ambiguity |
| Surprisal | Surprise (colloquial) | Technical term: `-ln p(o)` |
| Recognition Density | Belief distribution | Standard variational inference term |
| Blanket States | Boundary states | Formal: union of sensory and active states |
| Active States | Action states, motor states | Formal Markov Blanket partition term |
| Sensory States | Input states, observation states | Formal Markov Blanket partition term |
| Policy | Plan, strategy (informal) | Formal: sequence of actions (a₁,...,aₜ) |
| Epistemic Value | Curiosity, exploration bonus | Formal component of EFE |
| Pragmatic Value | Utility, reward | Formal component of EFE |

For the full glossary with definitions, see [resources/glossary.md](./resources/glossary.md).

---

## Topic Order Convention

All 4 courses follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

This order is fixed and must not be changed. It reflects the logical dependency chain:

- Systems (what exists) → Agents (which systems count as agents) → Perception (how agents observe) → Cognition (how agents think) → Action (how agents act) → Learning (how agents improve) → Communication (how agents interact) → Planning (how agents plan ahead)

---

## Content Format Standards (biol-1 Compliance)

All content files follow the formatting conventions from `biol-1/course`:

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Introduction → Learning Objectives → Key Terms → Core Concepts (5 subsections) → Examples → Summary → References |
| `questions.md` | `# Course — Module — Study Questions` + simple numbered list (20 questions). No section headers within the list. |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions, `**1.**` numbering, `A) ... B) ...` format) → `Part B: Free Response` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → `<!-- lab:reflection -->` / `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme, concept cards with progress meters, quiz with JS answer checking, animated transitions |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between courses, use relative paths:

```markdown
<!-- From 01_philosophy/03_perception/module.md to the math version: -->
See the [mathematical formulation](../../03_math/03_perception/module.md) for the formal derivation.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- From any module to the root README: -->
See the [Curriculum Overview](../../README.md) for the full course map.

<!-- From any module to a parallel module in another course: -->
See [Perception in Cognitive Science](../../02_cognitive_science/03_perception/module.md) for the neural correlates.
```

---

## Content Generation Standards

- All content uses **real methods** — no mocks, stubs, or placeholder implementations.
- Module content should be **modular, functional, and documented**.
- Each module should be **self-contained** but aware of its position in the curriculum.
- Labs should provide **hands-on, actionable** exercises appropriate to the course domain.
- Dashboards should be **interactive HTML** with working JavaScript.
- All notation must match [resources/notation_table.md](./resources/notation_table.md).
- All terminology must match [resources/glossary.md](./resources/glossary.md).
- All references should be drawn from [resources/references.md](./resources/references.md) when possible.
- Philosophy course uses **incremental onboarding**: Module 1 starts with zero prerequisites and builds gradually.
- Computer Science course uses the custom `active_inference` library in `04_computer_science/src/active_inference/` (subpackages: `agent/`, `math/`, `visualization/`). Labs and module code examples must import from this library, not raw pymdp.
- Each course's study questions must reflect that course's **disciplinary perspective**.
- Quiz questions must be **answerable** from the module content.

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] No placeholder brackets `[...]` remain
- [ ] All notation matches `resources/notation_table.md`
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Questions are course-specific (not generic)
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 FR questions
- [ ] Lab has structured parts with learning goals and `{fill:textarea}` fields
- [ ] Summary table in lab is complete (not truncated)
