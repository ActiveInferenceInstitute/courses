# Station: Cognition (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Prefrontal cortex and belief updating, dopamine and precision, attention networks, default mode network, neural correlates of free energy
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module maps cognitive processes (belief updating, attention, curiosity) onto neural substrates. Content should:

1. **Identify the neural substrates of belief updating**: The prefrontal cortex maintains and updates beliefs; the anterior cingulate cortex monitors prediction errors; the insula integrates interoceptive predictions.
2. **Define key terms precisely**:
   - **Prefrontal cortex (PFC)**: The brain region that maintains abstract beliefs and evaluates competing hypotheses
   - **Dopaminergic system**: The neurotransmitter system that signals precision of prior beliefs and expected reward
   - **Default mode network (DMN)**: A network active during rest, self-referential thought, and mental simulation -- linked to the generative model running in "offline" mode
   - **Salience network**: The network (insula, ACC) that detects surprising events and redirects attention
3. **Connect neurotransmitters to precision**: Dopamine = prior precision, acetylcholine = sensory precision, noradrenaline = global arousal/uncertainty.
4. **Link psychiatric conditions to neural disruption**: Schizophrenia (aberrant dopamine/precision), ADHD (impaired noradrenergic precision), depression (reduced dopaminergic drive).

## Active Inference Integration

- Free energy minimization is implemented through recurrent neural dynamics in prefrontal-parietal networks
- The DMN implements the generative model's "default" predictions about self and world
- Aberrant precision weighting provides a computational neuroscience account of psychosis (Adams et al., 2013)

## Assessment Alignment

Questions should test the ability to:
- Map the accuracy-complexity trade-off onto specific brain networks
- Explain how dopamine disruption leads to delusional beliefs via aberrant precision
- Describe the DMN's role in maintaining the generative model

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
