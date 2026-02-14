# Station: Agents (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Agents
- **Subtitle**: The Neural Architecture of Active Inference Agents
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must examine which neural circuits implement the core components of active inference agents. It should detail the prefrontal cortex as the substrate for hierarchical generative models — specifying the roles of dorsolateral PFC in model maintenance, ventromedial PFC in outcome evaluation, and orbitofrontal cortex in state inference. The basal ganglia should be treated as the neural implementation of policy selection: the direct and indirect pathways as competing policy channels, the subthalamic nucleus as a "hold" signal preventing premature commitment, and the ventral striatum as encoding expected free energy. Thalamic nuclei (pulvinar, mediodorsal) should be covered as precision modulators controlling the gain of cortical prediction error signals. The module must present specific evidence linking dopamine to precision and confidence signals — including Schwartenbeck et al.'s (2015) fMRI evidence for dopaminergic encoding of Bayesian surprise and FitzGerald et al.'s (2015) work on dopamine and precision in hierarchical inference. The mapping between POMDP matrices (A, B, C, D, E) and neural substrates must be presented and critically evaluated, noting where the mapping is empirically supported versus where it remains a computational-level proposal.

## Key Concepts

- **Prefrontal-basal ganglia circuits for policy selection**: The cortico-striatal-thalamic loop as implementing policy evaluation and selection; direct pathway (Go/policy execution) vs. indirect pathway (NoGo/policy suppression); hyperdirect pathway for urgency signals
- **Dopamine as precision signaling**: Phasic dopamine as encoding precision-weighted prediction errors (departing from simple reward prediction error accounts); tonic dopamine as setting the precision of prior beliefs about policies (the gamma parameter)
- **Cortico-thalamic loops and precision modulation**: The pulvinar and mediodorsal thalamus as gain controllers that modulate the weight of ascending prediction errors relative to descending predictions
- **Neural POMDP implementation**: Mapping the A matrix to sensory cortex likelihood representations, B matrix to hippocampal/prefrontal transition models, C matrix to insular/orbitofrontal preference encoding, D matrix to hippocampal priors, E matrix to habitual policy representations in dorsal striatum

## Key References

- Schwartenbeck, P., FitzGerald, T. H. B., Dolan, R. J., & Friston, K. (2015). Exploration, novelty, surprise, and free energy minimization. *Frontiers in Psychology*, 4, 710.
- FitzGerald, T. H. B., Dolan, R. J., & Friston, K. (2015). Dopamine, reward learning, and active inference. *Frontiers in Computational Neuroscience*, 9, 136.
- Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). Active inference: A process theory. *Neural Computation*, 29(1), 1-49.
- Parr, T., & Friston, K. J. (2018). The anatomy of inference: Generative models and brain structure. *Cerebral Cortex*, 28(4), 1254-1270.

## Prerequisite Modules

- Module 01 (Systems) — understanding of neural systems as dynamical systems at NESS is required before examining how specific circuits implement agent-level computations.

## Cross-Unit Connections

- **Advanced Theory (Module 02)**: The Theory treatment formalizes POMDPs, belief MDPs, and information geometry on statistical manifolds. The neuroscience treatment here asks which neural circuits instantiate these formal structures, and whether the neural evidence constrains or underdetermines the mathematical framework.
- **Philosophical Foundations (Module 02)**: The Philosophy treatment debates the conditions for genuine agency — autonomy, intentionality, the boundary problem. The neuroscience treatment here examines what neural architecture is necessary for a system to qualify as an active inference agent, and whether the prefrontal-basal ganglia system is sufficient.
- **Research Methods (Module 02)**: The Methods treatment covers building and validating agent models in PyMDP, including parameter recovery and model inversion. The neuroscience treatment here provides the neural data (fMRI, single-unit recordings, pharmacological manipulations) that constrain and test those computational models.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
