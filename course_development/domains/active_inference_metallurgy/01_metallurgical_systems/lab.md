# Lab: Crystal Systems Analysis Through the Active Inference Lens

## Objective

Apply Active Inference concepts to analyze the crystallographic and thermodynamic behavior of a real metallurgical system. You will map Markov blankets at multiple scales, interpret characterization data as sensory observations, and perform free energy calculations that bridge thermodynamic and variational frameworks.

## Prerequisites

- Undergraduate-level knowledge of crystal structures (FCC, BCC, HCP)
- Basic understanding of defects in crystalline materials (vacancies, dislocations)
- Familiarity with X-ray diffraction principles
- Python with NumPy for computational exercises (optional: access to a crystallographic visualization tool such as VESTA)

## Materials

- Periodic table and crystal structure reference data (lattice parameters for Fe, Al, Cu)
- XRD pattern data set (provided or simulated): a steel sample with mixed BCC and FCC phases
- Python environment with NumPy and Matplotlib installed
- Calculator for thermodynamic calculations

## Procedure

### Part 1: Markov Blanket Mapping at Multiple Scales (20 minutes)

For a plain carbon steel (Fe-0.4wt%C) at room temperature, draw a nested Markov blanket diagram at three scales.

1. **Atomic scale**: Draw the BCC unit cell of ferrite. Label the internal states (atomic positions, electron density), the Markov blanket (unit cell faces), and the external states (neighboring cells). Identify one sensory state (interatomic force across the boundary) and one active state (atomic displacement under thermal vibration).

2. **Grain scale**: Sketch a polycrystalline microstructure with 5-8 grains. Label the grain boundaries as Markov blankets. For one grain boundary, identify what information crosses the boundary (stress transmission, diffusive flux) and what is conditionally independent (internal dislocation structure of non-adjacent grains).

3. **Component scale**: Sketch a cross-section of a steel beam in service. Label the component surface as the outermost Markov blanket. Identify the sensory states (surface exposure to environment, load application points) and the active states (deformation response, corrosion product formation).

### Part 2: Defect Analysis as Prediction Error (15 minutes)

Calculate the equilibrium vacancy concentration in iron at two temperatures and interpret the result using Active Inference.

1. **Calculate**: Using the vacancy formation energy for BCC iron (E_v = 1.6 eV) and the Boltzmann relation (c_v = exp(-E_v / k_B T)), compute the equilibrium vacancy fraction at:
   - T = 300 K (room temperature)
   - T = 1200 K (near the austenite region)

2. **Interpret**: The ideal crystal model predicts zero vacancies. The actual equilibrium state has a nonzero vacancy concentration. Explain this as a free energy minimization outcome: how does the entropy of mixing (the "complexity" term) compete with the vacancy formation energy (the "accuracy" term)?

3. **Predict**: If the steel is quenched rapidly from 1200 K to 300 K, what happens to the vacancy concentration? Is the quenched state at equilibrium? Describe this in Active Inference terms as a frozen prediction error.

### Part 3: XRD Data Interpretation as Perception (15 minutes)

Analyze an XRD pattern from a dual-phase steel sample.

1. **Identify phases**: Given peak positions corresponding to BCC ferrite (primary peaks at 2-theta values corresponding to {110}, {200}, {211}) and FCC austenite (peaks at {111}, {200}, {220}), identify which peaks belong to which phase.

2. **Estimate phase fractions**: Using relative peak intensities, estimate the approximate volume fraction of each phase. This is the metallurgist's perception of the material's internal phase distribution.

3. **Assess precision**: What are the sources of uncertainty in your phase fraction estimate? Consider peak overlap, preferred orientation, background subtraction, and counting statistics. In Active Inference terms, what is the precision of this perceptual modality?

4. **Active sensing proposal**: If you needed to reduce uncertainty about the austenite distribution (whether it is uniformly distributed or concentrated at grain boundaries), which additional characterization technique would you choose, and why? Justify this as an active sensing decision.

### Part 4: Free Energy Bridge Calculation (10 minutes)

Demonstrate the mathematical parallel between thermodynamic and variational free energy.

1. **Gibbs free energy**: For the ferrite-to-austenite transformation in pure iron at 1185 K (the equilibrium transformation temperature), the Gibbs energy change is approximately zero (G_alpha = G_gamma). At 1300 K, the austenite phase has lower Gibbs energy. Calculate or sketch the Gibbs energy difference as a function of temperature near the transformation point.

2. **Variational parallel**: Write the variational free energy expression F = E_q[log q(x) - log p(x,y)] and identify the structural correspondence:
   - q(x) corresponds to the current phase (the system's "belief" about its state)
   - p(x,y) corresponds to the Gibbs energy surface (the "true" model at given T, P)
   - Minimizing F corresponds to the system transforming to the phase with the lowest Gibbs energy

3. **Reflect**: In one paragraph, explain why this parallel is deeper than an analogy. What mathematical features do both minimization processes share?

## Discussion

1. At which scale did the Markov blanket concept feel most natural (atomic, grain, or component)? At which scale was it most challenging, and why?
2. How does the equilibrium vacancy calculation change your understanding of "defects" -- are they errors, or are they thermodynamically favored states? What does this imply for the concept of prediction error in Active Inference?
3. What limits the precision of your XRD phase fraction estimate, and how would you design an experiment to improve it? Is there a point of diminishing returns for measurement precision?
4. Does the mathematical parallel between Gibbs and variational free energy convince you that the two frameworks are deeply connected, or does it seem like a coincidence of mathematical form? What additional evidence would strengthen or weaken the connection?
