# Section 1: Metallurgical Systems -- Section Overview

## Learning Objectives

1. Describe crystal lattices, unit cells, and grain boundaries as Markov blankets that define system boundaries at the atomic, mesoscopic, and engineering scales.
2. Model atoms, point defects, and dislocations as agents that maintain and update their states within the lattice according to interatomic potentials.
3. Interpret X-ray diffraction patterns and spectroscopic data as sensory observations that constrain inference about internal crystallographic states.
4. Apply lattice energy calculations and first-principles methods (DFT) as computational cognition -- the material system's internal modeling of its own equilibrium.
5. Connect Gibbs free energy minimization in thermodynamics to variational free energy minimization in Active Inference, establishing the mathematical bridge that unifies the curriculum.

## Introduction

Metallurgy begins at the atomic scale. Before we can understand phase transformations, microstructural evolution, or process optimization, we must understand the most fundamental metallurgical system: the crystal lattice. This section establishes the foundational parallel between physical metallurgy and Active Inference by examining crystal structures, defects, and fundamental thermodynamics through the lens of the Free Energy Principle.

The core insight is neither metaphorical nor superficial: thermodynamic free energy minimization and variational free energy minimization share the same mathematical structure. A crystal lattice minimizing its Gibbs free energy is formally analogous to an Active Inference agent minimizing its variational free energy. The lattice boundary (grain boundary, surface, or unit cell face) functions as a Markov blanket. Defects -- vacancies, interstitials, dislocations -- are prediction errors relative to the ideal crystal model. Diffusion is the mechanism by which these prediction errors are resolved. And characterization techniques (XRD, SEM-EDS, XPS) are the sensory modalities through which the metallurgist perceives the material's internal states.

Across eight modules, this section develops these parallels with full technical rigor. Module 01 (Systems) establishes the crystal lattice as a bounded system with Markov blankets at every scale -- from the unit cell to the grain to the component. Module 02 (Agents) models atoms and defects as agents whose behavior is governed by interatomic potentials and thermodynamic driving forces. Module 03 (Perception) covers the characterization techniques that serve as sensory modalities: X-ray diffraction reveals lattice parameters and phase identity, spectroscopy reveals chemical composition, and electron microscopy reveals microstructural morphology. Module 04 (Cognition) introduces computational methods -- DFT calculations and interatomic potential models -- as the material's (and the metallurgist's) internal modeling of lattice energy and stability.

Module 05 (Action) covers deformation and alloying as active states -- the mechanisms by which the material changes its environment or the metallurgist changes the material. Module 06 (Learning) traces the historical development of alloy systems, from empirical trial-and-error to CALPHAD databases, as a story of cumulative model building. Module 07 (Communication) examines diffusion as atomic-scale communication -- the mechanism by which concentration gradients (prediction errors) are resolved through mass transport. Module 08 (Planning) covers alloy design as strategic planning -- selecting compositions and processing routes to achieve target properties under uncertainty.

## Key Concepts

### 1. The Crystal Lattice as Markov Blanket (Module 01: Systems)

A crystal lattice is the archetypal metallurgical system. The unit cell defines the smallest repeating boundary -- a Markov blanket at the atomic scale. Internal states are the atomic positions and electronic configurations within the cell. External states are the neighboring cells and the broader material environment. Sensory states include the interatomic forces transmitted across cell boundaries. Active states include the displacements of boundary atoms in response to stress or thermal activation. At larger scales, grain boundaries serve as Markov blankets between grains with different crystallographic orientations, and the component surface serves as the boundary between the material and its service environment.

### 2. Defects as Prediction Errors (Module 02: Agents and Module 05: Action)

The ideal crystal model predicts that every atomic site is occupied by the correct atom in the correct position. Defects -- vacancies, interstitials, substitutional atoms, dislocations, stacking faults -- are deviations from this prediction. In Active Inference terms, each defect represents a prediction error: the actual atomic configuration differs from the model's expectation. The material system acts to minimize these prediction errors through diffusion (vacancies migrating to sinks), recovery (dislocations rearranging into lower-energy configurations), and recrystallization (the formation of new, defect-free grains). The equilibrium defect concentration reflects the accuracy-complexity trade-off: some defects are thermodynamically favorable (they increase entropy, reducing free energy despite increasing internal energy).

### 3. Characterization as Perception (Module 03: Perception)

