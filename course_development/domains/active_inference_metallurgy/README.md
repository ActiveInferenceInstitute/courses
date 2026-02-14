# Active Inference for Metallurgy

> **Audience**: Materials scientists, metallurgical engineers, and process engineers
> **Files**: ~250

---

## Curriculum Statistics

| Metric | Value |
| --- | --- |
| Courses | 4 |
| Modules per Course | 8 |
| Total Modules | 32 |
| Files per Module | 7 |
| Target Audience | Materials scientists, metallurgical engineers, graduate students |
| Prerequisites | Thermodynamics, physical chemistry, materials science fundamentals, Python basics |

---

## Overview

Welcome to **Active Inference for Metallurgy**. This curriculum teaches Active Inference — the theory that all systems work by constantly predicting and acting to minimize surprise — through the lens of metals, alloys, and manufacturing processes.

**Tone**: Engineering-focused. Thermodynamic rigor meets shop-floor pragmatism.

## Courses

| # | Course | Perspective | Lab Type |
| --- | --- | --- | --- |
| 1 | [Metallurgical Systems](./01_metallurgical_systems/README.md) | Crystal structures, defects, thermodynamic fundamentals | Simulation Lab |
| 2 | [Thermodynamic Inference](./02_thermodynamic_inference/README.md) | Phase equilibria, CALPHAD, transformation kinetics | Calculation Lab |
| 3 | [Microstructural Evolution](./03_microstructural_evolution/README.md) | Nucleation, grain growth, precipitation, characterization | Image Analysis Lab |
| 4 | [Process Optimization](./04_process_optimization/README.md) | Heat treatment, welding, additive manufacturing, Industry 4.0 | Digital Twin Lab |

---

## Core Topics

Each course covers the same 8 topics in the same order — the Active Inference "spine":

| # | Topic | 01 Metallurgical Sys | 02 Thermo Inference | 03 Microstructure | 04 Process Opt |
| --- | --- | --- | --- | --- | --- |
| 1 | **Systems** | Crystal lattice as Markov blanket | Phase diagram as generative model | Grain boundaries as system boundaries | Manufacturing as inference system |
| 2 | **Agents** | Atoms and defects | Chemical species | Nuclei as autonomous agents | Sensors and controllers |
| 3 | **Perception** | XRD, spectroscopy | Thermal analysis, calorimetry | Microscopy, EBSD | In-situ monitoring, NDT |
| 4 | **Cognition** | Lattice energy calculations | Phase stability computation | Microstructure prediction | Digital twin cognition |
| 5 | **Action** | Deformation, alloying | Phase transformation kinetics | Grain growth and coarsening | Heat treatment, quenching |
| 6 | **Learning** | Alloy development history | CALPHAD and machine learning | Adaptive characterization | Closed-loop process control |
| 7 | **Communication** | Diffusion and mass transport | Interface energy signaling | Grain boundary networks | SCADA and data pipelines |
| 8 | **Planning** | Alloy design strategies | TTT/CCT diagram planning | Microstructure engineering | Process route optimization |

---

## Learning Pathway

```
Start Here
    ↓
[01 Metallurgical Systems] ──→ Atomic foundations & crystal architecture
    ↓
[02 Thermodynamic Inference] ──→ Phase diagrams as predictive models
    ↓
[03 Microstructural Evolution] ──→ How microstructures emerge & evolve
    ↓
[04 Process Optimization] ──→ Smart manufacturing & digital twins
```

---

## Module Structure

Each module contains **7 files**:

| File | Purpose |
| --- | --- |
| `module.md` | Core lesson with diagrams, equations, and case studies |
| `questions.md` | Study questions (conceptual + applied) |
| `practice_quiz.md` | Self-assessment quiz |
| `lab.md` | Simulation, calculation, or image analysis lab |
| `dashboard.html` | Interactive review (steel blue accent, progress meters) |
| `README.md` | Module overview and navigation |
| `AGENTS.md` | Content generation guidelines |

---

## Shared Resources

| Resource | Purpose |
| --- | --- |
| [Glossary](./resources/glossary.md) | Key terms with metallurgical translations |
| [Notation Table](./resources/notation_table.md) | Canonical symbols |
| [References](./resources/references.md) | Metallurgy and FEP literature |
| [Cross-Course Map](./resources/cross_course_map.md) | How modules connect across courses |
| [Learning Pathways](./resources/learning_pathways.md) | Suggested routes |
| [FAQ](./resources/faq.md) | Frequently asked questions |

---

## Directory Map

```
active_inference_metallurgy/
├── README.md
├── AGENTS.md
├── OVERVIEW.md
├── course.toml
├── audit_modules.sh
├── resources/
│   ├── glossary.md, notation_table.md, references.md
│   ├── cross_course_map.md, learning_pathways.md, faq.md
│   └── README.md, AGENTS.md
├── 01_metallurgical_systems/
│   ├── 01_systems/ … 08_planning/   (8 modules)
├── 02_thermodynamic_inference/
│   ├── 01_systems/ … 08_planning/   (8 modules)
├── 03_microstructural_evolution/
│   ├── 01_systems/ … 08_planning/   (8 modules)
└── 04_process_optimization/
    ├── 01_systems/ … 08_planning/   (8 modules)
```
