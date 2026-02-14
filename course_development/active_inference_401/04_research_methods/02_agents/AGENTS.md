# Station: Agents (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Agents
- **Subtitle**: Building and Validating Agent Models
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must serve as a practical guide to building, fitting, and validating active inference agents using the PyMDP framework (Heins et al., 2022). Students should learn the full workflow: defining the POMDP generative model (specifying $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$, $\mathbf{E}$ matrices), running inference and action selection, simulating synthetic behavioral data, and fitting model parameters to empirical behavioral data via grid search or optimization. A critical component is parameter recovery analysis (Wilson & Collins, 2019): simulating data from known parameters, attempting to recover them, and characterizing the conditions under which recovery fails (e.g., parameter correlations, flat likelihood surfaces, insufficient trial counts). The module should also cover computational phenotyping — using fitted model parameters as individual-difference measures for clinical or cognitive profiling (Palminteri et al., 2017) — and address the practical question of when active inference agents are preferable to simpler reinforcement learning or Bayesian models.

## Key Concepts

- **PyMDP implementation**: Defining the POMDP generative model in code — constructing the likelihood matrix $\mathbf{A}$, transition matrices $\mathbf{B}^{(a)}$, preference vector $\mathbf{C}$, initial state prior $\mathbf{D}$, and habit vector $\mathbf{E}$; running belief updating and policy selection via expected free energy $G(\pi)$
- **Model inversion for behavioral data**: Fitting active inference agent parameters to empirical choice and reaction time data using maximum likelihood estimation, maximum a posteriori estimation, or variational Bayes; model comparison against alternative accounts (RL, Bayesian ideal observer)
- **Parameter recovery**: The practice of simulating synthetic datasets from known ground-truth parameters, fitting the model to recover those parameters, and evaluating recovery quality via correlation, bias, and coverage; diagnosing when and why recovery fails (trade-offs between $\gamma$ and $\mathbf{C}$, for instance)
- **Agent-based simulation**: Using populations of active inference agents to generate predictions about group-level behavioral distributions, explore parameter spaces, and conduct power analyses for planned experiments
- **Computational phenotyping**: Extracting individual model parameters (e.g., policy precision $\gamma$, prior preference strength, learning rates) as quantitative measures of cognitive style or clinical phenotype; validating that these parameters have adequate test-retest reliability and discriminant validity

## Key References

- Heins, C., Millidge, B., Da Costa, L., et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software*, 7(73), 4098.
- Smith, R., Friston, K. J., & Whyte, C. J. (2022). A step-by-step tutorial on active inference and its application to empirical data. *Journal of Mathematical Psychology*, 107, 102632.
- Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife*, 8, e49547.
- Palminteri, S., Wyart, V., & Koechlin, E. (2017). The importance of falsification in computational cognitive modeling. *Trends in Cognitive Sciences*, 21(6), 425-433.
- Schwartenbeck, P., FitzGerald, T. H. B., & Dolan, R. J. (2016). Neural signals encoding shifts in beliefs. *NeuroImage*, 125, 578-586.

## Prerequisite Modules

- Module 01: Systems (establishes the dynamical systems foundation and NESS framework that agents are embedded within)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/02_agents/module.md](../../03_advanced_theory/02_agents/module.md)): Formalizes POMDPs, belief MDPs, and information geometry of agent models — this module implements and validates those formal structures computationally
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/02_agents/module.md](../../02_neuroscientific_frontiers/02_agents/module.md)): Maps active inference agent components to neural circuits (prefrontal-basal ganglia, dopamine as precision) — this module provides the behavioral modeling tools to test those neural mappings
- **Philosophical Foundations** ([../../01_philosophical_foundations/02_agents/module.md](../../01_philosophical_foundations/02_agents/module.md)): Debates the conditions for genuine agency vs. mere system dynamics — this module operationalizes those conditions as model comparison questions (does an agent model fit better than a reactive model?)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
