# Station: Planning (Research Methods)

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: Experimental design, model comparison, open problems
- **Topic**: Planning
- **Subtitle**: Open Problems and Research Frontiers in Active Inference
- **Lab Style**: Research Proposal
- **Audience**: PhD students and researchers
- **Tone**: Practical, methodologically rigorous, computationally concrete

## Content Guidance

This module must survey the major open problems that define the frontier of active inference research, presenting each as a concrete research program with identifiable testable predictions, methodological challenges, and existing preliminary evidence. The module should cover five frontier areas in depth: (1) **Scale-free inference** — does the free energy principle genuinely apply at all biological scales, from subcellular molecular networks to ecosystems? What empirical evidence would confirm or disconfirm scale-free active inference, and what are the methodological challenges of testing it (Ramstead et al., 2023)? (2) **Consciousness and the FEP** — can active inference models explain phenomenal experience, and what are the testable predictions (Seth, 2021)? Cover the relationship to integrated information theory, global workspace theory, and the specific predictions active inference makes about the neural correlates of consciousness (e.g., precision and the sense of presence). (3) **Embodied AI** — using active inference for robot control and embodied agent design (Tschantz et al., 2020); cover practical benchmarking against deep RL, sample efficiency, transfer learning, and the computational costs of real-time active inference. (4) **Computational psychiatry** — precision dysregulation as a unifying model of psychopathology (Parr et al., 2022; Adams et al., 2013); cover the computational phenotyping workflow for clinical populations, treatment response prediction, and the challenge of moving from group-level model differences to individual-level clinical utility. (5) **AGI and alignment** — implications of active inference for artificial general intelligence and AI safety (Friston et al., 2022); cover the relationship between expected free energy minimization and reward maximization, whether active inference agents are inherently aligned or misaligned, and the technical challenges of scaling active inference to complex environments. For each frontier, students should identify specific, falsifiable predictions and the experimental or computational methods that could test them. This module should inspire students to formulate their own research directions.

## Key Concepts

- **Scale-free inference**: The claim that the free energy principle applies at all scales of biological organization — from molecular self-assembly to cellular metabolism to neural computation to social cognition to ecological dynamics; testable via cross-scale Markov blanket identification and empirical testing of NESS conditions at each scale; methodological challenge of defining Markov blankets non-trivially at arbitrary scales
- **Consciousness and the FEP**: Active inference accounts of phenomenal experience — the relationship between precision, temporal depth, and subjective awareness; testable predictions about the neural correlates of consciousness (e.g., global precision changes under anesthesia, the relationship between interoceptive inference and the sense of self); comparison with integrated information theory (IIT) and global neuronal workspace theory (GNWT)
- **Embodied AI applications**: Active inference as a framework for robot control and embodied artificial agents — PyMDP and RxInfer.jl implementations for discrete and continuous control; benchmarking against deep RL on standard tasks (navigation, manipulation, exploration); advantages (sample efficiency, principled exploration via epistemic value) and disadvantages (computational cost, scalability limitations) of active inference for AI
- **Clinical computational psychiatry**: Precision dysregulation as a computational account of psychiatric disorders — aberrant precision weighting in autism (over-precise sensory predictions), schizophrenia (imprecise prior beliefs), anxiety (elevated volatility estimates), and depression (low expected precision of reward); computational phenotyping workflow for clinical populations; challenges of clinical translation (reliability, ecological validity, individual prediction)
- **AGI and alignment**: Active inference as a framework for understanding and designing artificial general intelligence — the relationship between expected free energy minimization and human-compatible objectives; whether the epistemic drive inherent in active inference produces inherently safe or unsafe exploration behavior; the technical challenge of specifying appropriate preference priors ($\mathbf{C}$ vectors) for AGI systems; connections to reward hacking, mesa-optimization, and goal misgeneralization

## Key References

- Ramstead, M. J. D., Sakthivadivel, D. A. R., Heins, C., et al. (2023). On Bayesian mechanics: A physics of and by beliefs. *Interface Focus*, 13(3), 20220029.
- Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Dutton.
- Tschantz, A., Seth, A. K., & Buckley, C. L. (2020). Learning action-oriented models through active inference. *PLOS Computational Biology*, 16(4), e1007805.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Friston, K. J., Da Costa, L., Sajid, N., Heins, C., Ueltzhöffer, K., Pavliotis, G. A., & Parr, T. (2022). The free energy principle made simpler but not too simple. *Physics Reports*, 1024, 1-29.
- Adams, R. A., Stephan, K. E., Brown, H. R., Frith, C. D., & Friston, K. J. (2013). The computational anatomy of psychosis. *Frontiers in Psychiatry*, 4, 47.
- Sajid, N., Tigas, P., Zakharov, A., Fountas, Z., & Friston, K. J. (2021). Exploration and preference satisfaction trade-off in reward-free active inference. *arXiv preprint arXiv:2104.04080*.

## Prerequisite Modules

- Module 04: Cognition (Bayesian model comparison as the core inferential tool for evaluating competing frontier hypotheses)
- Module 05: Action (active inference for motor control provides the foundation for embodied AI applications)
- Module 06: Learning (model fitting and validation pipeline required for all computational psychiatry and benchmarking work)

## Cross-Unit Connections

- **Advanced Theory** ([../../03_advanced_theory/08_planning/module.md](../../03_advanced_theory/08_planning/module.md)): Derives deep temporal models and sophisticated inference with recursive expected free energy evaluation — this module asks how to test those theoretical constructs experimentally and what open mathematical problems remain
- **Neuroscientific Frontiers** ([../../02_neuroscientific_frontiers/08_planning/module.md](../../02_neuroscientific_frontiers/08_planning/module.md)): Reviews hippocampal replay, prospective coding, and model-based planning in the brain — this module identifies the open neuroscientific questions (e.g., does replay implement active inference planning?) and the experimental methods to address them
- **Philosophical Foundations** ([../../01_philosophical_foundations/08_planning/module.md](../../01_philosophical_foundations/08_planning/module.md)): Examines imagination, counterfactual reasoning, and temporal consciousness — this module connects those philosophical questions to concrete research programs (consciousness science, embodied AI, clinical psychiatry) where they can be empirically pursued

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md) and [../../resources/glossary.md](../../resources/glossary.md).
