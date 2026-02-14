# Station: Cognition (Cognitive Science)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Mind, brain, behavior
- **Topics**: Variational free energy, attention as precision, accuracy-complexity trade-off, cognitive biases, the dark room problem
- **Lab Style**: Essay & Discussion
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module covers the internal optimization process of the generative model. Content should:

1. **Build on perception**: Students now understand that perception updates beliefs. Cognition broadens this to the overall organization and optimization of the generative model.
2. **Define key terms precisely**:
   - **Variational free energy (VFE)**: A single quantity measuring how well the agent's model fits reality -- high VFE means poor fit, low VFE means good fit
   - **Accuracy-complexity trade-off**: The brain prefers models that explain data well (accuracy) without unnecessary complexity (Occam's principle)
   - **Epistemic value**: The value of actions or beliefs that reduce uncertainty about hidden states
   - **Expected free energy (EFE)**: The quantity agents minimize when selecting future actions, combining pragmatic and epistemic value
3. **Use cognitive biases constructively**: Frame confirmation bias, anchoring, and overconfidence as natural consequences of precision settings, not as failures of rationality.
4. **Address the dark room problem**: Explain why minimizing surprise does not entail seeking boring environments.

## Active Inference Integration

- VFE decomposes into accuracy minus complexity, corresponding to the evidence lower bound (ELBO) in variational inference
- Attention is precision optimization over different information channels (Parr & Friston, 2019)
- Psychiatric symptoms (delusions, anxiety, depression) arise from aberrant precision weighting

## Assessment Alignment

Questions should test the ability to:
- Explain the accuracy-complexity trade-off using an everyday example
- Reframe a cognitive bias as a consequence of precision settings
- Articulate why the dark room problem does not invalidate Active Inference

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
