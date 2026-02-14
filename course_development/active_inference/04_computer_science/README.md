# Computational Active Inference

> **Quick Navigation**: [Curriculum Home](../README.md) | [Syllabus](./syllabus.md) | [Agent Guidelines](./AGENTS.md) | [Resources](../resources/)

## Overview

Implements Active Inference algorithms in Python using a custom `active_inference` library (inspired by pymdp). Covers generative model specification (A-E matrices), belief updating, policy selection via Expected Free Energy, parameter learning, multi-agent simulation, and deep temporal planning. All code is executable and well-documented.

---

## Modules

| # | Topic | Subtitle | Description |
|---|-------|----------|-------------|
| 1 | [Systems](./01_systems/) | Generative Process vs Generative Model in pymdp | Environment setup. Generative process vs generative model. pymdp installation and basics. |
| 2 | [Agents](./02_agents/) | The Agent Class: States, Observations, and A-E Matrices | Agent class initialization. A-E matrix specification. pymdp API walkthrough. |
| 3 | [Perception](./03_perception/) | State Estimation with A-Matrix and B-Matrix | A-matrix likelihood. B-matrix transitions. Belief update implementation. Posterior visualization. |
| 4 | [Cognition](./04_cognition/) | C-Matrix (Preferences), D-Matrix (Priors), E-Matrix (Habits) | Preference specification. Prior beliefs. Habit formation. Precision tuning. |
| 5 | [Action](./05_action/) | Policy Selection and Expected Free Energy Calculation | G(π) computation. Policy selection. T-maze implementation. Exploration vs exploitation. |
| 6 | [Learning](./06_learning/) | Parameter Learning: Updating Dirichlet Concentrations | pA and pB updates. Online learning loop. Multi-episode training. Behavioral visualization. |
| 7 | [Communication](./07_communication/) | Multi-Agent Simulation and Signaling Games | Multi-agent pymdp. Observing other agents. Signaling game. Communication emergence. |
| 8 | [Planning](./08_planning/) | Deep Temporal Models, Gridworlds, and Long-Horizon Planning | Multi-step planning. Gridworld implementation. T-maze with delayed reward. Temporal depth. |

---

## Module Contents

Each module folder contains 7 files:

| File | Description |
|------|-------------|
| `module.md` | Full lecture content from a computational perspective |
| `questions.md` | 20 study questions (computational focus) |
| `practice_quiz.md` | Quiz: Part A Multiple Choice (7 questions) + Part B Free Response (3 questions) |
| `lab.md` | Coding Lab lab: pymdp implementation, simulation, and visualization with Python |
| `dashboard.html` | Interactive HTML5 dashboard with concept cards and quiz |
| `README.md` | Module overview with cross-references |
| `AGENTS.md` | Agent guidelines for content generation |

---

## Source Code: `active_inference` Python Package (v0.4.0)

The `src/active_inference/` directory is a self-contained Python package providing real, tested implementations of Active Inference algorithms. Install with `pip install -e src/`.

### Package Structure

```text
src/active_inference/
├── __init__.py              # Top-level re-exports (56 symbols: 4 classes, 48 functions, 3 config, 1 constant)
├── agent/
│   ├── generative_model.py  # GenerativeModel class (A, B, C, D, E matrices)
│   ├── agent.py             # ActiveInferenceAgent (perception–action loop)
│   └── environment.py       # DiscreteEnvironment (generative process)
├── math/
│   ├── free_energy.py       # VFE, EFE, softmax, entropy, KL divergence
│   ├── inference.py         # Variational state inference (fixed-point iteration)
│   └── learning.py          # Dirichlet updates, expected_A/B, BMR
└── visualization/
    ├── config.py            # VizConfig dataclass (runtime-configurable styling)
    ├── plotting.py          # Beliefs, VFE, prediction errors, policies (6 fns)
    ├── matrices.py          # A/B/C/D/E heatmaps, model summary, graphs (9 fns)
    ├── diagnostics.py       # Convergence, VFE/EFE components, BMR (8 fns)
    └── simulation.py        # Dashboards, trajectories, T-maze, gridworld (5 fns)
```

