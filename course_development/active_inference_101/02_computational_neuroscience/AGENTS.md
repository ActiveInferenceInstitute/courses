# Course AGENTS: Computational Neuroscience

> **Quick Navigation**: [Course README](./README.md) | [Curriculum AGENTS](../AGENTS.md)

## Identity

- **Course**: Computational Neuroscience
- **Number**: 2
- **Perspective**: Neural circuits & Bayesian brain
- **Lab Type**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible. Full mathematical notation. Python/NumPy. Textbook-quality.

## Content Guidelines

This course presents Active Inference from the perspective of computational neuroscience, grounding abstract concepts in neural circuits, brain regions, and neurotransmitter systems. All content should:

1. **Connect concepts to neural substrates**: Every Active Inference concept should be linked to specific brain structures, neural circuits, or neurotransmitter systems. For example, precision weighting maps to neuromodulators (dopamine, acetylcholine, noradrenaline).
2. **Use the Bayesian brain framework**: Frame the brain as performing approximate Bayesian inference, with neural populations encoding probability distributions and synaptic connections implementing likelihood mappings.
3. **Define neuroscience jargon on first use**:
   - **Predictive coding**: A neural implementation of Active Inference where cortical hierarchies pass predictions downward and prediction errors upward
   - **Attractor dynamics**: Stable patterns of neural activity that represent beliefs or percepts
   - **Synaptic plasticity**: The mechanism by which learning updates the generative model at the neural level
   - **Neuromodulation**: The process by which neurotransmitters adjust precision weighting across neural circuits
4. **Include neural circuit diagrams**: Where possible, describe the flow of information through cortical layers, basal ganglia, cerebellum, and prefrontal cortex.
5. **Reference neuroimaging and electrophysiology evidence**: Cite fMRI, EEG, and single-unit recording studies that support Active Inference predictions.

## Lab Design Principles

Labs in this course are **simulation lab** format:

- Provide simple computational simulations of neural processes (e.g., attractor networks, predictive coding circuits)
- Use Python/NumPy for all simulations, keeping code accessible to introductory students
- Include visualization of neural dynamics (firing rates, oscillations, attractor landscapes)
- Use `{fill:textarea}` for analysis and interpretation of simulation results

## Question Standards

- Questions should test the ability to map Active Inference concepts onto neural mechanisms
- Include questions that ask students to predict what would happen if a specific neural component were disrupted
- Connect clinical neuroscience (lesion studies, pharmacological manipulations) to Active Inference predictions

## References

- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference*. MIT Press.
- Breakspear, M. (2017). Dynamic models of large-scale brain activity. *Nature Neuroscience*, 20(3), 340-352.
