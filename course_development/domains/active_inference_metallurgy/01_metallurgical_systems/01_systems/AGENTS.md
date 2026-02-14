# Station: Systems (Metallurgical Systems)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Crystal structures, defects, and fundamental thermodynamics
- **Topics**: Systems — Crystal Lattices as Markov Blankets
- **Lab Style**: Simulation Lab
- **Audience**: Materials science graduate students and metallurgical engineers
- **Tone**: Technical / engineering-focused

## Active Inference Integration

The crystal lattice is the foundational system boundary in metallurgy. A unit cell defines a Markov blanket at the atomic scale: internal states (atomic positions, electronic structure), external states (surrounding lattice, applied fields), sensory states (interatomic forces at the cell boundary), and active states (lattice relaxation, thermal vibration). The Bravais lattice types (FCC, BCC, HCP, etc.) represent distinct generative models — each encoding different expectations about nearest-neighbor coordination, packing efficiency, and slip system availability.

## Key Mappings

| FEP Concept | Crystal Lattice Translation |
|-------------|---------------------------|
| Markov Blanket | Unit cell boundary; crystal surface; grain boundary |
| Internal States | Atomic positions within the unit cell; electron density distribution |
| External States | Applied stress field; thermal field; chemical environment |
| Generative Model | Bravais lattice type (FCC, BCC, HCP) as structural expectation |
| Model Evidence | Lattice stability confirmed by diffraction pattern matching predicted reflections |

## Content Guidelines

- Emphasize that crystal symmetry operations define the system's invariances — what the lattice "expects" to remain unchanged
- Connect Wigner-Seitz cells to the concept of the minimal sufficient boundary (Markov blanket)
- Treat lattice parameter as a precision-weighted belief about interatomic spacing
- Polymorphic transitions (e.g., BCC iron to FCC austenite) exemplify model switching under environmental change

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
