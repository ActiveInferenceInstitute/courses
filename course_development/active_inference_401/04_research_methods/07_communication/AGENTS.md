# Station: Communication (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Communication
- **Subtitle**: Studying Social Inference Experimentally
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must cover the experimental methods for studying social active inference — how interacting agents infer each other's beliefs, intentions, and strategies through observation and communication. The primary paradigms are hyperscanning (simultaneous neuroimaging of two or more interacting individuals) and computational models of social learning fitted to behavioral data from interactive tasks. Students should learn the practical workflow for hyperscanning studies using fMRI, EEG, and fNIRS (Hasson et al., 2012): experimental design constraints (e.g., temporal synchronization, shared vs. independent task components, controlling for stimulus-driven coupling vs. genuine social inference), analysis methods (inter-brain synchrony, Granger causality, dynamic causal modeling of coupled brains), and the substantial methodological challenges (small effective sample sizes because each data point is a dyad, motion artifacts in interactive settings, the difficulty of controlling for non-social explanations of inter-brain coupling). The canonical behavioral paradigm is the multi-round trust game, which Diaconescu et al. (2014) analyzed using the hierarchical Gaussian filter (HGF) to model belief updating about a partner's trustworthiness. Students should understand the HGF as a computational model of hierarchical social learning (Mathys et al., 2014), including parameter estimation, model comparison against simpler (non-hierarchical) alternatives, and computational phenotyping of social cognitive traits (e.g., volatility estimation as a marker of social anxiety). Agent-based simulation of multi-agent active inference systems should also be covered as a tool for generating predictions and testing theoretical claims about generative model alignment.

## Key Concepts

- **Hyperscanning paradigms**: Simultaneous neuroimaging (fMRI, EEG, fNIRS) of two or more interacting individuals to study inter-brain coupling during social inference; methodological considerations include temporal synchronization, baseline conditions (non-interactive control), and analysis methods (inter-brain coherence, phase-locking value, wavelet transform coherence)
- **Computational phenotyping of social learning**: Using fitted parameters of social learning models (e.g., HGF volatility learning rate $\omega$, social precision parameters) as quantitative measures of individual differences in social cognition; validating these measures against clinical scales (social anxiety, autism traits) and testing for group differences in computational parameters
- **Two-player trust games**: The multi-round trust game as a canonical paradigm for studying social inference — one player (investor) decides how much to invest, the other (trustee) decides how much to return; computational models track belief updating about the partner's strategy as a function of observed outcomes (Diaconescu et al., 2014)
- **Hierarchical Gaussian filter (HGF)**: A hierarchical Bayesian model for online learning in volatile environments (Mathys et al., 2014); in social contexts, the HGF models how agents update beliefs about a partner's strategy (level 1), the volatility of that strategy (level 2), and meta-volatility (level 3); parameters include learning rates at each level and precision weighting of prediction errors
- **Agent-based social simulation**: Simulating populations of active inference agents that interact through shared Markov blankets to generate predictions about emergent social dynamics, convention formation, and generative model alignment; useful for theory development and for generating quantitative predictions to test empirically

## Key References

- Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S., & Keysers, C. (2012). Brain-to-brain coupling: A mechanism for creating and sharing a social world. *Trends in Cognitive Sciences*, 16(2), 114-121.
- Diaconescu, A. O., Mathys, C., Weber, L. A. E., Daunizeau, J., Kasper, L., Lomakina, E. I., ... & Stephan, K. E. (2014). Inferring on the intentions of others by hierarchical Bayesian learning. *PLOS Computational Biology*, 10(9), e1003810.
- Mathys, C. D., Lomakina, E. I., Daunizeau, J., Iglesias, S., Brodersen, K. H., Friston, K. J., & Stephan, K. E. (2014). Uncertainty in perception and the hierarchical Gaussian filter. *Frontiers in Human Neuroscience*, 8, 825.
- Behrens, T. E. J., Hunt, L. T., Woolrich, M. W., & Rushworth, M. F. S. (2008). Associative learning of social value. *Nature*, 456(7219), 245-249.
- Friston, K. J., & Frith, C. D. (2015). Active inference, communication and hermeneutics. *Cortex*, 68, 129-143.
- Schilbach, L., Timmermans, B., Reddy, V., Costall, A., Bente, G., Schlicht, T., & Vogeley, K. (2013). Toward a second-person neuroscience. *Behavioral and Brain Sciences*, 36(4), 393-414.

## Prerequisite Modules

- Module 02: Agents (provides the PyMDP agent modeling and parameter fitting framework that multi-agent simulation extends to social contexts)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/07_communication/module.md](../../03_advanced_theory/07_communication/module.md)): Formalizes multi-agent active inference via shared Markov blankets, coupled dynamical systems, and mean-field game theory — this module designs experiments and simulations to test those formal predictions empirically
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/07_communication/module.md](../../02_neuroscientific_frontiers/07_communication/module.md)): Reviews mirror neuron systems, mentalizing networks, and social prediction error signals — this module provides the hyperscanning and computational phenotyping tools to study those neural systems during real social interaction
- **Philosophical Foundations** ([../../01_philosophical_foundations/07_communication/module.md](../../01_philosophical_foundations/07_communication/module.md)): Examines shared intentionality, language as active inference, and the social Markov blanket — this module operationalizes those concepts into testable experimental paradigms (trust games, communication tasks, convention formation experiments)

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
