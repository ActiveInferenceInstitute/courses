# Section Lab: Neural Implementations of Active Inference

> **Quick Navigation**: [Course Home](./README.md) | [Curriculum Home](../README.md)

## Objective

This integrative lab synthesizes all eight modules from the Computational Neuroscience course. You will analyze how neural circuits implement Active Inference processes, working with conceptual models of neural dynamics, predictive coding architectures, and neuromodulatory systems.

## Prerequisites

- Completion of all eight Computational Neuroscience modules (01_systems through 08_planning)
- Familiarity with neural population dynamics, predictive coding, cortical hierarchies, neuromodulation, and Bayesian brain theory
- Basic comfort with reading equations and interpreting simulation plots

---

## Part 1: Neural Dynamical Systems (Simulation Analysis)

**Scenario**: Consider a neural population in primary visual cortex (V1) receiving input from the lateral geniculate nucleus (LGN). The population exhibits oscillatory dynamics in the gamma band (30-80 Hz) when processing visual stimuli.

**1a.** Describe this neural population as a dynamical system. What are the state variables? What constitutes the attractor landscape? How do excitatory-inhibitory interactions give rise to oscillatory attractors? Draw on the concepts from Module 01 (Systems) to frame your answer.

{fill:textarea}

**1b.** When a visual stimulus is presented, the attractor landscape changes. Explain how this perturbation relates to the concept of prediction error in the Active Inference framework. How does the neural population's movement toward a new attractor correspond to perceptual inference?

{fill:textarea}

---

## Part 2: Predictive Coding Architecture (Circuit Analysis)

**Scenario**: A two-level cortical hierarchy (V1 and V2) processes a visual scene. V2 sends top-down predictions to V1, which sends bottom-up prediction errors to V2.

**2a.** Diagram the information flow between V1 and V2 in terms of predictive coding. Identify which neural populations carry predictions (deep pyramidal cells), which carry prediction errors (superficial pyramidal cells), and how precision weighting is implemented via synaptic gain modulation. Use the NMDA/AMPA receptor framework from Module 03 (Perception).

{fill:textarea}

**2b.** A novel object appears in the visual field. Trace the neural response through the hierarchy over the first 200 milliseconds. When does prediction error peak? How does the hierarchy settle into a new steady state? What happens to gamma-band activity in V1 during this process, and why does this relate to precision weighting?

{fill:textarea}

---

## Part 3: Neuromodulation and Action Selection (Integration Exercise)

**Scenario**: A participant in a neuroscience experiment must decide between pressing a left button (safe, small reward) or a right button (risky, large reward). Dopaminergic and noradrenergic systems modulate the decision.

**3a.** Explain how dopamine implements precision weighting on prior preferences (the C vector in Active Inference). A participant with higher tonic dopamine levels might show different exploration-exploitation behavior. Describe the neural mechanism using concepts from Module 05 (Action) and Module 04 (Cognition).

{fill:textarea}

**3b.** Now consider the role of norepinephrine (locus coeruleus system) in modulating the precision of sensory evidence. Under the Active Inference framework, how does norepinephrine balance between exploiting current beliefs and being open to surprising new evidence? How does this relate to the explore-exploit dilemma at the neural level?

{fill:textarea}

---

## Part 4: Learning and Synaptic Plasticity (Computational Analysis)

**4a.** Hebbian learning ("neurons that fire together wire together") and prediction error-driven learning appear to be different mechanisms. Using the Active Inference framework, explain how both can be understood as aspects of free energy minimization. Specifically, show how Hebbian plasticity relates to parameter learning (updating the generative model's A matrix) and how prediction error signals drive this process. Reference Module 06 (Learning).

{fill:textarea}

**4b.** Sleep plays a critical role in memory consolidation. Under Active Inference, offline replay during sleep can be understood as Bayesian model reduction -- pruning weak synaptic connections to reduce model complexity. Describe the neural mechanisms involved (hippocampal sharp-wave ripples, cortical slow oscillations) and explain how they implement free energy minimization without external sensory input.

{fill:textarea}

---

## Part 5: Neural Communication and Hierarchical Planning (Systems Integration)

**5a.** Mirror neurons in premotor cortex fire both when an agent performs an action and when they observe another agent performing the same action. Explain this phenomenon using the Active Inference concept of shared generative models. How does this neural mechanism support Theory of Mind and social inference? What predictions does Active Inference make about mirror neuron responses that differ from classical "simulation theory"? Reference Module 07 (Communication).

{fill:textarea}

**5b.** Prefrontal cortex is thought to implement hierarchical planning by maintaining multiple policy representations at different temporal scales. Using the Active Inference framework, describe how prefrontal working memory implements planning as inference. How do different prefrontal subregions (dorsolateral PFC, orbitofrontal cortex, anterior cingulate cortex) map onto different components of expected free energy computation? Reference Module 08 (Planning).

{fill:textarea}

---

## Part 6: Integration and Critical Analysis

**6a.** Write a 300-word synthesis explaining how the brain implements the complete Active Inference loop (perceive-infer-plan-act-learn) using the neural mechanisms covered across all eight modules. Your synthesis should identify specific brain regions and neurotransmitter systems for each component.

{fill:textarea}

**6b.** Identify one strength and one limitation of the computational neuroscience approach to Active Inference compared to the cognitive science approach (Course 1) and the mathematical approach (Course 3). What can neural implementation tell us that pure theory cannot? What gaps remain?

{fill:textarea}

---

## Submission Guidelines

- Respond to all parts in the text areas provided
- Total expected length: approximately 2000-3000 words across all parts
- Use proper neuroscience terminology and reference specific neural structures
- When discussing neural circuits, be precise about directionality (bottom-up vs. top-down) and neurotransmitter systems

## Recommended Readings

- Bogacz, R. (2017). A tutorial on the free-energy framework for modelling perception and learning. *Journal of Mathematical Psychology*, 76, 198-211.
- Bastos, A. M. et al. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695-711.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*, Chapters 4-6. MIT Press.