### Configuration

All visualization styling is runtime-configurable via `VizConfig`:

```python
from active_inference.visualization import configure, get_config

# Customise output
configure(
    output_dir="./output",
    dpi=150,
    font_size=18,
    cmap_probability="Blues",
    save_format="pdf",
)

# Read current settings
cfg = get_config()
print(cfg.output_dir, cfg.dpi)
```

#### Configurable Fields

| Field | Default | Description |
|-------|---------|-------------|
| `output_dir` | `./output` | Default save directory for figures |
| `dpi` | `100` | Figure resolution |
| `font_size` | `16` | Base font size (≥16 for accessibility) |
| `title_size` | `18` | Title font size |
| `label_size` | `16` | Axis label size |
| `tick_size` | `14` | Tick labels |
| `legend_size` | `14` | Legend text |
| `annotation_size` | `14` | In-cell annotations |
| `fig_width` | `10.0` | Default figure width (inches) |
| `fig_height` | `6.0` | Default figure height (inches) |
| `cmap_probability` | `YlOrRd` | Colour map for probability matrices |
| `cmap_diverging` | `RdBu_r` | Colour map for signed values |
| `cmap_concentration` | `viridis` | Colour map for Dirichlet concentrations |
| `save_format` | `png` | Default file extension |
| `style_overrides` | `{}` | Extra matplotlib rcParams |

### Visualization Functions (28)

