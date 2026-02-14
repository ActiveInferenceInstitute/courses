# Module 07: Communication — Interdisciplinary Methods and Collaborative Research

> **Course**: Active Inference 401 | **Unit**: Research Methods | **Audience**: Graduate students / researchers

## Learning Objectives

1. Design **interdisciplinary research** programs that apply Active Inference across domains.
2. Analyze methods for **communicating Active Inference** to non-specialist audiences.
3. Evaluate the role of **open science, reproducibility, and community building** in advancing the field.

## Key Concepts

### 1. Interdisciplinary Research Design

Active Inference is inherently interdisciplinary, spanning neuroscience, psychology, philosophy, physics, mathematics, robotics, and ecology. This creates both opportunities and challenges:

**Bridging disciplines**: Successful interdisciplinary projects require:

- A shared formal language (mathematics of free energy provides this)
- Translation protocols between domain-specific vocabularies
- Mutual respect for disciplinary expertise and methodological standards
- Clear specification of what each discipline contributes

**Cross-domain application areas**:

| Domain | Active Inference Application | Methods Used |
|--------|------------------------------|--------------|
| Neuroscience | Brain as inference engine | DCM, EEG, fMRI (Modules 01, 03) |
| Psychology | Decision-making, perception | Behavioral paradigms (Module 04) |
| Psychiatry | Computational disorders | Clinical translation (Module 06) |
| Robotics | Embodied agents | Implementation (Module 05) |
| Ecology | Organisms as FEP systems | Bayesian mechanics, field studies |
| Social science | Collective behavior | Multi-agent models, survey data |
| Philosophy | Mind, consciousness | Conceptual analysis, thought experiments |
| AI / ML | Intelligent agents | Algorithm development, benchmarking |

### 2. Communication Strategies

Communicating Active Inference to different audiences requires different approaches:

**To neuroscientists**: Emphasize empirical predictions, DCM results, neural implementation
**To psychologists**: Emphasize behavioral predictions, computational phenotyping, clinical applications
**To physicists**: Emphasize Bayesian mechanics, FEP derivation, connections to thermodynamics
**To engineers**: Emphasize control theory connections, robot implementations, algorithm design
**To clinicians**: Emphasize clinical utility, patient outcomes, treatment implications
**To the public**: Use metaphors (brain as scientist, prediction machine), avoid jargon, emphasize real-world applications

**Common misunderstandings to address**:

1. "The brain literally calculates Bayes' theorem" → Active Inference is a normative/computational-level theory; neurons need not literally perform Bayesian computation
2. "Free energy principle is unfalsifiable" → Specific implementations make testable predictions; the principle itself is a framework, not a hypothesis
3. "Active Inference solves everything" → It provides a framework; specific applications must be empirically validated

### 3. Open Science and Reproducibility

Active Inference research benefits from and should contribute to open science:

**Open-source software**: pymdp, SPM, RxInfer.jl — all publicly available. New tools should be open-source by default.

**Pre-registration**: Register hypotheses, models, and analysis plans before data collection. This prevents post-hoc model selection bias.

**Data sharing**: Share behavioral data, fitted parameters, and model specifications. This enables replication and meta-analysis.

**Reproducible analysis**: Use version-controlled code, containerized environments, and literate programming (Jupyter notebooks, R Markdown) to ensure analyses are reproducible.

### 4. Community and Collaboration

**Active Inference Institute**: Central hub for education, research coordination, and community building.

**Textbook groups**: Reading groups working through Parr, Pezzulo & Friston (2022) and related texts.

**Cross-institutional collaborations**: Multi-site studies using standardized tasks and models enable larger sample sizes and greater generalizability.

**Student mentorship**: Graduate students in Active Inference need training in multiple disciplines — mathematics, neuroscience, programming, and philosophy. Mentorship programs should span these areas.

### 5. Publication and Peer Review

**Writing for different journals**: Active Inference papers must be adapted for the audience:

- *Neuron*, *Nature Neuroscience*: Emphasize novel empirical findings
- *PLoS Computational Biology*: Emphasize model development and validation
- *Psychological Review*: Emphasize theoretical contributions
- *Biological Psychiatry*: Emphasize clinical relevance
- *IEEE/ICRA*: Emphasize engineering applications

**Review challenges**: Papers may be reviewed by experts in one domain who lack expertise in another aspect of the work. Include clear, self-contained introductions to each disciplinary component.

## Summary

Interdisciplinary Active Inference research requires bridging domain-specific vocabularies with shared mathematical formalism, adapting communication strategies for different audiences, and embracing open science practices. Community building through the Active Inference Institute and cross-institutional collaboration accelerates the field's development.

## Further Reading

- Parr, T., Pezzulo, G. & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Active Inference Institute. <https://www.activeinference.org/>
- Ramstead, M. J. D. et al. (2020). An introduction to the free energy principle and related research. *Physics of Life Reviews*, 34, 1-5.
