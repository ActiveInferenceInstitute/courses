# Station: Planning (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Hippocampal replay, prefrontal prospection, place cells and grid cells, basal ganglia and habit formation, neural correlates of imagination
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module maps planning, imagination, and habit formation onto neural circuits. Content should:

1. **Present hippocampal replay as neural planning**: During rest and sleep, the hippocampus replays sequences of place cell activity, simulating possible future trajectories -- this is planning as inference at the neural level.
2. **Define key terms precisely**:
   - **Place cells**: Hippocampal neurons that fire when the animal is in a specific location, forming a spatial generative model
   - **Grid cells**: Entorhinal cortex neurons that fire in a regular hexagonal pattern, providing a coordinate system for spatial planning
   - **Hippocampal replay**: The reactivation of sequential place cell patterns during rest, simulating future paths through the environment
   - **Prefrontal prospection**: The prefrontal cortex's ability to simulate future scenarios by running the generative model forward in time
3. **Distinguish neural substrates of habits vs. planning**: Dorsomedial striatum supports goal-directed planning (EFE evaluation); dorsolateral striatum supports habitual policies (strong priors without deliberation).
4. **Connect imagination to perception**: The same neural populations active during perception are reactivated during imagination, supporting the Active Inference claim that imagination is offline inference.

## Active Inference Integration

- Hippocampal replay implements evaluation of future policies by simulating expected outcomes (Pezzulo et al., 2014)
- The prefrontal cortex maintains deep temporal models with nested timescale predictions
- The shift from goal-directed to habitual control reflects increasing policy prior precision through repeated experience

## Assessment Alignment

Questions should test the ability to:
- Explain hippocampal replay as neural implementation of planning as inference
- Compare the neural circuits for habitual vs. goal-directed action selection
- Describe how imagination reuses perceptual neural machinery for offline simulation

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
