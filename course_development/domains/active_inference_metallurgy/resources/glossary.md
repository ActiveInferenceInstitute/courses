# Glossary: Active Inference for Metallurgy

> Definitions of key terms used throughout the curriculum.
> Designed for materials scientists, metallurgical engineers, and process engineers.
> Each entry maps the formal Active Inference / FEP concept to its metallurgical translation.

---

### Active Inference

The theory that all adaptive systems — including material systems — act to confirm their predictions about the world while simultaneously updating those predictions when surprised. In metallurgical terms: a cooling alloy "acts" by transforming to phases that minimize thermodynamic free energy, while the system's trajectory is constrained by kinetics and boundary conditions — a physical enactment of inference.

### Allostasis

The process of achieving stability through structural transformation. Unlike homeostasis (returning to a fixed state), allostasis means the material system settles into a new equilibrium configuration. Example: a quenched steel that tempers at elevated temperature is not returning to its prior austenitic state but finding a new metastable configuration of tempered martensite.

### CALPHAD (Calculation of Phase Diagrams)

A computational framework that constructs thermodynamic models of multicomponent systems from assessed experimental data. Under Active Inference, CALPHAD databases serve as generative models — they predict what phases will be present at any given temperature, pressure, and composition, enabling the metallurgist to minimize surprise about equilibrium behavior.

### Characterization

The metallurgical analogue of sensory inference — gathering, filtering, and interpreting signals about material structure and properties. Techniques such as X-ray diffraction (XRD), electron backscatter diffraction (EBSD), and optical microscopy provide observations that the engineer uses to infer hidden states (crystal structure, phase fractions, texture).

### Crystal Structure as Markov Blanket

The idea that a crystal lattice defines a statistical boundary between internal states (atomic positions, bonding, electronic structure) and external states (temperature field, stress field, chemical environment). The lattice surface mediates all interactions between the crystal interior and its surroundings.

### Diffusion as Communication

Mass transport by diffusion is the fundamental communication mechanism in metallurgical systems. Atoms migrate down chemical potential gradients, transmitting composition information across grain boundaries and phase interfaces — analogous to message passing in Active Inference.

### Digital Twin

A computational replica of a physical manufacturing process that continuously updates its internal model using real-time sensor data. Under Active Inference, a digital twin is a generative model that minimizes prediction error between simulated and measured process states, enabling closed-loop control.

### Epistemic Value (Information Value)

The expected reduction in uncertainty that a characterization experiment or process measurement will produce. When an engineer requests an EBSD scan rather than relying on optical microscopy alone, the primary value is the higher-precision orientation data — reducing uncertainty about texture and misorientation distributions.

### Expected Free Energy (EFE)

The quantity that guides policy selection in Active Inference. It combines **pragmatic value** (will this processing route achieve target properties?) and **epistemic value** (will this experiment reduce our uncertainty about the material?). For metallurgists, EFE provides a principled framework for balancing exploitation of known alloy systems with exploration of novel compositions.

### Free Energy (Gibbs / Helmholtz / Variational)

In thermodynamics, the Gibbs free energy G = H − TS governs phase stability at constant pressure and temperature. In Active Inference, variational free energy is a tractable upper bound on surprise. The deep analogy: both quantities measure the "cost" of being out of equilibrium. Metallurgical processes and inference processes both proceed by minimizing their respective free energies.

### Generative Model (Thermodynamic Model)

The system's implicit or explicit model of how its environment works. In metallurgy, this is the thermodynamic database or phase diagram that predicts what phases will be stable under given conditions. A flawed generative model — an inaccurate phase diagram — leads to persistent process failures and unexpected microstructures.

### Grain Boundary

The interface between two crystals of different orientation. In Active Inference terms, a grain boundary is a Markov blanket at the mesoscale — it mediates diffusion (communication), segregation (selective filtering), and mechanical load transfer between adjacent grains. Grain boundary character distributions are critical to material properties.

### Homeostasis

The process of maintaining critical variables within viable bounds. For a metallurgical process, this includes maintaining melt temperature, cooling rate, and atmosphere composition within target ranges. Active Inference extends this by showing how feedback control systems actively work to keep process parameters in preferred states.

### Internal States

The hidden variables that characterize a material system's identity — crystal structure, defect density, precipitate distribution, residual stress state, chemical composition gradients. These are the states "inside the Markov blanket" that evolve through phase transformations, diffusion, and deformation.

### Markov Blanket (System Boundary)

The statistical boundary that separates a system's internal states from its external environment. In metallurgy: the surface of a grain, the interface between two phases, or the boundary of a heat-affected zone. The blanket consists of **sensory states** (what the system receives: heat flux, chemical potential) and **active states** (what the system emits: latent heat, diffusing species).

### Metastability

A state that is locally stable but not at global equilibrium. Martensite in quenched steel is metastable — it has lower free energy than the supersaturated austenite it formed from, but higher free energy than the equilibrium ferrite + cementite. Metastability is the metallurgical analogue of a local minimum in the free energy landscape.

### Nested Systems

Hierarchically organized systems at multiple scales. In metallurgy: atoms within unit cells, unit cells within grains, grains within phases, phases within components, components within assemblies. Each level has its own Markov blanket, and what constitutes a "sensory state" at one level becomes an "active state" at another.

### Nucleation

The process by which a new phase forms within a parent phase. Under Active Inference, nucleation is the emergence of a new agent — a critical nucleus that has crossed the free energy barrier and can now grow autonomously. The critical nucleus radius represents the boundary between dissolution (model rejection) and growth (model confirmation).

### Phase Diagram as Generative Model

The central conceptual bridge of this curriculum. A phase diagram encodes predictions about what phases will be stable at given temperature and composition. When a real alloy deviates from these predictions (e.g., due to rapid cooling), the deviation is prediction error — the driving force for subsequent transformations.

### Phase Transformation

A change in crystal structure, composition, or ordering. Under Active Inference, phase transformations are the material system's "actions" — structural changes that minimize thermodynamic free energy. Diffusion-controlled transformations are slow, deliberate actions; martensitic transformations are rapid, reflex-like responses.

### Precision (Measurement Resolution)

The inverse variance (reliability) of a measurement or model prediction. In metallurgy, precision determines which characterization data gets weighted heavily in decision-making. A transmission electron microscope provides atomic-resolution images (high precision); a handheld hardness tester provides rapid but approximate readings (low precision).

### Prediction Error (Process Deviation)

The difference between what the thermodynamic model or process model predicted and what actually occurred — e.g., unexpected phase fractions, off-target hardness, or unanticipated weld defects. All metallurgical process improvement is driven by the imperative to minimize prediction error.

### Processing Route (Policy)

A sequence of operations — melting, casting, hot rolling, heat treatment, finishing — designed to achieve target material properties. Under Active Inference, a processing route is a policy: a sequence of actions selected to minimize expected free energy over the manufacturing timeline.

### TTT / CCT Diagrams

Time-Temperature-Transformation (TTT) and Continuous Cooling Transformation (CCT) diagrams map the kinetics of phase transformations. Under Active Inference, these diagrams are temporal generative models — they predict what microstructure will form as a function of the thermal history (policy) applied to the alloy.

---

## Navigation

- [Notation Table](./notation_table.md)
- [References](./references.md)
- [Home](../README.md)
