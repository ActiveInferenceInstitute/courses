# Active Inference 101: College First Semester — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Cognitive Science](./01_cognitive_science/) | [Computational Neuroscience](./02_computational_neuroscience/) | [Mathematical Frameworks](./03_mathematical_frameworks/) | [Implementation](./04_implementation/) | [Portfolio AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit introductory Active Inference curriculum for first-semester college undergraduates with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain consistency in terminology, notation, and pedagogical structure across all units while keeping content accessible for students encountering Active Inference for the first time at the college level.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_cognitive_science/` | Directory | Unit 1: Cognitive Science & Active Inference (8 modules) |
| `02_computational_neuroscience/` | Directory | Unit 2: Computational Neuroscience & Active Inference (8 modules) |
| `03_mathematical_frameworks/` | Directory | Unit 3: Mathematical Frameworks for Active Inference (8 modules) |
| `04_implementation/` | Directory | Unit 4: Implementing Active Inference (8 modules) |

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

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Cognitive Science | Behavioral & cognitive | Essay & Discussion | "How does predictive processing explain the rubber hand illusion?" |
| Computational Neuroscience | Neural implementation | Simulation Lab | "Simulate a predictive coding network for visual processing" |
| Mathematical Frameworks | Formal introduction | Problem Set | "Show that VFE decomposes into energy minus entropy" |
| Implementation | Applied computation | Coding Assignment | "Implement a simple active inference agent in Python/NumPy" |

### 4. Write for First-Semester Undergraduates

- Assume basic calculus, linear algebra, and introductory programming (Python)
- Define all Active Inference terms on first use
- Use concrete examples before formal definitions
- Build notation gradually — introduce symbols one at a time
- Bridge from familiar concepts (Bayesian reasoning, prediction) to FEP formalism

---

## Notation Standards

All units use the notation defined in [resources/notation_table.md](./resources/notation_table.md). Key symbols:

| Symbol | Meaning | Context |
|--------|---------|---------|
| `F` | Variational Free Energy | Introduced formally in Unit 3 |
| `G` | Expected Free Energy | Introduced formally in Unit 3 |
| `P(A\|B)` | Conditional probability | Used throughout, assumed prerequisite |
| **A** | Likelihood matrix | How observations relate to hidden states |
| **B** | Transition matrix | How states change over time |
| **C** | Preference vector | What the agent prefers to observe |
| **D** | Prior state distribution | Initial beliefs about states |
| `q(s)` | Approximate posterior | The agent's current beliefs |
| `D_KL` | KL Divergence | Measuring distance between distributions |

---

## Terminology Standards

| Preferred Term | Simpler Introduction | Formal Meaning |
|----------------|---------------------|----------------|
| Generative Model | Brain's model of causes | Internal model predicting observations from hidden states |
| Prediction Error | Surprise signal | Difference between predicted and actual observations |
| Markov Blanket | Statistical boundary | The partition separating internal from external states |
| Precision | Confidence weighting | Inverse variance of a probability distribution |
| Variational Free Energy (VFE) | Overall prediction error | Upper bound on surprisal: `-ln p(o)` |
| Expected Free Energy (EFE) | Anticipated prediction error | Functional of policies evaluating future outcomes |
| Policy | Action plan | Sequence of actions `(a₁, ..., aₜ)` |
| Epistemic Value | Information gain | Value of reducing uncertainty about hidden states |
| Pragmatic Value | Goal achievement | Value of reaching preferred observations |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

This order reflects the logical dependency chain: defining systems → identifying agents → how they sense → how they think → how they act → how they improve → how they interact → how they plan ahead.

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Introduction → Learning Objectives → Key Terms → Core Concepts (5 subsections) → Examples → Summary → References |
| `questions.md` | `# Course — Module — Study Questions` + simple numbered list (20 questions). No section headers within the list. |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions, `**1.**` numbering, `A) ... B) ...` format) → `Part B: Short Answer` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → `<!-- lab:reflection -->` / `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#22d3ee` cyan accent), concept cards with progress meters, quiz with JS answer checking, animated transitions |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_cognitive_science/03_perception/module.md to the math version: -->
See the [mathematical formulation](../../03_mathematical_frameworks/03_perception/module.md) for the formal derivation.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- From any module to the root README: -->
See the [Curriculum Overview](../../README.md) for the full course map.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Content is appropriate for first-semester undergraduates
- [ ] Mathematical notation is introduced gradually (not all at once)
- [ ] No placeholder brackets `[...]` remain
- [ ] All notation matches `resources/notation_table.md`
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files: `module.md`, `questions.md`, `practice_quiz.md`, `lab.md`, `dashboard.html`, `README.md`, `AGENTS.md`
- [ ] Questions are unit-specific (not generic)
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 questions
- [ ] Lab has structured parts with learning goals and `{fill:textarea}` fields
- [ ] Summary table in lab is complete

---

## Dashboard Color Identity

- **Accent**: Cyan `#22d3ee`
- **Gradient**: Cyan → Purple
- **Semantic**: Fresh, accessible, introductory
