# Station: Planning (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Planning
- **Subtitle**: Hippocampal Replay, Prospection, and Model-Based Planning
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must examine the neural mechanisms of planning and prospection, with hippocampal replay and prefrontal-hippocampal interaction as the central neural substrates. Hippocampal sequence replay must be covered in depth: the original discovery of reverse replay during sharp-wave ripples in post-task rest (Foster & Wilson, 2006), forward replay of upcoming trajectories during pauses in navigation (Pfeiffer & Foster, 2013), and the critical reinterpretation that replay serves not merely memory consolidation but active planning — simulating possible future trajectories to evaluate policies before execution. Preplay of novel sequences — hippocampal activation of place cell sequences representing paths never previously traversed — must be presented as evidence for a generative model capable of constructing novel state-action trajectories, not merely replaying experienced ones. Theta sequences during active navigation must be covered: the compression of upcoming trajectory segments within individual theta cycles (approximately 125ms), interpreted as a form of compressed lookahead or short-horizon planning that sweeps through possible future states. The prefrontal-hippocampal axis in model-based decision making should be detailed: hippocampal place cells and entorhinal grid cells as providing the state space representation, prefrontal cortex as evaluating and selecting among hippocampally-simulated trajectories, and the theta-phase coupling between hippocampus and PFC as the mechanism coordinating this interaction. Mattar & Daw's (2018) account of replay prioritization must be treated as a key theoretical contribution: the proposal that the brain prioritizes which experiences to replay based on the expected improvement in future decision-making (gain), connecting replay to expected free energy minimization. The model-based vs. model-free distinction must be covered with its neural correlates: prefrontal-hippocampal circuits as implementing model-based control (flexible, but computationally expensive), dorsolateral striatum as implementing model-free habitual control (efficient, but inflexible), and evidence from Daw et al. (2011) and Gershman & Daw (2017) on the arbitration between these systems. The module must critically evaluate the limits of current evidence — particularly the difficulty of establishing that replay is causal for planning (vs. merely correlated), and the translational gap between rodent electrophysiology and human decision-making.

## Key Concepts

- **Hippocampal sequence replay as offline planning**: Sharp-wave ripple-associated replay of place cell sequences — both reverse (post-experience consolidation) and forward (pre-decision planning); evidence from rodent electrophysiology that disruption of SWRs impairs future decision-making (Jadhav et al., 2012); the reinterpretation of replay as policy evaluation via trajectory simulation
- **Preplay and prospective coding**: Activation of place cell sequences representing novel, unexperienced paths — evidence that the hippocampal generative model can construct new trajectories, not merely replay old ones; the relationship to the concept of imagination in active inference (offline policy evaluation under the generative model)
- **Theta sequences as compressed lookahead**: Within each theta cycle (~8 Hz), place cells fire in a sequence representing a spatial trajectory spanning several steps ahead of the animal's current position; interpreted as a rapid, compressed form of short-horizon planning; Gupta et al. (2012) on non-local theta sequences at choice points
- **Model-based vs. model-free neural substrates**: Prefrontal-hippocampal circuits for model-based planning (flexible, goal-directed, computationally expensive) vs. dorsolateral striatum for model-free habits (stimulus-response, efficient, inflexible); evidence from devaluation paradigms, two-step tasks, and lesion studies; arbitration mechanisms involving ventromedial PFC and inferior frontal gyrus

## Key References

- Foster, D. J., & Wilson, M. A. (2006). Reverse replay of behavioural sequences in hippocampal place cells during the awake state. *Nature*, 440(7084), 680-683.
- Pfeiffer, B. E., & Foster, D. J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. *Nature*, 497(7447), 74-79.
- Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312-325.
- Mattar, M. G., & Daw, N. D. (2018). Prioritized memory access explains planning and hippocampal replay. *Nature Neuroscience*, 21(11), 1609-1617.

## Prerequisite Modules

- Module 04 (Cognition) — understanding of prefrontal hierarchies and working memory as sustained prediction is required before examining how prefrontal-hippocampal circuits implement planning over extended temporal horizons.
- Module 05 (Action) — understanding of motor control and policy execution is required before examining how the brain evaluates and selects among possible action sequences before executing them.
- Module 06 (Learning) — understanding of synaptic plasticity and model refinement is required before examining how replay and consolidation mechanisms support the learning of generative models used for planning.

## Cross-Unit Connections

- **Advanced Theory (Module 08)**: The Theory treatment formalizes deep temporal models, sophisticated inference (recursive evaluation of expected free energy), and planning as inference. The neuroscience treatment here asks which neural mechanisms implement these computations — whether hippocampal replay corresponds to the tree search in sophisticated inference, and whether theta sequences implement the temporal depth required by deep POMDP models.
- **Philosophical Foundations (Module 08)**: The Philosophy treatment examines imagination, counterfactual reasoning, and temporal consciousness — the phenomenology of mental time travel. The neuroscience treatment here provides the mechanistic substrate: hippocampal replay and preplay as the neural implementation of imagination, and the relationship between these mechanisms and the subjective experience of planning.
- **Research Methods (Module 08)**: The Methods treatment covers open problems and research frontiers in active inference. The neuroscience treatment here highlights specific open neuroscientific questions: the causal role of replay in planning (not just correlation), the neural mechanisms of model-based/model-free arbitration, and the challenge of scaling rodent replay findings to human prospection.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
