# Lab: Research Methods for Active Inference

## Objective

Design, execute, and report a complete research project applying Active Inference methodology to a specific empirical or theoretical problem. This capstone lab integrates computational modeling, experimental design, data analysis, and scholarly communication.

## Prerequisites

- Completion of or concurrent enrollment in all prior 401 tracks (Philosophical Foundations, Neuroscientific Frontiers, Advanced Theory)
- Proficiency in at least one Active Inference software toolkit (SPM/DCM, pymdp, RxInfer.jl)
- Graduate-level statistical competence (Bayesian model comparison, parameter estimation, posterior predictive checks)
- Experience with scientific writing and presentation

## Part 1: Research Proposal

1. **Problem Identification**: Select a research question amenable to Active Inference modeling. The question must be:
   - Novel (not a replication of existing published work)
   - Tractable within a semester time frame
   - Connected to at least two of the four course tracks
2. **Literature Review**: Provide a focused review (minimum 20 papers) situating your question within the Active Inference literature and adjacent fields.
3. **Formal Model Specification**: Specify your generative model in full mathematical detail:
   - State space (hidden states s, observations o, actions a)
   - Likelihood mapping p(o|s) with parameterization
   - Transition dynamics p(s'|s, a) with temporal structure
   - Prior preferences C, initial state prior D, policy prior E
   - Variational family q(s) and inference algorithm (variational message passing, belief propagation, sampling)
4. **Predictions**: Derive at least three quantitative predictions from your model, with comparison to at least one alternative model.

## Part 2: Implementation and Analysis

1. **Model Implementation**: Implement your generative model in a suitable framework:
   - For discrete state spaces: pymdp (Python) or custom implementation
   - For continuous state spaces: SPM (MATLAB), RxInfer.jl (Julia), or NumPyro (Python)
   - For multi-agent models: custom implementation with documented architecture
2. **Parameter Recovery**: Demonstrate that your model's parameters can be recovered from simulated data (identifiability analysis).
3. **Model Comparison**: If applicable, fit competing models to the same data and perform Bayesian model comparison (compute log model evidence, Bayes factors, or WAIC/LOO-CV).
4. **Sensitivity Analysis**: Characterize how model behavior depends on key parameters (precision, learning rate, temporal horizon, policy depth).

## Part 3: Scholarly Communication

1. **Manuscript**: Write a complete research paper (6000--10000 words) following the structure:
   - Abstract, Introduction, Methods (model specification + inference algorithm), Results, Discussion, Conclusion
   - All figures publication-quality with proper captions
   - All equations numbered and referenced
2. **Reproducibility Package**: Provide a complete code repository with:
   - README with installation and execution instructions
   - Requirements/environment specification
   - All scripts to reproduce figures and results
3. **Peer Review**: Conduct formal peer review of one other student's manuscript using standard journal review criteria.

## Deliverables

- Research proposal (Part 1): due week 4, 3000--5000 words
- Implementation and preliminary results (Part 2): due week 10, code repository + 2000-word progress report
- Final manuscript and reproducibility package (Part 3): due week 14
- Peer review report: due week 15, 1000--2000 words

## Discussion Requirements

- Week 5: Present your research proposal for seminar feedback (20 minutes + 15 minutes discussion)
- Week 11: Present preliminary results and methodological challenges (20 minutes + 15 minutes discussion)
- Week 15: Final presentation in conference-talk format (25 minutes + 10 minutes Q&A)
- Engage substantively with at least two other students' projects throughout the semester
