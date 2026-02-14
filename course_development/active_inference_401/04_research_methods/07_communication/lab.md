# Lab: Interdisciplinary Methods and Collaborative Research

> **Learning Goal:** Practice designing interdisciplinary projects, communicating across domains, and implementing open science.

## Part 1: Interdisciplinary Project Design

**Exercise**: Design a research project that requires expertise from at least 3 disciplines:

**Example project**: "Active Inference models of anxiety in adolescents during social media use"

| Discipline | Contribution | Key Methods |
|-----------|-------------|-------------|
| Computational neuroscience | Generative model of anxiety | POMDP specification, parameter fitting |
| Developmental psychology | Adolescent development theory | Longitudinal study design, age-appropriate tasks |
| Social media studies | Platform behavior data | Digital trace analysis, usage metrics |
| Clinical psychology | Assessment and intervention | Clinical measures (GAD-7), therapeutic protocols |

**Project structure**:

1. Aim 1 (Computational): Develop Active Inference model of social media-induced anxiety
2. Aim 2 (Behavioral): Validate model against adolescent behavioral data
3. Aim 3 (Clinical): Use model to predict which adolescents are at risk and design interventions

Design your own 3-discipline project. Specify each discipline's contribution and how they integrate.

{fill:textarea}

## Part 2: Communication Exercises

> **Learning Goal:** Translate Active Inference for different audiences.

**Exercise**: Write a 150-word explanation of "precision-weighted prediction errors" for each audience:

**For a neuroscientist**: Focus on synaptic gain modulation, NMDA receptors, cortical layers, and oscillatory signatures. Use technical neuroscience terminology.

{fill:textarea}

**For a clinical psychologist**: Focus on how confidence in beliefs vs. evidence determines interpretation. Use clinical examples (anxiety = too much weight on threat signals).

{fill:textarea}

**For a high school student**: Use everyday analogies (confidence in what you expect to happen vs. what actually happens). Avoid all jargon.

{fill:textarea}

Compare your three explanations. What was gained and lost in each translation?

{fill:textarea}

## Part 3: Open Science Implementation

> **Learning Goal:** Design a fully reproducible analysis.

**Exercise**: Design the reproducibility infrastructure for an Active Inference study:

| Component | Implementation | Tool |
|----------|---------------|------|
| Pre-registration | Register hypotheses, models, analysis plan | OSF or AsPredicted |
| Version control | All analysis code in Git repository | GitHub/GitLab |
| Data sharing | De-identified data in public repository | OSF, Dryad, or OpenNeuro |
| Model code | Publish model specification as runnable code | Python package or Jupyter notebook |
| Environment | Containerize computational environment | Docker or conda environment.yml |
| Documentation | Literate programming with embedded analysis | Jupyter notebooks + markdown |
| Analysis pipeline | End-to-end automated pipeline | Makefile or Snakemake |

Write the README for this repository, including instructions for reproducing all results.

{fill:textarea}

## Part 4: Workshop Design

> **Learning Goal:** Design an educational workshop.

**Exercise**: Design a 2-day workshop introducing Active Inference to cognitive neuroscience graduate students:

**Day 1: Foundations**

- Session 1 (2h): What is Active Inference? Core concepts without math (metaphors, intuitions)
- Session 2 (2h): The mathematics — free energy, generative models, policy selection
- Session 3 (2h): Hands-on: Building a simple Active Inference agent in pymdp

**Day 2: Applications**

- Session 4 (2h): DCM — how to apply Active Inference to neuroimaging
- Session 5 (2h): Computational psychiatry — clinical applications
- Session 6 (2h): Design your own study — participants work in interdisciplinary teams

For each session, specify: learning objectives, materials needed, and assessment.

{fill:textarea}

## Part 5: Reflection

In 300 words, reflect: Active Inference aspires to be a "theory of everything" for adaptive systems. But interdisciplinary ambition comes with risks — superficial application across domains, loss of disciplinary rigor, and over-promising. How do you balance the excitement of a unifying framework with the rigor needed for each specific application?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Project design | Multi-disciplinary integration |
| 2 | Scientific communication | Audience adaptation |
| 3 | Reproducibility | Open science infrastructure |
| 4 | Education | Workshop curriculum design |
| 5 | Critical reflection | Ambition vs. rigor |
