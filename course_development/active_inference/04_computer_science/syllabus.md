# Course 4: Computational Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md) | [Resources](../resources/) | [Agent Guidelines](./AGENTS.md)

## Course Description

This course implements Active Inference algorithms in Python using a custom `active_inference` library (inspired by pymdp). Students will build, run, and analyze discrete-state-space Active Inference agents from scratch. Topics include generative model specification (A-E matrices), belief updating via variational inference, policy selection via Expected Free Energy, parameter learning with Dirichlet updates, multi-agent simulation, and deep temporal planning. All code is executable, well-documented, and builds progressively across modules.

---

## Prerequisites

- Courses 1-3 (Philosophy, Cognitive Science, and Mathematics of Active Inference)
- Python programming: comfortable with NumPy, basic OOP (classes, methods), matplotlib
- The course uses a custom `active_inference` library bundled with the curriculum (see `src/active_inference/`)
- Recommended: Jupyter notebooks for interactive development

> **Note**: All source paths (e.g., `src/active_inference/`) are relative to the `04_computer_science/` directory.

---

## Course Schedule

| Week | Module | Topic | Implementation Focus | Key Components | Deliverables |
|------|--------|-------|---------------------|----------------|-------------|
| 1 | [Module 1](./01_systems/) | **Systems** | Environment setup, generative process vs model | `DiscreteEnvironment`, observation generation | Lab 1, Quiz 1 |
| 2 | [Module 2](./02_agents/) | **Agents** | Agent class, A-E matrix specification | `GenerativeModel`, `ActiveInferenceAgent`, T-maze | Lab 2, Quiz 2 |
| 3 | [Module 3](./03_perception/) | **Perception** | Belief updating, A-matrix likelihood | `run_state_inference()`, posterior visualization | Lab 3, Quiz 3 |
| 4 | [Module 4](./04_cognition/) | **Cognition** | Preferences (C), priors (D), habits (E) | C, D, E vector construction, precision γ | Lab 4, Quiz 4 |
| 5 | [Module 5](./05_action/) | **Action** | Policy selection, G(π) computation | `compute_efe()`, softmax policy selection | Lab 5, Quiz 5 |
| 6 | [Module 6](./06_learning/) | **Learning** | Parameter learning, Dirichlet updates | `update_dirichlet_A()`, `update_dirichlet_B()` | Lab 6, Quiz 6 |
| 7 | [Module 7](./07_communication/) | **Communication** | Multi-agent simulation, signaling games | Multi-agent loop, mutual information tracking | Lab 7, Quiz 7 |
| 8 | [Module 8](./08_planning/) | **Planning** | Deep temporal models, gridworlds | Temporal depth T, sophisticated inference | Lab 8, Quiz 8, Final Project |

---

## Learning Objectives

By the end of this course, you should be able to:

1. **Build** a complete Active Inference agent with A, B, C, D, and E matrices using the `active_inference` library
2. **Implement** state estimation using variational belief updating (fixed-point iteration)
3. **Compute** Expected Free Energy (G) and select policies via softmax
4. **Simulate** the canonical T-maze benchmark with exploration-exploitation tradeoff
5. **Implement** online parameter learning through Dirichlet concentration updates (pA, pB)
6. **Design** multi-agent simulations where agents observe and influence each other
7. **Build** deep temporal models for planning over extended time horizons
8. **Visualize** beliefs, prediction errors, EFE components, and free energy trajectories

---

## Assessment Components

| Component | Description | Frequency |
|-----------|-------------|-----------|
| Practice Quizzes | Part A: 7 multiple choice + Part B: 3 free response per module (code comprehension) | Weekly (8 total) |
| Coding Labs | Hands-on implementation with running code | Weekly (8 total) |
| Study Questions | 20 computational questions per module | Weekly (8 total) |
| Final Project | Extended implementation project | End of course |

### Final Project Options

1. **Custom Environment**: Design and implement a novel Active Inference environment (not T-maze or gridworld) that demonstrates a specific cognitive phenomenon (e.g., foraging, social dilemma, perceptual rivalry)
2. **Multi-Agent System**: Build a multi-agent simulation that demonstrates emergent communication, cooperation, or competition between Active Inference agents
3. **Benchmarking Study**: Compare Active Inference agents against reinforcement learning baselines (Q-learning, SARSA) on a standard task, measuring sample efficiency, exploration behavior, and asymptotic performance
4. **Visualization Tool**: Build an interactive dashboard that visualizes the internal dynamics of an Active Inference agent in real time (beliefs, EFE components, policy probabilities, learning curves)

---

## Technical Setup

```bash
# Navigate to the curriculum's CS course
cd active_inference/04_computer_science/

# The custom active_inference library is in src/
# Add to Python path:
import sys
sys.path.insert(0, 'src')

# Verify installation
from active_inference.agent import GenerativeModel, ActiveInferenceAgent
from active_inference.math import compute_vfe, compute_efe
from active_inference.visualization import plot_beliefs, plot_free_energy
```

### Dependencies

```bash
pip install numpy matplotlib scipy jupyter
```

---

## Resources

| Resource | Purpose |
|----------|---------|
| [Notation Table](../resources/notation_table.md) | Mapping between mathematical notation and code variables |
| [Glossary](../resources/glossary.md) | Definitions with implementation notes |
| [References](../resources/references.md) | Key papers and tutorial references |
| [Cross-Course Map](../resources/cross_course_map.md) | Navigate to conceptual counterparts in other courses |
| `src/active_inference/` | Custom library: agent/, math/, visualization/ subpackages |
| [pymdp GitHub](https://github.com/infer-actively/pymdp) | Foundational library that inspired this implementation |
| [pymdp JOSS Paper](https://joss.theoj.org/papers/10.21105/joss.04098) | Heins et al. (2022) — pymdp publication |
