# Active Inference for Robotics — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Resources](./resources/) | [Robotic Systems](./01_robotic_systems/) | [Bio-Inspired Design](./02_bioinspired_design/) | [Control & Estimation](./03_control_estimation/) | [Autonomous Agents](./04_autonomous_agents/) | [Domain AGENTS](../AGENTS.md)

## Overview

This directory contains a 4-unit Active Inference curriculum for robotics engineers and researchers with 32 modules, shared resources, and comprehensive documentation. Agents working in this repository must maintain engineering rigor in terminology, notation, and implementation while connecting FEP theory to practical robotic systems.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Curriculum overview, learning pathway, and navigation |
| `AGENTS.md` | File | This file — agent guidelines and content standards |
| `resources/` | Directory | Shared notation, glossary, references, and cross-course map |
| `01_robotic_systems/` | Directory | Unit 1: Robotic Systems — Architecture and Boundaries (8 modules) |
| `02_bioinspired_design/` | Directory | Unit 2: Bio-Inspired Design — Nature's Inference Engines (8 modules) |
| `03_control_estimation/` | Directory | Unit 3: Control & Estimation — Active Inference Controllers (8 modules) |
| `04_autonomous_agents/` | Directory | Unit 4: Autonomous Agents — Multi-Agent Robotics (8 modules) |

---

## Critical Rules for All Agents

### 1. Consult Shared Resources First

Before generating or editing any content, read these files:

| Resource | Purpose | When to Consult |
|----------|---------|-------|
| [resources/notation_table.md](./resources/notation_table.md) | **Canonical notation** | Before writing any formula, equation, or system diagram |
| [resources/glossary.md](./resources/glossary.md) | **Canonical definitions** | Before using or defining any technical term |
| [resources/references.md](./resources/references.md) | **Canonical references** | Before citing any source |
| [resources/cross_course_map.md](./resources/cross_course_map.md) | **Cross-course links** | Before adding cross-references |

### 2. Never Use Placeholders

All content must use **real methods** — no mocks, stubs, placeholder brackets, or `[TODO]` markers. Every module must contain substantive, technically accurate content.

### 3. Maintain Unit-Specific Perspectives

| Unit | Perspective | Lab Type | Example Content |
|------|------------|----------|----------------|
| Robotic Systems | Architecture & hardware | Hardware Lab | "Diagram the sensor-actuator architecture of a 6-DOF manipulator as a Markov blanket" |
| Bio-Inspired Design | Biological inspiration | Design Challenge | "Design a whisker-based tactile sensor array inspired by rat vibrissae for active perception" |
| Control & Estimation | Control theory & state estimation | Simulation Lab | "Implement an active inference PID controller and compare it to classical PID on a pendulum" |
| Autonomous Agents | Multi-agent systems | ROS2 Project | "Build a ROS2 node that implements belief propagation for multi-robot coordination" |

### 4. Write for Robotics Engineers

- Assume strong foundations in control theory, linear algebra, signal processing, and programming
- Use standard robotics notation (state vectors, transfer functions, Jacobians)
- Include code examples in Python and ROS2 where appropriate
- Reference real hardware platforms and sensor technologies
- Connect FEP to existing robotics paradigms (PID, Kalman filters, SLAM, MPC)
- Balance theory with practical implementation details

---

## Notation Standards

All units use the notation defined in [resources/notation_table.md](./resources/notation_table.md). Key symbols:

| Symbol | Meaning | Robotics Context |
|--------|---------|-----------------|
| `F` | Variational Free Energy | Control objective to minimize |
| `G` | Expected Free Energy | Planning objective for path selection |
| **A** | Likelihood matrix | Sensor model (observation → state) |
| **B** | Transition matrix | Dynamics model (state evolution) |
| **C** | Preference vector | Target state / goal configuration |
| **D** | Prior state distribution | Initial state estimate |
| `q(s)` | Approximate posterior | State estimate (belief) |
| `x, u, z` | State, control input, observation | Standard robotics notation |
| `K` | Kalman gain / precision-weighted gain | Active inference gain matrix |
| `J` | Jacobian | Linearization of dynamics/observation model |

