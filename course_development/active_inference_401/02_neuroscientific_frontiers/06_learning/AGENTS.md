# Station: Learning (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Learning
- **Subtitle**: Synaptic Plasticity, Neuromodulation, and Bayesian Learning
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must examine how the brain learns and refines generative models, covering multiple timescales from rapid synaptic modification to slow structural reorganization. Hebbian and anti-Hebbian plasticity should be reinterpreted as free energy minimization: Hebbian LTP as strengthening connections that reduce prediction error (increasing the accuracy of the generative model), and anti-Hebbian plasticity as decorrelation that reduces redundancy in internal representations. The module must address the dopamine debate head-on — Schultz's (1997) reward prediction error interpretation vs. Friston's precision/confidence interpretation, presenting the empirical evidence for each: phasic dopamine responses to unexpected rewards (Schultz), but also dopamine responses to salient non-rewarding stimuli (Bromberg-Martin et al., 2010) and the role of dopamine in precision-weighted belief updating (FitzGerald et al., 2015). Acetylcholine must be covered as modulating sensory precision: basal forebrain cholinergic projections to cortex increasing the gain of sensory inputs (Gil et al., 1997), enabling more precise sensory evidence to drive learning. Sleep consolidation should be presented as offline optimization of the generative model: hippocampal sharp-wave ripples replaying recent experience (Diekelmann & Born, 2010), cortical slow oscillations coordinating systems-level memory consolidation, and the role of sleep spindles in thalamocortical plasticity — all reinterpreted as the brain performing variational inference and model compression during offline states. The empirical Bayes interpretation of cortical hierarchies (Friston & Frith, 2015) must be covered: each cortical level learns hyperparameters that serve as empirical priors for the level below, creating a hierarchy of increasingly abstract regularities. The module must critically evaluate where the Bayesian learning framework offers genuinely new predictions versus where it merely provides an alternative vocabulary for well-known plasticity mechanisms.

## Key Concepts

- **Hebbian plasticity as VFE minimization**: LTP and LTD as synaptic weight changes that minimize prediction error; spike-timing-dependent plasticity (STDP) as implementing a temporal version of prediction error minimization; the relationship between Hebbian learning rules and gradient descent on variational free energy
- **Dopamine: reward prediction error vs. precision signaling**: Schultz's canonical RPE account (phasic dopamine = reward prediction error) vs. the active inference interpretation (dopamine = precision of prior policies); evidence from optogenetic studies, pharmacological manipulations, and computational modeling that bears on this distinction
- **Acetylcholine and sensory precision**: Basal forebrain cholinergic projections to cortex as modulating the gain (precision) of sensory prediction errors; cholinergic effects on cortical processing modes (desynchronization, enhanced signal-to-noise); implications for learning rate modulation during uncertain environments
- **Sleep consolidation as offline model optimization**: Sharp-wave ripples as compressed replay of generative model trajectories; slow oscillation-spindle coupling as coordinating cortical-hippocampal model transfer; REM sleep as testing model robustness through endogenous prediction error generation

## Key References

- Friston, K. (2005). A theory of cortical responses. *Philosophical Transactions of the Royal Society B*, 360(1456), 815-836.
- Gershman, S. J., & Daw, N. D. (2017). Reinforcement learning and episodic memory in humans and animals: An integrative framework. *Annual Review of Psychology*, 68, 101-128.
- Diekelmann, S., & Born, J. (2010). The memory function of sleep. *Nature Reviews Neuroscience*, 11(2), 114-126.
- Friston, K., & Frith, C. (2015). A duet for one. *Consciousness and Cognition*, 36, 390-405.

## Prerequisite Modules

- Module 04 (Cognition) — understanding of hierarchical generative models in PFC and precision mechanisms is required before examining how these models are learned and refined through synaptic plasticity, neuromodulation, and sleep consolidation.

## Cross-Unit Connections

- **Advanced Theory (Module 06)**: The Theory treatment formalizes Bayesian model reduction, structure learning, and the computation of model evidence bounds. The neuroscience treatment here asks which neural plasticity mechanisms implement these formal operations — whether synaptic pruning corresponds to Bayesian model reduction, and whether sleep consolidation implements evidence maximization.
- **Philosophical Foundations (Module 06)**: The Philosophy treatment examines the epistemology of model revision — Kuhnian paradigm shifts, abductive inference, Bayesian epistemology. The neuroscience treatment here provides mechanistic grounding: what are the neural constraints on how generative models can be revised, and do these constraints have epistemological implications?
- **Research Methods (Module 06)**: The Methods treatment covers parameter estimation, model fitting, and validation techniques (EM, variational Bayes, posterior predictive checks). The neuroscience treatment here provides the neural learning data (plasticity time courses, neuromodulatory effects, sleep-dependent consolidation) that these computational methods must account for.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
