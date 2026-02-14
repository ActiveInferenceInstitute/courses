# Station: Agents (Microstructural Evolution)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Nucleation, grain growth, precipitation, and characterization
- **Topics**: Agents — Nuclei as Autonomous Agents
- **Lab Style**: Image Analysis Lab
- **Audience**: Microscopists, characterization engineers, and microstructure scientists
- **Tone**: Technical / engineering-focused

## Active Inference Integration

A critical nucleus is an autonomous agent that emerges when local thermodynamic conditions warrant the formation of a new phase. Classical nucleation theory frames this as a Bayesian decision: the system evaluates the evidence (thermodynamic driving force from supercooling or supersaturation) against the cost (interfacial energy of creating the new boundary). Only when the nucleus exceeds the critical radius does the evidence outweigh the cost, and the agent becomes self-sustaining. Heterogeneous nucleation at grain boundaries, dislocations, or inclusions lowers the evidence threshold — these pre-existing features act as informative priors that reduce the barrier to agent formation. Zener pinning represents agent-agent interaction: precipitate agents impede grain boundary agent motion.

## Key Mappings

| FEP Concept | Nucleation Agent Translation |
|-------------|----------------------------|
| Agent | Critical nucleus; growing precipitate; mobile grain boundary segment |
| Agent Formation | Nucleation event (crossing the critical radius threshold) |
| Evidence Threshold | Classical nucleation barrier (Delta G*) |
| Informative Prior | Heterogeneous nucleation site (grain boundary, dislocation, inclusion) |
| Agent Interaction | Zener pinning (precipitates constraining grain boundary motion) |
| Agent Growth | Post-critical nucleus growth by atomic attachment from the parent phase |

## Content Guidelines

- Frame the critical radius as the decision boundary — subcritical clusters dissolve (insufficient evidence), supercritical nuclei grow (evidence exceeds threshold)
- Treat heterogeneous nucleation as prior-assisted inference: the pre-existing defect reduces the nucleation barrier, analogous to an informative prior reducing the evidence needed for model updating
- Connect competitive nucleation of multiple phases to Bayesian model comparison — the system selects the phase with the lowest free energy (highest model evidence)
- Emphasize Zener pinning as an agent interaction constraint that couples precipitate and grain boundary dynamics

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
