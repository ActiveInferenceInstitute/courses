# Lab: Renormalization Group and Scale-Free Active Inference

> **Learning Goal:** Apply RG concepts to Active Inference at multiple scales, analyzing coarse-graining, criticality, and multi-scale organization.

## Part 1: Multi-Scale Markov Blanket Identification

**Exercise**: For the human body, identify the Markov blanket at each organizational scale:

| Scale | System | External States | Sensory States | Active States | Internal States |
|-------|--------|----------------|---------------|--------------|----------------|
| Molecular | Single protein | Solvent molecules, ligands | Binding sites, allosteric sites | Conformational changes, enzymatic activity | Intramolecular dynamics |
| Cellular | Neuron | Extracellular environment | Receptors, ion channels, synaptic inputs | Axon terminals, neurotransmitter release | Intracellular signaling, gene expression |
| Circuit | Cortical column | Other columns, subcortical input | Input layer neurons (L4) | Output layer neurons (L5/6) | Internal processing layers (L2/3) |
| Organ | Brain | Body, environment | Sensory nerves | Motor nerves, endocrine | Cortical and subcortical processing |
| Organism | Person | Physical/social environment | Sense organs (eyes, ears) | Muscles, voice, hands | Brain, viscera |
| Social | Family | Other families, institutions | Communication received | Communication sent, actions | Shared beliefs, family dynamics |

Write a 200-word analysis: At which scale does the Markov blanket identification become most controversial? Why?

{fill:textarea}

## Part 2: Coarse-Graining Exercise

> **Learning Goal:** Perform a conceptual RG transformation on a neural system.

**Exercise**: Consider a network of 100 spiking neurons. Perform two levels of coarse-graining:

**Level 0 (Microscopic)**: 100 individual neurons with spiking dynamics

- States: individual membrane potentials V₁, V₂, ..., V₁₀₀
- Interactions: synaptic weights w_{ij}

**Level 1 (Mesoscopic)**: Group into 10 neural populations of 10 neurons each

- States: mean firing rates r₁, r₂, ..., r₁₀
- Effective interactions: population coupling J_{IJ} = some function of {w_{ij}}

**Level 2 (Macroscopic)**: Group into 2 brain regions of 5 populations each

- States: regional activity levels R₁, R₂
- Effective interaction: inter-regional coupling

At each level: (a) What information is lost? (b) What information is preserved? (c) Does the generative model structure (A, B matrices) change form?

{fill:textarea}

## Part 3: Criticality Analysis

> **Learning Goal:** Evaluate the evidence for neural criticality.

**Exercise**: Evaluate the following evidence for brain criticality:

| Evidence | Finding | Supports Criticality? | Alternative Explanation |
|----------|---------|---------------------|----------------------|
| Neural avalanches | Power-law size distribution with exponent ~3/2 | Yes — matches critical Ising model | Could be subcritical with weak correlations |
| 1/f noise | Power spectrum ~1/f across broad frequency range | Yes — scale invariance | Could result from multiple uncorrelated processes |
| Long-range correlations | fMRI shows correlations across distant brain regions | Yes — divergent correlation length | Could reflect anatomical connectivity |
| Maximal dynamic range | Neural systems at criticality respond to widest range of input intensities | Yes — optimal sensitivity | Could be selected for without criticality |
| Information capacity | Criticality maximizes mutual information between input and output | Yes — optimal coding | Other mechanisms achieve good coding |

Write a 300-word assessment: Is the brain at criticality, near criticality, or is this a misleading framework?

{fill:textarea}

## Part 4: Society as Active Inference

> **Learning Goal:** Apply scale-free Active Inference to social systems.

**Exercise**: Model a political election as Active Inference at the social scale:

1. **Social generative model**: What is the "shared model" of a political party? (Beliefs about the economy, society, threats, opportunities)
2. **Social prediction errors**: What events generate prediction errors in the social model? (Unexpected economic data, scandals, crises)
3. **Social active inference**: How does the party act to minimize free energy? (Policy proposals = active states; media = sensory management)
4. **Social learning**: How does the party's model update after an election loss?
5. **Echo chambers as precision traps**: How do echo chambers function as excessive precision on prior beliefs, preventing model updating?

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: The scale-free claim of Active Inference — that the same principles apply from molecules to societies — is either the framework's greatest strength or its greatest weakness. If it applies to everything, does it predict anything? Compare this to other "universal" frameworks (thermodynamics, natural selection, information theory). Are they similarly general, and are they similarly useful?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Multi-scale identification | Nested Markov blankets |
| 2 | RG transformation | Coarse-graining neural systems |
| 3 | Evidence evaluation | Neural criticality |
| 4 | Social application | Scale-free framework |
| 5 | Philosophical critique | Universality vs. predictive power |