The metallurgist perceives the material's internal states through characterization techniques, each with its own precision and resolution. X-ray diffraction senses the average lattice parameter and phase identity -- high precision for crystal structure, but blind to local defects. Electron backscatter diffraction (EBSD) senses grain orientations and boundary character -- revealing mesoscale structure invisible to bulk XRD. Transmission electron microscopy (TEM) senses individual dislocations and precipitates at nanometer resolution but samples a tiny volume. Each technique has a characteristic Markov blanket: it senses specific states while remaining conditionally independent of others. The skilled metallurgist practices active perception -- choosing techniques and measurement parameters to maximize information gain about the specific uncertainty they are trying to resolve.

### 4. Computational Cognition and the FEP Bridge (Modules 04-05: Cognition and Action)

Density functional theory (DFT) calculates the electronic structure and total energy of atomic configurations from first principles. In Active Inference terms, DFT is cognition -- it computes the internal model of lattice energy that predicts which configurations are stable and which are not. The metallurgist uses DFT predictions to guide alloy design: if the calculation predicts that a particular solute will strengthen the lattice, the metallurgist acts by preparing that alloy. The gap between DFT prediction and experimental observation is the prediction error that drives further model refinement. The deepest insight of this section is that the material itself performs the same computation: a crystal lattice settling into its equilibrium configuration is minimizing Gibbs free energy, formally equivalent to minimizing variational free energy.

### 5. Diffusion as Communication and Alloy Design as Planning (Modules 07-08: Communication and Planning)

Diffusion is how atoms communicate. A concentration gradient is a spatial prediction error -- the local composition differs from equilibrium. Fick's laws describe how this prediction error is resolved through atomic migration, with the diffusion coefficient setting the rate. At a higher level, the metallurgist's alloy design process is planning under uncertainty: selecting compositions, temperatures, and times to achieve target microstructures and properties, using phase diagrams and TTT/CCT diagrams as policy maps. The expected free energy framework applies directly: each processing route has a predicted outcome (pragmatic value) and an associated uncertainty (epistemic cost).

## Applications

### Application 1: Steel Heat Treatment -- From Austenite to Martensite

Consider a plain carbon steel (Fe-0.4wt%C) heated to 900 degrees Celsius (austenitizing) and then rapidly quenched. At the system level, the austenite phase is a high-temperature Markov blanket -- an FCC lattice with carbon dissolved in octahedral interstitial sites. Upon quenching, the system experiences a massive prediction error: the rapidly falling temperature drives the system far from its equilibrium model. The austenite lattice cannot transform to equilibrium ferrite plus cementite (the diffusion-dependent prediction error resolution) because cooling is too fast for carbon diffusion. Instead, the lattice undergoes a diffusionless (martensitic) transformation -- a shear-based structural change that traps carbon in a supersaturated BCT lattice. Martensite is, in effect, a frozen prediction error: the system attempted to minimize free energy but was kinetically arrested before reaching equilibrium.

### Application 2: Aluminum Precipitation Hardening -- Sequential Model Updating

In Al-Cu alloys (such as 2024-T4), the precipitation sequence GP zones to theta-double-prime to theta-prime to theta (Al2Cu) represents sequential model updating at the atomic scale. Each metastable phase represents the material's best current inference about its equilibrium state given the available thermal energy and diffusion time. GP zones are the first approximation -- clusters of copper atoms on specific crystallographic planes. As aging continues (more thermal energy, more diffusion), the model updates: theta-double-prime provides a better fit to the Gibbs energy surface, and eventually theta-prime and equilibrium theta emerge. The peak hardness condition (T6 temper) corresponds to the optimal balance between precipitate coherency (maintaining lattice strain that resists dislocation motion) and precipitate size -- an accuracy-complexity trade-off in the material's own free energy landscape.

## Conclusion

Metallurgical Systems establishes the foundational parallel between physical metallurgy and Active Inference. By understanding crystal lattices as Markov blankets, defects as prediction errors, characterization as perception, DFT as cognition, deformation as action, alloy development as learning, diffusion as communication, and alloy design as planning, students gain a unified framework that connects atomic-scale phenomena to the Free Energy Principle. The next section -- Thermodynamic Inference -- exploits this bridge fully, treating phase diagrams as generative models and CALPHAD calculations as variational inference.
