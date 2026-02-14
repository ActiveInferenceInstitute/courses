# Station: Action (Neuroscientific Frontiers)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Predictive processing, precision, neural dynamics
- **Topic**: Action
- **Subtitle**: Motor Control and Active Inference in the Brain
- **Lab Style**: Paper Review
- **Audience**: PhD students and researchers
- **Tone**: Empirical, evidence-driven, mechanistically specific

## Content Guidance

This module must present the active inference account of motor control: proprioceptive predictions issued by motor cortex are fulfilled by classical reflex arcs at the spinal level, making action equivalent to prediction error minimization in the proprioceptive domain. Adams et al. (2013) must be covered in detail — their argument that descending corticospinal signals are predictions of proprioceptive states (not motor commands), and that alpha motor neuron activation in the spinal cord represents the minimization of proprioceptive prediction errors via the stretch reflex. The cerebellum must be treated as a forward model generating predicted sensory consequences of motor commands, drawing on Wolpert et al. (1998) and the broader internal models framework, while reinterpreting cerebellar function through the active inference lens: the cerebellum as computing expected prediction errors to enable rapid online correction. The motor hierarchy must be specified from cortex (abstract action goals and temporal sequences in premotor cortex) through brainstem (postural and locomotor programs) to spinal cord (segmental reflexes implementing prediction error minimization). Oculomotor control should serve as a key test case: saccadic eye movements as a paradigmatic example of active inference, with evidence from Parr & Friston (2018) on how saccade generation follows from visual prediction errors weighted by precision. Active sensing (saccades, whisking, sniffing) must be treated as the motor side of perceptual inference. The module must critically evaluate this account against classical motor control theories — particularly optimal feedback control (Todorov & Jordan, 2002) and the question of whether active inference offers empirically distinguishable predictions or is merely a redescription.

## Key Concepts

- **Spinal reflexes as proprioceptive prediction error minimization**: Descending corticospinal projections as proprioceptive predictions; alpha motor neuron activation as the mechanism that minimizes the discrepancy between predicted and actual proprioceptive input; the stretch reflex as the fundamental motor "inference" mechanism
- **Cerebellar forward models**: The cerebellum as computing predicted sensory consequences of efference copies, enabling rapid correction of movement errors; Purkinje cell simple and complex spikes as encoding predicted and actual sensory states, respectively; the climbing fiber as a teaching signal for updating forward model parameters
- **Motor hierarchy**: Premotor cortex (action sequences, abstract goals) to primary motor cortex (specific movement parameters) to brainstem (postural programs, central pattern generators) to spinal cord (segmental reflexes) — each level providing progressively more concrete proprioceptive predictions
- **Oculomotor control and active sensing**: Saccadic eye movements as driven by visual prediction errors weighted by epistemic value; superior colliculus and frontal eye fields as implementing precision-weighted saccade planning; active sensing (saccades, whisking, head movements) as the motor component of perceptual inference

## Key References

- Adams, R. A., Shipp, S., & Friston, K. J. (2013). Predictions not commands: Active inference in the motor system. *Brain Structure and Function*, 218(3), 611-643.
- Friston, K. J., Daunizeau, J., Kilner, J., & Kiebel, S. J. (2010). Action and behavior: A free-energy formulation. *Biological Cybernetics*, 102(3), 227-260.
- Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338-347.
- Parr, T., & Friston, K. J. (2018). Active inference and the anatomy of oculomotion. *Neuropsychologia*, 111, 334-343.

## Prerequisite Modules

- Module 03 (Perception) — understanding of predictive coding and prediction error signaling in sensory cortices is essential before examining how motor systems fulfill predictions through action, as the active inference account of motor control is the complement of the perceptual inference account.

## Cross-Unit Connections

- **Advanced Theory (Module 05)**: The Theory treatment formalizes action through path integrals, KL control, and the derivation of optimal policies from expected free energy. The neuroscience treatment here asks how these formally derived control laws map onto actual motor circuits — whether spinal reflexes truly implement the gradient descent prescribed by the theory.
- **Philosophical Foundations (Module 05)**: The Philosophy treatment examines enactivism and affordances — the idea that perception and action are constitutively coupled. The neuroscience treatment here provides mechanistic detail: how does the sensorimotor loop actually work at the circuit level, and does this support the enactivist claim of constitutive coupling or merely causal interaction?
- **Research Methods (Module 05)**: The Methods treatment covers designing motor control experiments (reaching paradigms, saccade tasks, force field adaptation) and fitting active inference models to behavioral data. The neuroscience treatment here provides the neural signals (corticospinal recordings, cerebellar unit activity, EMG) that complement the behavioral measures.

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
