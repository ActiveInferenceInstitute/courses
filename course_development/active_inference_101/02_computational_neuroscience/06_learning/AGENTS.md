# Station: Learning (Computational Neuroscience)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Neural circuits & Bayesian brain
- **Topics**: Synaptic plasticity, Hebbian learning, long-term potentiation, hippocampus, sleep and consolidation, Bayesian model reduction in the brain
- **Lab Style**: Simulation Lab
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module maps learning onto neural plasticity mechanisms. Content should:

1. **Connect parameter learning to synaptic plasticity**: Updating the A, B, and D matrices of the generative model corresponds to changing synaptic weights through long-term potentiation (LTP) and long-term depression (LTD).
2. **Define key terms precisely**:
   - **Synaptic plasticity**: The ability of synapses to strengthen or weaken over time, the neural substrate of learning
   - **Hebbian learning**: "Neurons that fire together wire together" -- the basic rule for strengthening co-active connections
   - **Long-term potentiation (LTP)**: A persistent strengthening of synapses, the cellular mechanism of memory formation
   - **Hippocampus**: The brain structure critical for episodic memory formation and spatial learning, acting as a fast-learning buffer
3. **Explain the hippocampal-cortical complementary learning system**: The hippocampus rapidly encodes new experiences; during sleep, these are consolidated into cortical generative models.
4. **Connect structure learning to sleep**: Bayesian model reduction during sleep corresponds to synaptic downscaling and pruning of unnecessary connections.

## Active Inference Integration

- Parameter learning corresponds to synaptic plasticity updating the weights that define the generative model
- Structure learning (BMR) corresponds to synaptic pruning during sleep (Friston et al., 2017)
- The hippocampus acts as a fast inference engine; the cortex stores the long-term generative model

## Assessment Alignment

Questions should test the ability to:
- Explain how LTP implements parameter learning in the generative model
- Describe the complementary roles of hippocampus (fast learning) and cortex (slow consolidation)
- Predict what happens to learning when sleep is disrupted, using Active Inference concepts

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
