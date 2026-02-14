# Station: Cognition (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Cognition
- **Subtitle**: Prefrontal Hierarchies, Precision, and Working Memory
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must examine how prefrontal cortex implements hierarchical generative models and how precision optimization relates to attention and cognitive control. The hierarchical organization of PFC should be detailed: posterior lateral PFC encoding lower-level action-contingency representations, anterior lateral PFC encoding more abstract rules and temporal contexts, and frontopolar cortex supporting the highest level of the generative model hierarchy (Koechlin & Summerfield, 2007; Badre & D'Esposito, 2009). The relationship between attention and precision must be treated in depth: attentional gain modulation as the neural implementation of precision optimization, with specific evidence from single-unit recordings showing multiplicative gain changes in attended neurons, and from fMRI studies demonstrating precision-like effects on BOLD signal variability. Bastos et al. (2020) on prefrontal beta-gamma interactions during working memory must be covered — beta oscillations as carrying predictive content and gamma as carrying prediction errors within prefrontal circuits, not just in sensory cortex. Working memory should be reconceptualized as sustained prediction: active maintenance of generative model states in the face of distraction, with persistent activity in PFC as encoding prior beliefs that resist updating from irrelevant sensory inputs. The mapping between computational-level descriptions (belief updating, precision weighting) and neural-level mechanisms (synaptic gain, oscillatory coupling, persistent activity) must be critically evaluated, noting the gap between elegant computational models and the complexity of actual prefrontal circuitry.

## Key Concepts

- **Hierarchical generative models in PFC**: Rostro-caudal gradient of abstraction in lateral PFC (Koechlin's cascade model); posterior PFC encoding sensorimotor contingencies, mid-lateral PFC encoding contextual rules, anterior PFC encoding temporal episodes — each level providing predictions to the level below
- **Precision and attention as gain modulation**: Attention as the optimization of precision — increasing the gain (synaptic weight) of prediction error units at attended locations; evidence from Reynolds & Heeger (2009) normalization model, Feldman & Friston (2010) precision formulation, and single-unit evidence for multiplicative scaling
- **Working memory as sustained prediction**: Persistent activity in PFC (Goldman-Rakic, 1995) reinterpreted as the maintenance of prior beliefs in a generative model; activity-silent working memory (Stokes, 2015) as precision modulation of synaptic weights rather than firing rates
- **Prefrontal-parietal networks for belief updating**: Dorsal attention network (FEF, IPS) as implementing precision-weighted sensory prediction errors; frontoparietal control network as mediating the flexible updating of generative model parameters in response to changing task demands

## Key References

- Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167-202.
- Parr, T., & Friston, K. J. (2017). Working memory, attention, and salience in active inference. *Scientific Reports*, 7, 14678.
- Kanai, R., Komura, Y., Shipp, S., & Friston, K. (2015). Cerebral hierarchies: Predictive processing, precision and the pulvinar. *Philosophical Transactions of the Royal Society B*, 370(1668), 20140169.
- Bastos, A. M., Lundqvist, M., Waite, A. S., Kopell, N., & Miller, E. K. (2020). Layer and rhythm specificity for predictive routing. *Proceedings of the National Academy of Sciences*, 117(49), 31459-31469.

## Prerequisite Modules

- Module 03 (Perception) — understanding of predictive coding in sensory cortices is required before examining how similar principles extend to prefrontal hierarchies and higher-order cognition.

## Cross-Unit Connections

- **Advanced Theory (Module 04)**: The Theory treatment covers the formal variational methods (mean-field, Bethe free energy, message passing algorithms) that cognitive inference is proposed to implement. The neuroscience treatment here asks which of these specific algorithms the prefrontal cortex actually uses, and whether neural data can discriminate between them.
- **Philosophical Foundations (Module 04)**: The Philosophy treatment examines extended cognition and the question of cognitive boundaries — whether cognitive processes extend beyond the skull. The neuroscience treatment here provides evidence about the neural substrates of cognition that bears on this question: if cognition is implemented in specific prefrontal circuits with specific connectivity, what does this imply for the extended mind thesis?
- **Research Methods (Module 04)**: The Methods treatment covers Bayesian model comparison and structure learning — the tools for comparing competing computational models of cognition. The neuroscience treatment here provides the neural datasets (prefrontal recordings, working memory fMRI, attentional gain measurements) that constrain model selection.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
