# FAQ: Active Inference for Metallurgy

> Frequently asked questions about the Active Inference & Metallurgy curriculum.

---

## General

**Q: What is Active Inference?**

A: Active Inference is the theory that all adaptive systems — from neurons to organisms to physical materials — work by constantly predicting their sensory inputs and acting to minimize the difference between predictions and reality ("prediction error"). It is grounded in the Free Energy Principle, which states that any system that persists must minimize a quantity called variational free energy.

**Q: Why apply Active Inference to metallurgy?**

A: The connection is more natural than it first appears. Metals literally minimize thermodynamic free energy — the Gibbs free energy G = H − TS governs phase stability, and phase transformations proceed to reduce G. Active Inference provides a unifying framework that connects this thermodynamic truth to modern concepts of information processing, prediction, and adaptive behavior. It reveals that a cooling alloy and a learning brain are both performing the same fundamental operation: minimizing free energy.

**Q: Do I need to know Active Inference before starting this course?**

A: No. The curriculum is self-contained. Each module introduces the Active Inference concept alongside its metallurgical counterpart. If you understand thermodynamics and materials science, you already have the intuitions — this course gives them a formal framework.

**Q: Do I need to know metallurgy before starting this course?**

A: A working knowledge of undergraduate-level materials science (crystal structures, phase diagrams, diffusion) is strongly recommended. The course does not teach metallurgy from scratch but rather reinterprets it through the Active Inference lens.

---

## Content

**Q: How is the course structured?**

A: Four courses, each covering the same 8 Active Inference topics from a different metallurgical perspective. See the [README](../README.md) for the full structure. You can work through one course sequentially, or study the same topic across all four courses using the [Cross-Course Map](./cross_course_map.md).

**Q: What software tools are used?**

A: Python, PyCalphad (computational thermodynamics), MTEX (texture analysis), and standard scientific computing libraries (NumPy, SciPy, Matplotlib). Course 4 also references SCADA systems and digital twin platforms.

**Q: Is there math in this course?**

A: Yes, at a moderate level. Equations are always grounded in physical meaning. You will encounter Gibbs free energy expressions, diffusion equations, nucleation barriers, and basic variational quantities. Dense measure-theoretic proofs are not included — the focus is on engineering application.

**Q: What are the labs like?**

A: Labs vary by course: Course 1 uses simulation labs (molecular dynamics, lattice models), Course 2 uses calculation labs (phase diagram computation), Course 3 uses image analysis labs (micrograph segmentation, EBSD analysis), and Course 4 uses digital twin labs (process simulation and control).

---

## Theory

**Q: Is the analogy between thermodynamic free energy and variational free energy exact?**

A: It is more than an analogy. Both can be derived from the same mathematical framework (variational principles on probability distributions). The Gibbs free energy of a thermodynamic system and the variational free energy of a Bayesian model both measure the "cost" of departure from equilibrium — thermodynamic equilibrium in one case, statistical equilibrium (accurate inference) in the other. See Friston (2019) for the formal connection.

**Q: How does a metal "perceive" anything?**

A: Not consciously, of course. But in the formal framework, "perception" means updating internal states based on external inputs. When a grain boundary absorbs a solute atom that changes its energy, it has functionally "perceived" a chemical signal and updated its state. The formalism does not require awareness — only the mathematical structure of inference.

**Q: Can Active Inference actually improve alloy design?**

A: The framework is most valuable as a conceptual tool for organizing the design process — choosing what to measure (epistemic value), what to optimize (pragmatic value), and how to balance exploration of novel compositions with exploitation of known systems. It also provides a principled foundation for Bayesian optimization and sequential experimental design, which are already transforming computational materials science.

---

## Navigation

- [Glossary](./glossary.md)
- [Home](../README.md)
