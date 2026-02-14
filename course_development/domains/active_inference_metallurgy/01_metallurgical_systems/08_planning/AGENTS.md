# Station: Planning (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Planning — Alloy Design as Strategic Planning
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

Alloy design is strategic planning under uncertainty. The metallurgist holds a generative model of composition-structure-property relationships and selects a compositional policy (alloy recipe) that is expected to minimize the gap between predicted properties and the design specification. Multi-objective optimization — balancing strength, ductility, corrosion resistance, and cost — maps directly to Expected Free Energy minimization, where both pragmatic value (achieving property targets) and epistemic value (reducing uncertainty about unexplored alloy space) guide the selection of the next alloy to synthesize and test.

## Key Mappings

| FEP Concept | Alloy Design Translation |
|-------------|-------------------------|
| Planning | Compositional design; property-performance mapping |
| Policy | Alloy composition (wt% of each element); processing parameters |
| Expected Free Energy | Combined objective function: property targets (pragmatic) + uncertainty reduction (epistemic) |
| Generative Model | Composition-structure-property linkage; Ashby property maps |
| Counterfactual Evaluation | Predicting properties of untested compositions using CALPHAD or ML surrogates |
| Planning Horizon | Single-element addition vs. full multi-component optimization |

## Content Guidelines

- Frame Ashby material selection charts as a visualization of the policy space — each alloy class occupies a region in property space
- Connect multi-objective optimization (Pareto front analysis) to Expected Free Energy that balances exploitation and exploration
- Treat high-throughput experimentation (combinatorial libraries) as parallel policy evaluation
- Emphasize the role of uncertainty quantification in guiding the next experiment — the alloy designer should test the composition that maximally reduces model uncertainty

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
