# Active Inference for Robotics

> **Audience**: Robotics engineers and researchers
> **Estimated files**: 248

---

## Curriculum Statistics

| Metric | Value |
| --- | --- |
| Courses | 4 |
| Modules per Course | 8 |
| Total Modules | 32 |
| Files per Module | 7 |
| Estimated Total Files | 248 |
| Target Audience | Robotics engineers, graduate students, researchers |
| Prerequisites | Control theory, linear algebra, Python, and ROS2 basics |

---

## Overview

Welcome to **Active Inference for Robotics**. This curriculum teaches Active Inference — the theory that all living systems work by constantly predicting and acting to minimize surprise.

**Tone**: Engineering-focused. Hardware + software. ROS2, sensor fusion, control theory.

## Courses

| # | Course | Perspective | Lab Type |
| --- | --- | --- | --- |
| 1 | [Robotic Systems](./01_robotic_systems/README.md) | Sensors, actuators, embedded systems | Hardware Lab |
| 2 | [Bio-Inspired Design](./02_bioinspired_design/README.md) | Biomimicry & neural architectures | Design Challenge |
| 3 | [Control & Estimation](./03_control_estimation/README.md) | Kalman filters, PID, MPC, active inference | Simulation Lab |
| 4 | [Autonomous Agents](./04_autonomous_agents/README.md) | SLAM, navigation, multi-robot coordination | ROS2 Project |

---

## Core Topics

Each course covers the same 8 topics in the same order — the Active Inference "spine":

| # | Topic | 01 Robotic Sys | 02 Bio-Inspired | 03 Control/Est | 04 Autonomous |
| --- | --- | --- | --- | --- | --- |
| 1 | **Systems** | Robot architecture | Biological systems | Dynamical systems | Multi-agent systems |
| 2 | **Agents** | Embodied robots | Bio-inspired agents | Controller agents | Autonomous agents |
| 3 | **Perception** | Sensor models | Bio-sensing | State estimation | SLAM |
| 4 | **Cognition** | Onboard inference | Neural architectures | Filtering & smoothing | Belief propagation |
| 5 | **Action** | Actuation | Motor primitives | Control signals | Motion planning |
| 6 | **Learning** | Adaptive control | Evolutionary design | Parameter estimation | Online learning |
| 7 | **Communication** | Sensor fusion | Swarm signals | Distributed estimation | Multi-robot comms |
| 8 | **Planning** | Task planning | Morphological planning | MPC | Cooperative planning |

---

## Learning Pathway

```
Start Here
    ↓
[01 Robotic Systems] ──→ Hardware foundations & sensor-actuator architecture
    ↓
[02 Bio-Inspired Design] ──→ Nature's inference engines & biomimicry
    ↓
[03 Control & Estimation] ──→ Active inference controllers & state estimation
    ↓
[04 Autonomous Agents] ──→ Multi-agent systems & ROS2 integration
```

**Recommended path**: Work through sequentially. Engineers with strong control theory backgrounds may start with Course 03 and then explore Courses 01–02 for context.

---

## Module Structure

Each module contains **7 files**:

| File | Purpose |
| --- | --- |
| `module.md` | Core lesson with diagrams, code, and implementation notes |
| `questions.md` | Study questions (conceptual + implementation) |
| `practice_quiz.md` | Self-assessment quiz |
| `lab.md` | Hardware lab, simulation, or ROS2 project |
| `dashboard.html` | Interactive review (emerald accent, progress meters) |
| `README.md` | Module overview and navigation |
| `AGENTS.md` | Content generation guidelines |

---

## Shared Resources

| Resource | Purpose |
| --- | --- |
| [Glossary](./resources/glossary.md) | Key terms with robotics translations |
| [Notation Table](./resources/notation_table.md) | Canonical symbols (state vectors, matrices, gain) |
| [References](./resources/references.md) | Robotics and FEP literature |
| [Cross-Course Map](./resources/cross_course_map.md) | How modules connect across courses |
| [Learning Pathways](./resources/learning_pathways.md) | Suggested routes through the material |
| [FAQ](./resources/faq.md) | Frequently asked questions |

---

## Design Principles

1. **Engineering rigor**: Correct notation, real hardware references, functional code
2. **FEP-to-robotics bridge**: Every formal concept mapped to a robotics paradigm
3. **Implementation-ready**: Labs produce working code or hardware prototypes
4. **Standard tools**: Python, ROS2, standard robotics libraries
5. **From classical to active inference**: Content bridges PID/Kalman/MPC to FEP-based control

---

## Directory Map

```
active_inference_robotics/
├── README.md              ← You are here
├── AGENTS.md              ← Agent guidelines
├── OVERVIEW.md            ← Extended overview
├── resources/             ← Shared glossary, references, cross-course map
├── 01_robotic_systems/
│   ├── 01_systems/ … 08_planning/   (8 modules)
├── 02_bioinspired_design/
│   ├── 01_systems/ … 08_planning/   (8 modules)
├── 03_control_estimation/
│   ├── 01_systems/ … 08_planning/   (8 modules)
└── 04_autonomous_agents/
    ├── 01_systems/ … 08_planning/   (8 modules)
```

---

## Quick Start

1. Choose a course based on your engineering focus.
2. Start with Module 01 (Systems) and work through sequentially.
3. Use the dashboard for interactive review.
4. Complete the lab for hands-on practice.
