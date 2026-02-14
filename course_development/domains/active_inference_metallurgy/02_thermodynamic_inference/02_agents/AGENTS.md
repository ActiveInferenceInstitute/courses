# Station: Agents (Thermodynamic Inference)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Phase equilibria, transformation kinetics, and CALPHAD
- **Topics**: Agents — Chemical Species as Inference Agents
- **Lab Style**: Calculation Lab
- **Audience**: Thermodynamics specialists and computational materials scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Chemical species are inference agents that seek equilibrium partitioning to minimize the system's total Gibbs energy. Each diffusing element (C, Cr, Ni, Mo, etc.) can be treated as an agent with its own chemical potential landscape. The agent's preferred state is the equilibrium partition coefficient — the composition ratio between coexisting phases where chemical potentials are equal. When the system is out of equilibrium, each species experiences a chemical potential gradient (prediction error) and responds by diffusing (acting) to reduce that gradient. Activity coefficients encode the non-ideal interactions between agents, modifying their individual inference dynamics.

## Key Mappings

| FEP Concept | Chemical Species Translation |
|-------------|----------------------------|
| Agent | Individual chemical element (Fe, C, Cr, Ni, etc.) in a multicomponent system |
| Preferred State | Equilibrium partition coefficient between phases |
| Prediction Error | Chemical potential difference for species i between phases alpha and beta |
| Action | Diffusive flux of species i driven by chemical potential gradient |
| Agent Interaction | Activity coefficients; interaction parameters in solution models |
| Multi-Agent Equilibrium | Simultaneous equality of chemical potentials for all species across all phases |

## Content Guidelines

- Treat each chemical element as an independent agent performing gradient descent on its own chemical potential landscape, coupled to other agents through interaction parameters
- Frame activity as a belief-weighted concentration — it reflects the effective concentration accounting for non-ideal interactions
- Connect the Gibbs-Duhem equation to the constraint that agent actions must be mutually consistent
- Emphasize that partition coefficients are the posterior beliefs about where each species should reside at equilibrium

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
