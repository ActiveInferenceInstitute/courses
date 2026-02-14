# Module 08: Planning -- Autonomous Navigation and Mission Planning

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## Overview

This module covers **planning** in robotic systems as expected free energy minimization over future action sequences. Unlike classical planners that optimize a single cost function, Active Inference planning naturally integrates goal-seeking behavior (pragmatic value) with information-gathering behavior (epistemic value). We examine hierarchical planning architectures that span from high-level mission planning to low-level trajectory optimization.

## Learning Objectives

1. **Formulate** robotic planning as expected free energy minimization, decomposing the objective into pragmatic and epistemic value terms.
2. **Compare** classical planning algorithms (A*, RRT, potential fields) with Active Inference planning, identifying when each approach is advantageous.
3. **Design** hierarchical planning systems with task-level and navigation-level planners connected through a hierarchical generative model.
4. **Analyze** how different types of uncertainty (state, map, goal) affect planning decisions and drive information-seeking behavior.
5. **Implement** an Active Inference path planner in pseudocode that evaluates candidate trajectories by their expected free energy.
6. **Evaluate** planning under realistic constraints: computational budgets, replanning frequency, and the receding horizon principle.

## Key Concepts

- Planning as expected free energy minimization
- Pragmatic value (goal-seeking) vs. epistemic value (exploration)
- Hierarchical planning: mission level and navigation level
- Planning under state, map, and goal uncertainty
- Receding horizon planning and continuous replanning
- The exploration-exploitation trade-off as a natural consequence of free energy

## Prerequisites

- Module 04: Cognition (world models, SLAM)
- Module 05: Action (control execution)
- Familiarity with path planning concepts (optional but helpful)

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture: Autonomous Navigation and Mission Planning |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Answer) |
| [lab.md](./lab.md) | Lab: Planning Algorithm Design |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Cross-References

- **Previous module**: [Communication](../07_communication/README.md) -- coordinated multi-robot planning
- **Related in Course 3**: [Control & Estimation: Planning](../../03_control_estimation/08_planning/README.md) -- MPC and optimal control formulations
- **Related in Course 4**: [Autonomous Agents: Planning](../../04_autonomous_agents/08_planning/README.md) -- fully autonomous planning systems
- **Resources**: [Notation](../../resources/notation_table.md) | [Glossary](../../resources/glossary.md)
