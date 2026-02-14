# Station: Communication (Mathematical Frameworks)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Probability, information theory, variational methods
- **Topics**: Multi-agent generative models, coupled inference, generalized synchrony, shared priors, mutual information between agents
- **Lab Style**: Problem Set
- **Audience**: College 1st semester undergraduates
- **Tone**: Rigorous but accessible

## Content Guidelines

This module formalizes multi-agent communication as coupled inference. Content should:

1. **Extend the POMDP to multiple agents**: Each agent has its own generative model, but the hidden states of one agent include the beliefs and actions of the other. This creates a coupled dynamical system.
2. **Define key terms precisely**:
   - **Multi-agent generative model**: A model where agent A's hidden states include agent B's beliefs and vice versa, creating recursive inference
   - **Generalized synchrony**: The mathematical condition where two coupled dynamical systems converge to a shared trajectory -- the formal definition of successful communication
   - **Shared prior**: A common component of multiple agents' generative models, enabling efficient prediction across agents (e.g., language, cultural norms)
   - **Mutual information I(X;Y)**: The amount of information shared between two variables; quantifies how much knowing one agent's state tells you about the other's
3. **Formalize Theory of Mind**: Agent A's generative model includes a sub-model of agent B's generative model, creating nested inference.
4. **Connect to information theory**: Successful communication maximizes mutual information between agents' internal states.

## Active Inference Integration

- Multi-agent Active Inference treats each agent's actions as observations for the other agent (Friston & Frith, 2015)
- Generalized synchrony is the mathematical condition for aligned generative models
- Shared priors (language, culture) reduce the complexity of multi-agent inference by providing common structure

## Assessment Alignment

Questions should test the ability to:
- Set up a two-agent generative model where each agent models the other
- Calculate mutual information between two agents' belief states
- Explain how shared priors reduce the computational cost of communication

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