| # | Function | Module | Description |
|---|----------|--------|-------------|
| 1 | `plot_beliefs` | plotting | Belief evolution q(s) over time |
| 2 | `plot_free_energy` | plotting | VFE trajectory |
| 3 | `plot_prediction_errors` | plotting | Prediction error bars |
| 4 | `plot_policy_values` | plotting | EFE per policy |
| 5 | `plot_efe_decomposition` | plotting | Risk + ambiguity split |
| 6 | `plot_learning_progress` | plotting | KL divergence learning curve |
| 7 | `plot_matrix_heatmap` | matrices | Generic annotated heatmap |
| 8 | `plot_A_matrix` | matrices | Likelihood P(o\|s) heatmap |
| 9 | `plot_B_matrix` | matrices | Transition P(s'\|s,a) heatmap(s) |
| 10 | `plot_C_preferences` | matrices | Log-preference bar chart |
| 11 | `plot_D_prior` | matrices | Prior P(s₀) bar chart |
| 12 | `plot_E_habits` | matrices | Habit prior P(π) bar chart |
| 13 | `plot_model_summary` | matrices | Multi-panel A/B/C/D summary |
| 14 | `plot_B_transition_graph` | matrices | Directed graph from B-matrix |
| 15 | `plot_dirichlet_concentration` | matrices | pA prior vs learned |
| 16 | `plot_convergence` | diagnostics | Inference convergence curve |
| 17 | `plot_vfe_components` | diagnostics | VFE decomposition (complexity − accuracy) |
| 18 | `plot_efe_components` | diagnostics | EFE decomposition (risk + ambiguity) |
| 19 | `plot_precision_sweep` | diagnostics | q(π) across γ values |
| 20 | `plot_entropy_trajectory` | diagnostics | H[q(s)] over time |
| 21 | `plot_surprise_trajectory` | diagnostics | S(o) = −ln p(o) |
| 22 | `plot_dirichlet_learning` | diagnostics | pA convergence to true A |
| 23 | `plot_bmr_results` | diagnostics | BMR ΔF bar chart |
| 24 | `plot_simulation_dashboard` | simulation | 5-panel simulation dashboard |
| 25 | `plot_environment_trajectory` | simulation | State/obs/action trajectory |
| 26 | `plot_agent_vs_environment` | simulation | Beliefs vs true states |
| 27 | `plot_tmaze` | simulation | T-maze layout renderer |
| 28 | `plot_gridworld` | simulation | Gridworld with obstacles & path |

---

## Output Directory

`output/` receives all generated figures when tests are run. Each figure is named `##_description.png` (e.g., `01_beliefs.png`). Run the output suite:

```bash
cd 04_computer_science
python -m pytest tests/test_visualization_output.py -v
```

This generates 30 PNG files using analytically accurate synthetic data.

---

## Tests

```bash
# Run all tests (253 tests)
python -m pytest tests/ -v

# Run only visualization output tests
python -m pytest tests/test_visualization_output.py -v

# Run only unit tests
python -m pytest tests/ --ignore=tests/test_visualization_output.py -v
```

| Test File | Tests | Description |
|-----------|-------|-------------|
| `test_agent.py` | 18 | Agent creation, state inference, action selection, prediction errors, history |
| `test_environment.py` | 17 | Environment creation, dynamics, history tracking, edge cases |
| `test_free_energy.py` | 27 | VFE/EFE math correctness, KL divergence, entropy, surprisal, MI |
| `test_generative_model.py` | 29 | GenerativeModel construction, validation, log-likelihood, predictions |
| `test_inference.py` | 14 | State/policy inference convergence, marginal message passing |
| `test_integration.py` | 7 | End-to-end agent–environment simulation loops |
| `test_learning.py` | 20 | Dirichlet A/B/D updates, expected matrices, entropy, BMR |
| `test_visualization.py` | 87 | Smoke/content tests for all 28 visualization functions |
| `test_visualization_output.py` | 27 | Output tests generating figures to `output/` |
| `test_viz_config.py` | 7 | VizConfig defaults, configure(), output paths, style overrides |

---

## Prerequisites

Courses 1-3 (Philosophy, Cognitive Science, Mathematics). Python programming experience (NumPy, basic OOP). Install the custom library: `pip install -e src/`.

---

## Key References

- Heins et al. (2022) pymdp: A Python library for active inference (JOSS)
- Sajid et al. (2021) Active inference: Demystified and compared
- Smith et al. (2022) A step-by-step tutorial on active inference
- Da Costa et al. (2020) Active inference on discrete state-spaces
- pymdp documentation: github.com/infer-actively/pymdp

See [resources/references.md](../resources/references.md) for the complete reference list with 82 canonical citations.

---

## Cross-References

This course is part of a 4-course sequence. Each row below covers the same topic from a different angle:

| Course | Perspective | Lab Type |
|--------|-------------|----------|
| [Philosophy](../01_philosophy/) | Philosophical foundations | Thought Experiment |
| [Cognitive Science](../02_cognitive_science/) | Neural and behavioral correlates | Case Study Analysis |
| [Mathematics](../03_math/) | Formal derivation and proof | Derivation Exercise |
| [Computer Science](../04_computer_science/) | Python implementation with pymdp | Coding Lab |

See [resources/cross_course_map.md](../resources/cross_course_map.md) for the full cross-course navigation map with links to all 32 modules.

---

## Shared Resources

| Resource | Description |
|----------|-------------|
| [Notation Table](../resources/notation_table.md) | Canonical notation used across all courses |
| [Glossary](../resources/glossary.md) | 50+ term definitions with per-course usage |
| [References](../resources/references.md) | 82 canonical citations organized by topic |
| [Cross-Course Map](../resources/cross_course_map.md) | Links to parallel modules in other courses |

---

## Documentation

| Document | Description |
|----------|-------------|
| [syllabus.md](./syllabus.md) | Full course syllabus with schedule, learning objectives, and assessment |
| [AGENTS.md](./AGENTS.md) | Agent guidelines for this course |
| [../README.md](../README.md) | Curriculum overview and learning pathway |
| [../AGENTS.md](../AGENTS.md) | Curriculum-wide conventions and standards |