---

## Terminology Standards

| Preferred Term | Robotics Equivalent | FEP Formal Term |
|----------------|-------------------|----------------|
| Sensor model | Observation function `h(x)` | Likelihood mapping **A** |
| Dynamics model | State transition `f(x, u)` | Transition mapping **B** |
| Goal configuration | Target / setpoint | Preference prior **C** |
| State estimate | Belief, posterior | Recognition density `q(s)` |
| Prediction error | Innovation, residual | Sensory prediction error |
| Active inference controller | FEP-based controller | Active inference agent |
| Sensor-actuator loop | Perception-action cycle | Active inference loop |
| Multi-robot coordination | Swarm intelligence, consensus | Shared generative models |

---

## Topic Order Convention

All 4 units follow this exact topic order:

1. **Systems** → 2. **Agents** → 3. **Perception** → 4. **Cognition** → 5. **Action** → 6. **Learning** → 7. **Communication** → 8. **Planning**

Robotics version of the dependency chain:
- What is a robotic system? (Systems) → What makes a robot an agent? (Agents) → How does it sense? (Perception) → How does it estimate state? (Cognition) → How does it actuate? (Action) → How does it adapt? (Learning) → How do robots coordinate? (Communication) → How does it plan trajectories? (Planning)

---

## Content Format Standards

| File | Format Requirements |
|------|-------------------|
| `module.md` | `# Title: Subtitle` → Introduction → Learning Objectives → Key Terms → Core Concepts (5 subsections with diagrams/code) → Implementation Notes → Summary → References |
| `questions.md` | `# Course — Module — Study Questions` + numbered list (20 questions, mix of conceptual and implementation) |
| `practice_quiz.md` | `Name/Date` header → `Part A: Multiple Choice` (7 questions) → `Part B: Short Answer/Analysis` (3 questions) |
| `lab.md` | `Objectives` → multi-part with `> **Learning Goal:**` blockquotes → hardware/simulation prompts → `{fill:textarea}` fields → `Summary` table |
| `dashboard.html` | Interactive HTML5: dark theme (`#34d399` emerald accent), concept cards with progress meters, quiz with JS answer checking |
| `README.md` | Quick Navigation header, overview, module contents table, cross-references, navigation footer |
| `AGENTS.md` | Quick Navigation header, directory contents table, content generation conventions |

---

## Cross-Reference Convention

When linking between units, use relative paths:

```markdown
<!-- From 01_robotic_systems/03_perception/module.md to the control version: -->
See [Perception for Control](../../03_control_estimation/03_perception/module.md) for state estimation in control loops.

<!-- From any module to the notation table: -->
See the [Notation Table](../../resources/notation_table.md) for symbol definitions.

<!-- Cross-domain reference: -->
See the [Core Mathematics course](../../../active_inference/03_math/03_perception/module.md) for the formal derivation of perceptual inference.
```

---

## Quality Checklist for Content Review

Before marking any module complete, verify:

- [ ] Content reflects engineering rigor (correct notation, realistic hardware)
- [ ] Code examples are functional Python or valid ROS2 patterns
- [ ] Hardware references are to real, available platforms
- [ ] No placeholder brackets `[...]` remain
- [ ] All notation matches `resources/notation_table.md`
- [ ] All terms match `resources/glossary.md`
- [ ] Cross-references use correct relative paths
- [ ] Module has all 7 files
- [ ] Questions mix conceptual understanding with implementation skills
- [ ] Quiz Part A has exactly 7 MC questions; Part B has exactly 3 questions
- [ ] Lab activities are implementable (simulation or real hardware)
- [ ] FEP concepts are connected to standard robotics paradigms

---

## Dashboard Color Identity

- **Accent**: Emerald `#34d399`
- **Gradient**: Emerald → Blue
- **Semantic**: Technical, precise, engineered
