# Metallurgical Systems — Module 08: Planning — Discussion Questions

> Mix of analytical and applied questions for materials scientists and engineers.
> Questions 1-10 are analytical; Questions 11-20 are applied.

---

## Analytical Questions

1. How does the Active Inference concept of planning map onto the physical processes observed in crystal structures, defects, and fundamental thermodynamics? Identify at least three specific correspondences.

2. In what sense does a crystal lattice "minimize free energy" in the same way that an Active Inference agent minimizes variational free energy? Where does the analogy break down?

3. Compare the classical thermodynamic view of planning with the Active Inference interpretation. What additional insights does the FEP framework provide?

4. How does the concept of a Markov blanket help formalize the boundary conditions relevant to planning in metallurgical systems?

5. Explain how prediction error manifests in the context of planning during a non-equilibrium process such as rapid quenching of an Fe-C alloy.

6. How does the precision (inverse variance) of characterization measurements affect our ability to study planning in real materials?

7. Discuss the role of nested systems (atoms -> grains -> components) in the context of planning. How does information flow between scales?

8. What is the "generative model" that governs planning in a binary alloy system? How is this model encoded physically?

9. Compare how planning operates in a diffusion-controlled transformation versus a martensitic (diffusionless) transformation. What does this difference reveal about the "speed of inference" in materials?

10. How does the concept of epistemic value (information gain) apply to experimental design for studying planning?

---

## Applied Questions

11. You are characterizing a new Ti-6Al-4V component after additive manufacturing. Design an experimental protocol that maximizes the epistemic value (information gain) regarding planning in this material.

12. A heat treatment schedule for a Ni-based superalloy is producing inconsistent results. Using the Active Inference framework, diagnose where the "prediction error" is likely originating and propose corrective actions.

13. Map the Markov blanket of a single austenite grain during the eutectoid transformation. What are the sensory states, active states, and internal states?

14. Design a simple computational experiment (using Python/PyCalphad) to demonstrate planning in the Fe-C system. Describe the expected outputs.

15. How would you use the concept of planning to improve quality control in a continuous casting process? Propose specific sensor placements and data analysis strategies.

16. A grain boundary in a polycrystalline copper sample is migrating under annealing. Describe this process in Active Inference terms: what is the agent, what is it "predicting," and what action is it taking?

17. Compare the "learning" processes of two alloy development approaches: traditional trial-and-error versus CALPHAD-guided design. Frame both in terms of planning and model updating.

18. You are tasked with designing a new high-entropy alloy. How does expected free energy (balancing pragmatic and epistemic value) guide your experimental plan for studying planning?

19. Describe how digital twin technology implements planning in an industrial heat treatment furnace. What constitutes the twin's generative model, and how is prediction error minimized?

20. Reflect on a real manufacturing problem you have encountered (or a published case study). Reinterpret the problem through the lens of planning in Active Inference. What new insights does this framing provide?
