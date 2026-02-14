# Station: Agents (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Neural architecture of agents, cortical hierarchy, generative model in the brain, top-down vs. bottom-up processing
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module maps the agent concept onto neural architecture. Content should:

1. **Show how the brain implements a generative model**: The cortical hierarchy, with its six-layer structure and reciprocal connections, is the physical substrate of the generative model. Higher layers encode abstract priors; lower layers encode sensory likelihoods.
2. **Define key terms precisely**:
   - **Cortical hierarchy**: The layered organization of the cortex where each level predicts the activity of the level below
   - **Top-down processing**: Predictions flowing from higher to lower cortical areas
   - **Bottom-up processing**: Prediction errors flowing from lower to higher cortical areas
   - **Generative model (neural)**: The set of synaptic connections that encode the brain's model of how hidden states cause sensory data
3. **Introduce the canonical microcircuit**: The cortical column as the basic computational unit of Active Inference, with superficial pyramidal cells carrying prediction errors and deep pyramidal cells carrying predictions.
4. **Connect to the agent spectrum**: Show how different brain complexities (insect mushroom body, mammalian cortex, human prefrontal cortex) implement increasingly sophisticated generative models.

## Active Inference Integration

- The cortical hierarchy implements hierarchical generative models (Friston, 2005; Bastos et al., 2012)
- Prediction errors are carried by superficial pyramidal cells; predictions by deep pyramidal cells
- The self-model maps to interoceptive cortex (insula) and proprioceptive systems

## Assessment Alignment

Questions should test the ability to:
- Map the generative model components (likelihood, prior, posterior) onto cortical layers
- Explain the direction of information flow for predictions vs. prediction errors
- Describe how the self-model is implemented in interoceptive brain regions

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
