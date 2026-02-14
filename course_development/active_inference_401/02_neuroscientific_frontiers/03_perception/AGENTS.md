# Station: Perception (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Perception
- **Subtitle**: Predictive Coding in Cortical Hierarchies
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must cover the canonical microcircuit model for predictive coding in cortical hierarchies in full mechanistic detail. The Bastos et al. (2012) and Shipp (2016) proposals must be presented with explicit specification of cell types and laminar roles: superficial pyramidal cells in layers 2/3 as carrying prediction errors (ascending, associated with gamma-band oscillations), deep pyramidal cells in layers 5/6 as carrying predictions (descending, associated with beta-band oscillations), and layer 4 stellate cells as the input relay for feedforward prediction errors. The module must review the foundational evidence from Rao & Ballard (1999) on end-stopping and extra-classical receptive field effects in V1 as signatures of predictive coding, and extend to auditory predictive coding: the mismatch negativity (MMN) as an auditory prediction error generated in primary auditory cortex and propagated to frontal sources, and the P300 as a higher-order model updating signal. The role of neuromodulatory systems in precision weighting must be covered in detail: acetylcholine (via muscarinic and nicotinic receptors) as modulating sensory precision, dopamine (via D1/D2 receptors in PFC) as modulating the precision of prior beliefs, and noradrenaline as signaling unexpected uncertainty (volatility). The evidence must be critically evaluated — noting that while the canonical microcircuit is theoretically elegant, direct laminar-resolved evidence in humans remains limited, and alternative accounts of MMN (adaptation, deviance detection without prediction) must be addressed.

## Key Concepts

- **Canonical microcircuit for predictive coding**: The cortical column as a unit implementing prediction error computation (superficial pyramidal cells) and prediction generation (deep pyramidal cells), with inhibitory interneurons (PV, SST, VIP subtypes) playing distinct roles in gain control and precision modulation
- **Mismatch negativity (MMN) and P300 as prediction error signatures**: MMN as a pre-attentive auditory prediction error (peaking ~150-200ms, generated in superior temporal cortex with frontal contributions); P300 as a later, attention-dependent model-updating signal; the oddball, roving, and omission paradigms as experimental tools
- **Precision weighting via neuromodulators**: Acetylcholine increasing sensory precision (gain of superficial pyramidal cells), dopamine modulating prior precision (gain of deep pyramidal cells), noradrenaline signaling environmental volatility — each with specific receptor subtypes and laminar targets
- **Oscillatory signatures of predictive coding**: Gamma-band (30-100 Hz) oscillations associated with bottom-up prediction errors, beta-band (13-30 Hz) oscillations associated with top-down predictions; Granger causality and directed transfer function analyses supporting this directional asymmetry

## Key References

- Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79-87.
- Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695-711.
- Shipp, S. (2016). Neural elements for predictive coding. *Frontiers in Psychology*, 7, 1792.
- Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience*, 4, 215.

## Prerequisite Modules

- Module 02 (Agents) — understanding of the neural architecture of active inference agents is required before examining how perceptual inference is implemented in specific cortical circuits.

## Cross-Unit Connections

- **Advanced Theory (Module 03)**: The Theory treatment derives predictive coding update rules from variational free energy minimization, showing the mathematical necessity of prediction error and prediction signals. The neuroscience treatment here asks whether cortical circuits actually implement these specific update rules, and what the empirical constraints are.
- **Philosophical Foundations (Module 03)**: The Philosophy treatment examines the phenomenology of perception — Merleau-Ponty's embodied perception, the compatibility thesis between predictive processing and phenomenology. The neuroscience treatment here provides the mechanistic substrate: what is it about cortical circuit organization that might give rise to perceptual experience?
- **Research Methods (Module 03)**: The Methods treatment covers designing neuroimaging paradigms (oddball, roving, omission designs) and using DCM to test predictive coding hypotheses. The neuroscience treatment here provides the neural phenomena (MMN, repetition suppression, extra-classical RF effects) that those experimental designs target.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
