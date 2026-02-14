# Computational Active Inference — Agent Guidelines

> **Quick Navigation**: [README](./README.md) | [Syllabus](./syllabus.md) | [Curriculum AGENTS](../AGENTS.md) | [Resources](../resources/)

## Overview

Agents working on this course (Computer Science) should approach all content from a **computational** perspective while maintaining consistency with the curriculum-wide notation, terminology, and format standards.

---

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `README.md` | File | Course overview and navigation |
| `AGENTS.md` | File | This file — course-specific agent guidelines |
| `syllabus.md` | File | Full course syllabus with schedule and assessment |
| `src/` | Directory | `active_inference` Python package (v0.4.0) — 3 subpackages, 56 exports |
| `tests/` | Directory | pytest suite — 253 tests (agent, math, visualization, config, output) |
| `output/` | Directory | Generated visualization figures (30 PNGs from test suite) |
| `01_systems/` | Directory | Module 1: Systems — Generative Process vs Generative Model in pymdp |
| `02_agents/` | Directory | Module 2: Agents — The Agent Class: States, Observations, and A-E Matrices |
| `03_perception/` | Directory | Module 3: Perception — State Estimation with A-Matrix and B-Matrix |
| `04_cognition/` | Directory | Module 4: Cognition — C-Matrix (Preferences), D-Matrix (Priors), E-Matrix (Habits) |
| `05_action/` | Directory | Module 5: Action — Policy Selection and Expected Free Energy Calculation |
| `06_learning/` | Directory | Module 6: Learning — Parameter Learning: Updating Dirichlet Concentrations |
| `07_communication/` | Directory | Module 7: Communication — Multi-Agent Simulation and Signaling Games |
| `08_planning/` | Directory | Module 8: Planning — Deep Temporal Models, Gridworlds, and Long-Horizon Planning |

---

## Source Package: `active_inference` (v0.4.0)

### Subpackages

| Subpackage | Module | Key Exports |
|------------|--------|-------------|
| `agent` | `generative_model.py` | `GenerativeModel` (A, B, C, D, E matrices) |
| `agent` | `agent.py` | `ActiveInferenceAgent` (perception–action loop) |
| `agent` | `environment.py` | `DiscreteEnvironment` (generative process) |
| `math` | `free_energy.py` | `compute_vfe`, `compute_efe`, `softmax`, `entropy`, `kl_divergence` |
| `math` | `inference.py` | `run_state_inference` (variational fixed-point iteration) |
| `math` | `learning.py` | `update_dirichlet_A/B`, `expected_A/B`, `bayesian_model_reduction` |
| `visualization` | `config.py` | `VizConfig`, `configure`, `get_config`, `reset_config` |
| `visualization` | `plotting.py` | 6 time-series plotting functions |
| `visualization` | `matrices.py` | 9 matrix/model structure functions |
| `visualization` | `diagnostics.py` | 8 inference diagnostics functions |
| `visualization` | `simulation.py` | 5 simulation/environment functions |

### Visualization Configuration

All 28 visualisation functions read from a centralized `VizConfig` dataclass. Configure at runtime:

```python
from active_inference.visualization import configure
configure(output_dir="./output", dpi=150, font_size=18, cmap_probability="Blues")
```

Key configurable fields: `output_dir`, `dpi`, `font_size`, `title_size`, `label_size`, `tick_size`, `legend_size`, `annotation_size`, `fig_width`, `fig_height`, `cmap_probability`, `cmap_diverging`, `cmap_concentration`, `cmap_states`, `grid_alpha`, `save_format`, `style_overrides`.

---

## Test Suite

| File | Tests | Purpose |
|------|-------|---------|
| `test_agent.py` | 18 | Agent creation, inference, action, history |
| `test_environment.py` | 17 | Environment dynamics, edge cases |
| `test_free_energy.py` | 27 | VFE/EFE math, KL, entropy, surprisal, MI |
| `test_generative_model.py` | 29 | Model construction, validation, predictions |
| `test_inference.py` | 14 | State/policy inference, MMP |
| `test_integration.py` | 7 | End-to-end agent–environment loops |
| `test_learning.py` | 20 | Dirichlet updates, expected matrices, BMR |
| `test_visualization.py` | 87 | Smoke tests for all 28 vis functions |
| `test_visualization_output.py` | 27 | Generates figures to `output/` |
| `test_viz_config.py` | 7 | VizConfig defaults, configure(), output paths |

Run all 253 tests: `python -m pytest tests/ -v`

---

## Course-Specific Conventions

- **Perspective**: All content should be framed from a **computational** perspective.
- **Lab Type**: Labs use **Coding Lab** format — pymdp implementation, simulation, and visualization with Python.
- **Notation**: Use notation from [resources/notation_table.md](../resources/notation_table.md).
- **Terminology**: Use terms from [resources/glossary.md](../resources/glossary.md).
- **References**: Cite from [resources/references.md](../resources/references.md).

---

## Content Generation Standards

- All content uses **real methods** — no mocks, stubs, or placeholder implementations.
- Module content should be **modular, functional, and documented**.
- Questions must be **20 per module**, formatted as a simple numbered list.
- All 20 questions must reflect the **computational** perspective of this course.
- Quizzes must have **Part A: 7 multiple choice** + **Part B: 3 free response**.
- Labs must have **structured parts** with learning goals and `{fill:textarea}` fields.
- Lab summary tables must have **complete, untruncated** skill descriptions.
- Dashboards must be **interactive HTML5** with working JavaScript.
- Cross-references to parallel modules in other courses should use relative paths.
- Visualization functions must use the centralized `VizConfig` — no hardcoded styles.
- All figures must have ≥16pt font size for accessibility compliance.

---

## Quality Checklist

Before considering any module complete in this course:

- [ ] Content reflects the **computational** perspective (not generic)
- [ ] All 7 files are present and substantive
- [ ] No placeholder brackets `[...]` remain
- [ ] Notation matches `resources/notation_table.md`
- [ ] Terms match `resources/glossary.md`
- [ ] Lab summary table is complete (not truncated)
- [ ] Quiz questions are answerable from the module lecture
- [ ] Cross-references use correct relative paths
- [ ] Visualization uses `VizConfig` (not hardcoded styles)
- [ ] All tests pass (`python -m pytest tests/ -v`)
