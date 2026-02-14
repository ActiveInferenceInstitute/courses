#!/usr/bin/env bash
# Generate all 4 units × 8 modules × 7 files for Active Inference & Metallurgy
set -euo pipefail

BASE="/Users/4d/Documents/GitHub/courses/course_development/domains/active_inference_metallurgy"

# ─── Course metadata arrays ───
COURSE_DIRS=("01_metallurgical_systems" "02_thermodynamic_inference" "03_microstructural_evolution" "04_process_optimization")
COURSE_NAMES=("Metallurgical Systems" "Thermodynamic Inference" "Microstructural Evolution" "Process Optimization")
COURSE_PERSPECTIVES=("Crystal structures, defects, and fundamental thermodynamics" "Phase equilibria, transformation kinetics, and CALPHAD" "Nucleation, grain growth, precipitation, and characterization" "Heat treatment, welding, additive manufacturing, Industry 4.0")
COURSE_AUDIENCES=("Materials science graduate students and metallurgical engineers" "Thermodynamics specialists and computational materials scientists" "Microscopists, characterization engineers, and microstructure scientists" "Process engineers, manufacturing engineers, and Industry 4.0 specialists")
COURSE_LABS=("Simulation Lab" "Calculation Lab" "Image Analysis Lab" "Digital Twin Lab")

MODULE_TOPICS=("systems" "agents" "perception" "cognition" "action" "learning" "communication" "planning")
MODULE_NAMES=("Systems" "Agents" "Perception" "Cognition" "Action" "Learning" "Communication" "Planning")

# ─── Module titles per course (4 courses x 8 modules) ───
# C1: Metallurgical Systems
C1_TITLES=("Crystal Lattices as Markov Blankets" "Atoms and Defects as Agents" "X-Ray Diffraction and Spectroscopic Sensing" "Lattice Energy and First-Principles Cognition" "Deformation and Alloying as Material Action" "The Arc of Alloy Development" "Diffusion as Atomic Communication" "Alloy Design as Strategic Planning")
C1_SUBTOPICS=("Unit cells, crystal boundaries, Bravais lattices, atomic-scale system boundaries" "Vacancies, dislocations, solute atoms, interstitials as active entities in the lattice" "XRD, EDS, WDS, XPS — structure determination as sensory inference" "DFT calculations, interatomic potentials, lattice energy minimization as internal modeling" "Slip systems, twinning, solid solution strengthening, work hardening as system action" "Bronze Age to superalloys — how materials science learned over millennia" "Fick's laws, atomic migration, interdiffusion couples, Kirkendall effect" "Compositional design, property-performance maps, multi-objective optimization")

# C2: Thermodynamic Inference
C2_TITLES=("Phase Diagrams as Generative Models" "Chemical Species as Inference Agents" "Thermal Analysis and Calorimetric Sensing" "Phase Stability Computation and CALPHAD Cognition" "Phase Transformation Kinetics as Thermodynamic Action" "CALPHAD Assessment and Machine Learning" "Interface Energy and Thermodynamic Signaling" "TTT and CCT Diagram Planning")
C2_SUBTOPICS=("Binary and ternary phase diagrams as predictive maps, tie lines, lever rule" "Diffusing elements seeking equilibrium partitioning, activity, chemical potential" "DSC, DTA, dilatometry — sensing phase transitions through thermal signatures" "Thermo-Calc, PyCalphad, Gibbs energy minimization, Scheil solidification" "Nucleation barriers, Johnson-Mehl-Avrami kinetics, growth rates, TTT curves" "Database assessment cycles, machine learning for phase prediction, ICSD" "Interfacial free energy, wetting angles, segregation coefficients, Gibbs adsorption" "Transformation scheduling, cooling path design, CCT overlay, hardenability")

# C3: Microstructural Evolution
C3_TITLES=("Grain Boundaries as System Boundaries" "Nuclei as Autonomous Agents" "Microscopy and EBSD as Perceptual Systems" "Microstructure Prediction and Computational Modeling" "Grain Growth and Coarsening as Microstructural Action" "Adaptive Characterization and 4D Imaging" "Grain Boundary Networks and Communication Pathways" "Microstructure Engineering and Design")
C3_SUBTOPICS=("Polycrystalline architecture, grain boundary character, misorientation, CSL boundaries" "Critical nucleus formation, heterogeneous vs homogeneous nucleation, Zener pinning" "Optical microscopy, SEM, TEM, EBSD, orientation imaging — resolving hidden microstructure" "Phase-field modeling, Monte Carlo simulation, cellular automata, JMAK models" "Normal and abnormal grain growth, Ostwald ripening, precipitate coarsening" "Serial sectioning, synchrotron 4D-XCT, in-situ TEM, time-resolved characterization" "Triple junctions, percolation paths, grain boundary engineering, GB character distribution" "Grain size control, texture design, precipitation hardening schedules, thermo-mechanical processing")

# C4: Process Optimization
C4_TITLES=("Manufacturing Process as Inference System" "Sensors and Controllers as Process Agents" "In-Situ Monitoring and Non-Destructive Testing" "Digital Twin Cognition and Process Simulation" "Heat Treatment and Quenching as Process Action" "Closed-Loop Control and Adaptive Manufacturing" "SCADA, IoT, and Industrial Data Pipelines" "Process Route Optimization and the Digital Thread")
C4_SUBTOPICS=("Furnace, rolling mill, or AM printer as bounded inference systems, process boundaries" "Thermocouples, pyrometers, load cells, PLC controllers as sensor-actuator agent pairs" "In-situ XRD, infrared monitoring, ultrasonic testing, eddy current — real-time sensing" "FEA, CFD, surrogate models, ML-based process simulation as internal process models" "Austenitizing, quenching, tempering, aging, annealing schedules as process policies" "Statistical process control, reinforcement learning, Bayesian optimization for manufacturing" "Industrial IoT, OPC-UA, MES/ERP integration, data lakes for manufacturing intelligence" "Multi-step schedule optimization, digital thread from design to service, process-structure-property linkage")

ALL_TITLES=("${C1_TITLES[@]}" "${C2_TITLES[@]}" "${C3_TITLES[@]}" "${C4_TITLES[@]}")
ALL_SUBTOPICS=("${C1_SUBTOPICS[@]}" "${C2_SUBTOPICS[@]}" "${C3_SUBTOPICS[@]}" "${C4_SUBTOPICS[@]}")

# ─── Generate files ───
for ci in 0 1 2 3; do
    CDIR="${BASE}/${COURSE_DIRS[$ci]}"
    CNAME="${COURSE_NAMES[$ci]}"
    CPERSP="${COURSE_PERSPECTIVES[$ci]}"
    CAUD="${COURSE_AUDIENCES[$ci]}"
    CLAB="${COURSE_LABS[$ci]}"

    mkdir -p "$CDIR"

    # ── Unit README ──
    cat > "$CDIR/README.md" << UREADME
# ${CNAME}

> Part of **Active Inference for Metallurgy** | [Curriculum Home](../README.md)

## Overview

**${CNAME}** explores Active Inference through the lens of ${CPERSP,,}. This course is designed for ${CAUD}.

**Tone**: Engineering-focused. ${CPERSP}.

## Modules

| # | Topic | Subtitle | Lab Type |
| --- | --- | --- | --- |
UREADME

    for mi in 0 1 2 3 4 5 6 7; do
        idx=$((ci * 8 + mi))
        mn=$((mi + 1))
        printf "| %d | [%s](./%02d_%s/README.md) | %s | %s |\n" "$mn" "${MODULE_NAMES[$mi]}" "$mn" "${MODULE_TOPICS[$mi]}" "${ALL_TITLES[$idx]}" "$CLAB" >> "$CDIR/README.md"
    done

    cat >> "$CDIR/README.md" << 'UREADME2'

## Files Per Module

| File | Description |
| --- | --- |
| module.md | Full lesson content |
| questions.md | Study questions |
| practice_quiz.md | Practice quiz |
| lab.md | Lab exercise |
| dashboard.html | Interactive dashboard |
| README.md | Navigation and overview |
| AGENTS.md | Conventions and metadata |

## Resources

- [Glossary](../resources/glossary.md)
- [Notation Table](../resources/notation_table.md)
- [References](../resources/references.md)
- [Cross-Course Map](../resources/cross_course_map.md)
UREADME2

    # ── Unit AGENTS ──
    cat > "$CDIR/AGENTS.md" << UAGENTS
# ${CNAME} — Agent Guidelines

> **Quick Navigation**: [Unit README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: ${CPERSP}
- **Lab Style**: ${CLAB}
- **Audience**: ${CAUD}
- **Tone**: Technical / engineering-focused

Ensure all content adheres to [../resources/notation_table.md](../resources/notation_table.md).
UAGENTS

    # ── Unit syllabus ──
    cat > "$CDIR/syllabus.md" << USYLL
# Syllabus: ${CNAME}

> Part of **Active Inference for Metallurgy**

## Course Overview

This unit covers Active Inference through the lens of ${CPERSP,,}. It is designed for ${CAUD}.

## Schedule

| Week | Module | Topic |
| --- | --- | --- |
USYLL

    for mi in 0 1 2 3 4 5 6 7; do
        idx=$((ci * 8 + mi))
        mn=$((mi + 1))
        printf "| %d | %s | %s |\n" "$mn" "${MODULE_NAMES[$mi]}" "${ALL_TITLES[$idx]}" >> "$CDIR/syllabus.md"
    done

    cat >> "$CDIR/syllabus.md" << 'USYLL2'

## Assessment

- Weekly practice quizzes (self-assessment)
- Laboratory exercises (hands-on application)
- Discussion questions (analytical and applied)

## Prerequisites

- Undergraduate-level materials science or physical metallurgy
- Basic thermodynamics (Gibbs free energy, phase diagrams)
- Familiarity with Python for computational exercises
USYLL2

    # ── Generate 8 modules ──
    for mi in 0 1 2 3 4 5 6 7; do
        idx=$((ci * 8 + mi))
        mn=$((mi + 1))
        MDIR=$(printf "%s/%02d_%s" "$CDIR" "$mn" "${MODULE_TOPICS[$mi]}")
        MTITLE="${ALL_TITLES[$idx]}"
        MSUBT="${ALL_SUBTOPICS[$idx]}"
        MNAME="${MODULE_NAMES[$mi]}"
        MNUM=$(printf "%02d" "$mn")
        SK="ai_metallurgy_${COURSE_DIRS[$ci]}_${MNUM}_${MODULE_TOPICS[$mi]}"

        mkdir -p "$MDIR"

        # ── module.md ──
        cat > "$MDIR/module.md" << MODEOF
# ${MTITLE}

## Introduction

This module explores **${MNAME}** within the context of **${CNAME}**. In the Active Inference framework, ${MNAME,,} plays a critical role in how systems maintain their identity, process information, and adapt to perturbation. Here we examine this through the lens of ${CPERSP,,}.

**Key themes**: ${MSUBT}

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **${MNAME}** within the Active Inference framework as it applies to metallurgical systems
2. Identify how ${MNAME,,} manifests in ${CPERSP,,}
3. Connect the formal FEP concept of ${MNAME,,} to specific metallurgical phenomena
4. Analyze real-world case studies involving ${MNAME,,} in materials engineering
5. Apply ${MNAME,,} principles to solve practical metallurgical problems

---

## Key Concepts

### 1. ${MNAME} in the Active Inference Framework

In Active Inference, ${MNAME,,} refers to the process by which systems maintain and update their relationship with the environment. For metallurgical systems, this maps directly onto physical processes: ${MSUBT}.

The Free Energy Principle provides a unifying lens: every metallurgical phenomenon involving ${MNAME,,} can be understood as a system minimizing the difference between its current state and its preferred (equilibrium) state.

### 2. ${MNAME} at the Atomic Scale

At the most fundamental level, ${MNAME,,} in metallurgy operates through atomic-scale mechanisms. Atoms in a crystal lattice interact with their neighbors according to interatomic potentials, and the collective behavior of these interactions gives rise to macroscopic material properties.

### 3. ${MNAME} at the Mesoscale

Moving up in scale, ${MNAME,,} manifests through microstructural features — grain boundaries, precipitates, phase interfaces, and defect networks. These mesoscale structures mediate between atomic-level events and engineering-scale properties.

### 4. ${MNAME} at the Engineering Scale

At the largest scale relevant to this module, ${MNAME,,} is expressed through macroscopic material behavior and process-level phenomena. This is where the metallurgist's interventions — heat treatments, deformation processes, and compositional design — interact with the material's inherent tendencies.

### 5. The FEP Bridge: From Thermodynamics to Inference

The deepest insight of this curriculum is that thermodynamic free energy minimization and variational free energy minimization share the same mathematical structure. In the context of ${MNAME,,}, this means that the physical processes governing metallurgical behavior are formally analogous to the inference processes governing adaptive systems.

---

## Applications

### Case Study: ${MNAME} in Steel Processing

Consider a plain carbon steel (Fe-0.4wt%C) undergoing heat treatment. The concept of ${MNAME,,} manifests concretely: the material system processes information (temperature, composition gradients), updates its internal state (crystal structure, phase fractions), and acts to minimize its free energy through phase transformations.

### Case Study: ${MNAME} in Aluminum Alloy Design

In Al-Cu precipitation-hardening alloys (such as 2024-T3), ${MNAME,,} operates through the sequence of metastable precipitate formation: GP zones → θ″ → θ′ → θ (Al₂Cu). Each stage represents the system's ongoing inference about its equilibrium state.

---

## Cross-References

- For parallel treatment in other courses, see the [Cross-Course Map](../../resources/cross_course_map.md)
- See the [Glossary](../../resources/glossary.md) for term definitions
- See the [Notation Table](../../resources/notation_table.md) for symbol conventions

---

## Summary

| Concept | Metallurgical Meaning |
|---------|----------------------|
| ${MNAME} | ${MSUBT} |
| FEP Connection | Free energy minimization drives ${MNAME,,} in both thermodynamic and inferential frameworks |
| Scale | Operates from atomic (Å) through mesoscale (μm) to engineering (m) |
| Key Techniques | Characterization and modeling tools specific to ${MNAME,,} in this context |

---

## References

- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.
- Porter, D. A., Easterling, K. E., & Sherif, M. Y. (2021). *Phase Transformations in Metals and Alloys* (4th ed.). CRC Press.
- Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.
- Callister, W. D., & Rethwisch, D. G. (2020). *Materials Science and Engineering* (10th ed.). Wiley.
MODEOF

        # ── questions.md ──
        cat > "$MDIR/questions.md" << QEOF
# ${CNAME} — Module ${MNUM}: ${MNAME} — Discussion Questions

> Mix of analytical and applied questions for materials scientists and engineers.
> Questions 1–10 are analytical; Questions 11–20 are applied.

---

## Analytical Questions

1. How does the Active Inference concept of ${MNAME,,} map onto the physical processes observed in ${CPERSP,,}? Identify at least three specific correspondences.

2. In what sense does a crystal lattice "minimize free energy" in the same way that an Active Inference agent minimizes variational free energy? Where does the analogy break down?

3. Compare the classical thermodynamic view of ${MNAME,,} with the Active Inference interpretation. What additional insights does the FEP framework provide?

4. How does the concept of a Markov blanket help formalize the boundary conditions relevant to ${MNAME,,} in metallurgical systems?

5. Explain how prediction error manifests in the context of ${MNAME,,} during a non-equilibrium process such as rapid quenching of an Fe-C alloy.

6. How does the precision (inverse variance) of characterization measurements affect our ability to study ${MNAME,,} in real materials?

7. Discuss the role of nested systems (atoms → grains → components) in the context of ${MNAME,,}. How does information flow between scales?

8. What is the "generative model" that governs ${MNAME,,} in a binary alloy system? How is this model encoded physically?

9. Compare how ${MNAME,,} operates in a diffusion-controlled transformation versus a martensitic (diffusionless) transformation. What does this difference reveal about the "speed of inference" in materials?

10. How does the concept of epistemic value (information gain) apply to experimental design for studying ${MNAME,,}?

---

## Applied Questions

11. You are characterizing a new Ti-6Al-4V component after additive manufacturing. Design an experimental protocol that maximizes the epistemic value (information gain) regarding ${MNAME,,} in this material.

12. A heat treatment schedule for a Ni-based superalloy is producing inconsistent results. Using the Active Inference framework, diagnose where the "prediction error" is likely originating and propose corrective actions.

13. Map the Markov blanket of a single austenite grain during the eutectoid transformation. What are the sensory states, active states, and internal states?

14. Design a simple computational experiment (using Python/PyCalphad) to demonstrate ${MNAME,,} in the Fe-C system. Describe the expected outputs.

15. How would you use the concept of ${MNAME,,} to improve quality control in a continuous casting process? Propose specific sensor placements and data analysis strategies.

16. A grain boundary in a polycrystalline copper sample is migrating under annealing. Describe this process in Active Inference terms: what is the agent, what is it "predicting," and what action is it taking?

17. Compare the "learning" processes of two alloy development approaches: traditional trial-and-error versus CALPHAD-guided design. Frame both in terms of ${MNAME,,} and model updating.

18. You are tasked with designing a new high-entropy alloy. How does expected free energy (balancing pragmatic and epistemic value) guide your experimental plan for studying ${MNAME,,}?

19. Describe how digital twin technology implements ${MNAME,,} in an industrial heat treatment furnace. What constitutes the twin's generative model, and how is prediction error minimized?

20. Reflect on a real manufacturing problem you have encountered (or a published case study). Reinterpret the problem through the lens of ${MNAME,,} in Active Inference. What new insights does this framing provide?
QEOF

        # ── practice_quiz.md ──
        cat > "$MDIR/practice_quiz.md" << PQEOF
# Practice Quiz: ${CNAME} — Module ${MNUM}: ${MNAME}

**Name**: ______________________ **Date**: ______________________

---

## Part A: Multiple Choice

1. In the Active Inference framework, ${MNAME,,} in a metallurgical system is best understood as:

A) A random process with no thermodynamic driving force
B) A process driven by the minimization of free energy (both thermodynamic and variational)
C) An externally imposed constraint with no internal dynamics
D) A purely kinetic phenomenon unrelated to equilibrium

2. The Markov blanket of a crystal grain includes:

A) Only the atoms at the grain interior
B) The grain boundary — mediating interactions between the grain's internal states and external environment
C) The entire polycrystalline sample
D) Only the external temperature field

3. In the context of ${MNAME,,}, "prediction error" in a metallurgical system corresponds to:

A) A measurement instrument malfunction
B) The deviation between the system's current state and its equilibrium (predicted) state
C) An error in the periodic table
D) The difference between two competing phase diagrams

4. Which characterization technique provides the highest precision for studying crystallographic ${MNAME,,}?

A) Visual inspection
B) Hardness testing
C) Electron backscatter diffraction (EBSD)
D) Density measurement

5. The thermodynamic free energy G = H − TS and the variational free energy F share:

A) No mathematical relationship
B) The same fundamental structure — both measure departure from equilibrium
C) Identical numerical values in all cases
D) Only a metaphorical connection

6. When a supersaturated Al-Cu alloy forms GP zones during aging, this is an example of:

A) The system increasing its free energy
B) Active inference — the system acting to minimize its thermodynamic free energy
C) A violation of the Second Law
D) Random atomic motion with no driving force

7. Nested Markov blankets in metallurgy refer to:

A) Multiple layers of insulation around a furnace
B) The hierarchical structure: atoms → unit cells → grains → phases → components
C) A type of heat treatment schedule
D) Overlapping X-ray diffraction patterns

---

## Part B: Short Analysis

1. A martensitic transformation in steel occurs in milliseconds, while pearlitic transformation takes minutes to hours. Using Active Inference language, explain why these two "actions" of the system operate at such different timescales. What does this tell us about the system's inference process?

2. You have two characterization methods for studying ${MNAME,,}: optical microscopy (fast, low cost, limited resolution) and TEM (slow, expensive, atomic resolution). Using the concept of epistemic value and precision, explain how you would decide which to use for a given research question.

3. Describe how a CALPHAD database functions as a "generative model" for a metallurgical system. What happens when the database predictions diverge from experimental observations? How is the model updated, and what is the Active Inference term for this process?
PQEOF

        # ── lab.md ──
        cat > "$MDIR/lab.md" << LABEOF
# Lab: Exploring ${MNAME} in ${CNAME}

## Objectives

> **Learning Goal:** Apply the Active Inference concept of ${MNAME,,} to a concrete metallurgical scenario using ${CLAB,,} techniques.

This is a **${CLAB,,} exercise** designed for materials scientists and engineers. The focus is on connecting theoretical concepts to practical analysis.

---

## Part 1: System Definition (10 min)

Choose a metallurgical system to analyze. Suggested options:

- Fe-0.4wt%C steel undergoing austenitization and cooling
- Al-4wt%Cu alloy during precipitation aging
- Ti-6Al-4V produced by laser powder bed fusion
- Pure copper undergoing recrystallization after cold work

{fill:textarea, placeholder: "Selected system and brief description (alloy, processing condition, relevant phenomena)"}

---

## Part 2: ${MNAME} Analysis (25 min)

### 2A: Identify the Active Inference Components

Map your chosen system onto the Active Inference framework in the context of ${MNAME,,}:

| Component | Your System |
|-----------|-------------|
| System boundary (Markov blanket) | |
| Internal states | |
| External states | |
| Sensory states | |
| Active states | |

{fill:textarea, placeholder: "Complete the mapping table for your metallurgical system"}

### 2B: ${MNAME} Dynamics

Describe how ${MNAME,,} operates in your system:

- What is the driving force (free energy gradient)?
- What is the timescale?
- What characterization technique would you use to observe it?

{fill:textarea, placeholder: "Describe the dynamics of ${MNAME,,} in your system"}

---

## Part 3: Quantitative Exercise (20 min)

Perform a simple calculation or simulation related to ${MNAME,,} in your system:

- If computational: use Python with PyCalphad, NumPy, or similar
- If analytical: use thermodynamic relations (Gibbs energy, diffusion equation, nucleation barrier)

{fill:textarea, placeholder: "Show your calculation or simulation code and results"}

---

## Part 4: Reflection (10 min)

1. How did the Active Inference framework change your understanding of ${MNAME,,} in this system?
2. What prediction error exists between the equilibrium model and the real behavior of your system?
3. How could you reduce this prediction error through better characterization or modeling?

{fill:textarea, placeholder: "Reflect on the Active Inference interpretation"}

---

## Summary

| Analysis Component | Key Finding |
|-------------------|-------------|
| System analyzed | |
| ${MNAME} mechanism identified | |
| Driving force | |
| Main prediction error | |
| Recommended next characterization | |

{fill:textarea, placeholder: "Complete the summary table"}
LABEOF

        # ── dashboard.html ──
        cat > "$MDIR/dashboard.html" << DASHEOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard: ${MNAME} — ${CNAME}</title>
    <style>
        :root {
            --accent: #4a90d9;
            --accent-glow: #4a90d922;
            --bg: #0f172a;
            --card: #1e293b;
            --border: #334155;
            --text: #e2e8f0;
            --muted: #94a3b8;
            --dim: #64748b;
            --green: #22c55e;
            --red: #ef4444;
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:'Segoe UI',system-ui,-apple-system,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
        .hero { background:linear-gradient(135deg, #4a90d9, #2c3e50); padding:48px 24px 36px; text-align:center; }
        .hero h1 { font-size:2rem; color:#fff; margin-bottom:8px; }
        .hero .sub { font-size:1.1rem; color:rgba(255,255,255,.85); margin-bottom:12px; }
        .hero .tag { display:inline-block; background:rgba(255,255,255,.2); color:#fff; padding:4px 14px; border-radius:20px; font-size:.8rem; backdrop-filter:blur(4px); }
        .nav { display:flex; justify-content:center; gap:6px; flex-wrap:wrap; padding:14px 24px; background:#1a2332; border-bottom:1px solid var(--border); }
        .nav a { color:var(--muted); text-decoration:none; font-size:.85rem; padding:6px 14px; border:1px solid var(--border); border-radius:8px; transition:all .2s; }
        .nav a:hover,.nav a.active { color:var(--accent); border-color:var(--accent); background:var(--accent-glow); }
        .content { max-width:1100px; margin:0 auto; padding:24px; }
        .stitle { color:var(--accent); font-size:1.25rem; margin:32px 0 16px; padding-bottom:8px; border-bottom:2px solid var(--border); }
        .stitle:first-child { margin-top:0; }
        .cgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; }
        .concept-card { background:var(--card); padding:20px; border-radius:12px; border:1px solid var(--border); cursor:pointer; transition:transform .2s,border-color .2s; }
        .concept-card:hover { transform:translateY(-2px); border-color:var(--accent); }
        .concept-card h3 { display:flex; justify-content:space-between; align-items:center; font-size:1rem; margin-bottom:8px; }
        .concept-card h3 .toggle { font-size:1.2rem; color:var(--dim); transition:transform .3s; }
        .concept-card.open h3 .toggle { transform:rotate(45deg); }
        .concept-card .brief { color:var(--muted); font-size:.9rem; }
        .concept-card .detail { display:none; color:var(--muted); font-size:.85rem; margin-top:12px; padding-top:12px; border-top:1px solid var(--border); line-height:1.7; }
        .concept-card.open .detail { display:block; }
        .meter { background:var(--border); border-radius:8px; height:6px; overflow:hidden; margin-top:14px; }
        .meter-fill { height:100%; border-radius:8px; background:linear-gradient(90deg,var(--accent),#4a90d988); transition:width 1s ease; }
        .meter-label { color:var(--dim); font-size:.7rem; margin-top:4px; }
        .quiz-box { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .qprog { color:var(--dim); font-size:.85rem; margin-bottom:12px; }
        .qq { font-size:1rem; margin-bottom:16px; font-weight:500; }
        .qbtn { background:rgba(255,255,255,.03); color:var(--text); border:1px solid var(--border); padding:12px 16px; border-radius:10px; cursor:pointer; display:block; width:100%; text-align:left; margin:6px 0; transition:all .2s; font-size:.9rem; }
        .qbtn:hover:not(:disabled) { background:rgba(255,255,255,.08); border-color:var(--accent); }
        .qbtn.correct { background:#166534; border-color:var(--green); color:#bbf7d0; }
        .qbtn.wrong { background:#7f1d1d; border-color:var(--red); color:#fecaca; }
        .qbtn:disabled { cursor:default; opacity:.85; }
        .qexp { margin-top:12px; padding:12px; border-radius:10px; font-size:.9rem; display:none; animation:fadeIn .3s; }
        @keyframes fadeIn { from{opacity:0;transform:translateY(4px)} to{opacity:1;transform:translateY(0)} }
        .qnav { display:flex; gap:8px; margin-top:16px; }
        .qnav button { background:rgba(255,255,255,.05); color:var(--text); border:1px solid var(--border); padding:8px 18px; border-radius:8px; cursor:pointer; transition:all .2s; font-size:.85rem; }
        .qnav button:hover:not(:disabled) { border-color:var(--accent); color:var(--accent); }
        .qnav button:disabled { opacity:.3; cursor:default; }
        #score-box { display:none; margin-top:16px; padding:20px; background:rgba(0,0,0,.2); border-radius:12px; text-align:center; animation:fadeIn .5s; }
        .cklist { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .cklist label { display:flex; align-items:flex-start; gap:10px; padding:8px 0; color:var(--muted); font-size:.9rem; cursor:pointer; transition:color .2s; }
        .cklist label:hover { color:var(--text); }
        .cklist input[type=checkbox] { margin-top:3px; accent-color:var(--accent); width:18px; height:18px; flex-shrink:0; }
        .cklist .done { color:var(--accent); text-decoration:line-through; opacity:.7; }
        .pbar { background:var(--border); border-radius:8px; height:8px; overflow:hidden; margin-top:16px; }
        .pfill { height:100%; border-radius:8px; background:var(--accent); transition:width .5s ease; width:0; }
        .ptxt { color:var(--dim); font-size:.8rem; margin-top:6px; }
        .mnav { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .mgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:10px; }
        .module-link { display:block; padding:14px; background:var(--bg); border:1px solid var(--border); border-radius:10px; color:var(--muted); text-decoration:none; font-size:.85rem; transition:all .2s; }
        .module-link:hover { border-color:var(--accent); color:var(--accent); transform:translateY(-1px); }
        .module-link.current { border-color:var(--accent); background:var(--accent-glow); }
        .module-link strong { display:block; color:var(--text); margin-bottom:2px; font-size:.9rem; }
        .module-link.current strong { color:var(--accent); }
        footer { margin-top:48px; padding:24px; text-align:center; color:var(--dim); font-size:.8rem; border-top:1px solid var(--border); }
        @media(max-width:600px) { .hero h1{font-size:1.5rem;} .cgrid,.mgrid{grid-template-columns:1fr;} .content{padding:16px;} }
    </style>
</head>
<body>
    <div class="hero">
        <h1>Module ${MNUM}: ${MNAME} in ${CNAME}</h1>
        <p class="sub">${MTITLE}</p>
        <span class="tag">Active Inference: Metallurgy — ${CNAME}</span>
    </div>

    <nav class="nav">
        <a href="module.md">Lecture</a>
        <a href="questions.md">Questions</a>
        <a href="practice_quiz.md">Quiz</a>
        <a href="lab.md">Lab</a>
        <a class="active" href="#">Dashboard</a>
    </nav>

    <div class="content">
        <h2 class="stitle">Key Concepts</h2>
        <div class="cgrid">
            <div class="concept-card" onclick="this.classList.toggle('open')">
                <h3>${MNAME} as Free Energy Minimization <span class="toggle">+</span></h3>
                <p class="brief">How ${MNAME,,} in metallurgical systems maps onto the FEP.</p>
                <div class="detail">${MSUBT}. The fundamental connection: both thermodynamic and variational free energy measure departure from equilibrium.</div>
                <div class="meter"><div class="meter-fill" style="width:70%"></div></div>
                <div class="meter-label">Mastery: 70%</div>
            </div>
            <div class="concept-card" onclick="this.classList.toggle('open')">
                <h3>Multi-Scale ${MNAME} <span class="toggle">+</span></h3>
                <p class="brief">${MNAME} operates from atomic to engineering scales.</p>
                <div class="detail">Nested Markov blankets: atoms within unit cells within grains within phases within components. Each scale has its own inference dynamics.</div>
                <div class="meter"><div class="meter-fill" style="width:50%"></div></div>
                <div class="meter-label">Mastery: 50%</div>
            </div>
            <div class="concept-card" onclick="this.classList.toggle('open')">
                <h3>Characterization as Perception <span class="toggle">+</span></h3>
                <p class="brief">How we observe ${MNAME,,} through measurement.</p>
                <div class="detail">Every characterization technique is a sensory channel with specific precision and resolution. Choosing the right technique maximizes epistemic value.</div>
                <div class="meter"><div class="meter-fill" style="width:40%"></div></div>
                <div class="meter-label">Mastery: 40%</div>
            </div>
        </div>

        <h2 class="stitle">Self-Assessment Quiz</h2>
        <div class="quiz-box">
            <div class="qprog" id="qprog">Question 1 of 3</div>
            <div id="qc"></div>
            <div class="qnav">
                <button id="pbtn" onclick="prevQ()" disabled>&larr; Previous</button>
                <button id="nbtn" onclick="nextQ()">Next &rarr;</button>
            </div>
            <div id="score-box"></div>
        </div>

        <h2 class="stitle">Learning Objectives</h2>
        <div class="cklist" id="cklist">
            <label><input type="checkbox"> Define ${MNAME,,} within the Active Inference framework for metallurgical systems.</label>
            <label><input type="checkbox"> Identify how ${MNAME,,} manifests in ${CPERSP,,}.</label>
            <label><input type="checkbox"> Connect FEP concepts to specific metallurgical phenomena.</label>
            <label><input type="checkbox"> Analyze case studies involving ${MNAME,,} in materials engineering.</label>
            <label><input type="checkbox"> Apply ${MNAME,,} principles to practical problems.</label>
            <div class="pbar"><div class="pfill" id="pfill"></div></div>
            <p class="ptxt" id="ptxt">0 of 5 complete</p>
        </div>

        <h2 class="stitle">Module Navigation</h2>
        <div class="mnav">
            <div class="mgrid">
DASHEOF

        # Add module navigation links
        for ni in 0 1 2 3 4 5 6 7; do
            nn=$((ni + 1))
            nnum=$(printf "%02d" "$nn")
            nidx=$((ci * 8 + ni))
            ntitle="${ALL_TITLES[$nidx]}"
            if [ "$ni" -eq "$mi" ]; then
                echo "<a class=\"module-link current\" href=\"#\"><strong>Module ${nnum}: ${MODULE_NAMES[$ni]}</strong>${ntitle}</a>" >> "$MDIR/dashboard.html"
            else
                echo "<a class=\"module-link\" href=\"../${nnum}_${MODULE_TOPICS[$ni]}/dashboard.html\"><strong>Module ${nnum}: ${MODULE_NAMES[$ni]}</strong>${ntitle}</a>" >> "$MDIR/dashboard.html"
            fi
        done

        cat >> "$MDIR/dashboard.html" << DASH2EOF
            </div>
        </div>
    </div>

    <footer>Active Inference Institute &mdash; Active Inference: Metallurgy — ${CNAME} — Module ${MNUM}: ${MNAME}</footer>

    <script>
    document.querySelectorAll('.concept-card').forEach(function(c){
        c.addEventListener('click',function(){c.classList.toggle('open');});
    });

    var Q=[
        {"q": "In the context of ${MNAME,,}, the Free Energy Principle states that metallurgical systems:", "opts": ["Maximize entropy at all costs", "Minimize free energy through structural and compositional changes", "Remain static unless externally forced", "Violate thermodynamic laws"], "correct": 1, "explain": "The FEP states that persistent systems minimize free energy — in metallurgy this manifests as phase transformations and microstructural evolution driven by thermodynamic free energy minimization."},
        {"q": "A Markov blanket in a metallurgical context can be identified as:", "opts": ["A thermal insulation layer", "The boundary (e.g., grain boundary or phase interface) that separates internal from external states", "A type of rolling mill", "An X-ray diffraction pattern"], "correct": 1, "explain": "The Markov blanket is the statistical boundary mediating interactions between internal and external states — grain boundaries and phase interfaces serve this role in metals."},
        {"q": "Prediction error in a metallurgical system corresponds to:", "opts": ["An instrument calibration mistake", "The deviation between the current non-equilibrium state and the predicted equilibrium state", "A flaw in the alloy's crystal structure", "The cost of raw materials"], "correct": 1, "explain": "Prediction error = departure from equilibrium. When a quenched alloy is far from its predicted equilibrium phases, it has high prediction error, driving subsequent transformations."}
    ];
    var ci=0,ans=new Array(Q.length).fill(null),sc=0;

    function renderQ(){
        var q=Q[ci],done=ans[ci]!==null;
        var h='<p class="qq"><strong>Q'+(ci+1)+'.</strong> '+q.q+'</p>';
        q.opts.forEach(function(o,i){
            var c='qbtn';
            if(done){if(i===q.correct)c+=' correct';else if(i===ans[ci])c+=' wrong';}
            h+='<button class="'+c+'" onclick="pickA('+i+')" '+(done?'disabled':'')+'>'+String.fromCharCode(65+i)+') '+o+'</button>';
        });
        if(done){
            var ok=ans[ci]===q.correct;
            h+='<div class="qexp" style="display:block;background:'+(ok?'#166534':'#7f1d1d')+';">'+(ok?'Correct! ':'Incorrect. ')+q.explain+'</div>';
        }
        document.getElementById('qc').innerHTML=h;
        document.getElementById('qprog').textContent='Question '+(ci+1)+' of '+Q.length;
        document.getElementById('pbtn').disabled=ci===0;
        document.getElementById('nbtn').textContent=ci===Q.length-1?'See Score':'Next \u2192';
    }

    function pickA(i){
        if(ans[ci]!==null)return;
        ans[ci]=i;
        if(i===Q[ci].correct)sc++;
        renderQ();
    }

    function nextQ(){
        if(ci<Q.length-1){ci++;renderQ();}
        else{
            var pct=Math.round(sc/Q.length*100);
            var d=document.getElementById('score-box');
            d.style.display='block';
            d.innerHTML='<h3 style="color:'+(pct>=60?'var(--green)':'var(--red)')+'">'+sc+'/'+Q.length+' ('+pct+'%)</h3><p style="color:var(--muted);margin-top:8px">'+(pct>=80?'Excellent understanding of the material!':pct>=60?'Good foundation. Review the concepts you missed.':'Consider re-reading the module before moving on.')+'</p>';
        }
    }

    function prevQ(){if(ci>0){ci--;renderQ();}}

    var SK='${SK}';
    var QK=SK+'_quiz';
    function initCL(){
        var saved=JSON.parse(localStorage.getItem(SK)||'[]');
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        boxes.forEach(function(cb,i){
            if(saved[i])cb.checked=true;
            if(cb.checked)cb.parentElement.classList.add('done');
            cb.addEventListener('change',function(){
                cb.parentElement.classList.toggle('done',cb.checked);
                saveCL();updProg();
            });
        });
        updProg();
    }
    function saveCL(){
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        localStorage.setItem(SK,JSON.stringify(Array.from(boxes).map(function(c){return c.checked;})));
    }
    function updProg(){
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        var n=boxes.length,done=Array.from(boxes).filter(function(c){return c.checked;}).length;
        document.getElementById('pfill').style.width=(n?done/n*100:0)+'%';
        document.getElementById('ptxt').textContent=done+' of '+n+' complete';
    }

    function saveQuiz(){
        localStorage.setItem(QK,JSON.stringify({ci:ci,ans:ans,sc:sc}));
    }
    function loadQuiz(){
        try{
            var d=JSON.parse(localStorage.getItem(QK));
            if(d&&d.ans&&d.ans.length===Q.length){
                ci=d.ci||0;ans=d.ans;sc=d.sc||0;
            }
        }catch(e){}
    }
    var _origPickA=pickA;
    pickA=function(i){_origPickA(i);saveQuiz();};

    document.addEventListener('DOMContentLoaded',function(){
        document.querySelectorAll('.meter-fill').forEach(function(f){
            var w=f.style.width;f.style.width='0%';
            setTimeout(function(){f.style.width=w;},200);
        });
        loadQuiz();
        renderQ();
        initCL();
    });
    </script>
</body>
</html>
DASH2EOF

        # ── README.md ──
        cat > "$MDIR/README.md" << RMEOF
# Module ${MNUM}: ${MNAME}

> **Quick Navigation**: [Course Home](../README.md) | [Curriculum Home](../../README.md)

## ${MTITLE}

Part of **${CNAME}**.

## Contents

| File | Description |
| --- | --- |
| [module.md](./module.md) | Full lecture (${MTITLE}) |
| [questions.md](./questions.md) | 20 Study Questions |
| [practice_quiz.md](./practice_quiz.md) | Practice Quiz (MC + Short Analysis) |
| [lab.md](./lab.md) | Lab: ${MTITLE} |
| [dashboard.html](./dashboard.html) | Interactive Dashboard |

## Learning Goals

1. **Define** ${MNAME,,} in the Active Inference framework for metallurgical systems
2. **Identify** how ${MNAME,,} manifests in ${CPERSP,,}
3. **Apply** ${MNAME,,} principles to real materials engineering problems

## Resources

- [Notation](../../resources/notation_table.md)
- [Glossary](../../resources/glossary.md)
RMEOF

        # ── AGENTS.md ──
        cat > "$MDIR/AGENTS.md" << AMEOF
# Station: ${MNAME} (${CNAME})

> **Quick Navigation**: [Module README](./README.md) | [Course AGENTS](../AGENTS.md)

## Conventions

- **Perspective**: ${CPERSP}
- **Topics**: ${MNAME} — ${MTITLE}
- **Lab Style**: ${CLAB}
- **Audience**: ${CAUD}
- **Tone**: Technical / engineering-focused

Ensure all content adheres to [../../resources/notation_table.md](../../resources/notation_table.md).
AMEOF

        echo "  Created module: ${CDIR}/${MNUM}_${MODULE_TOPICS[$mi]}"
    done

    echo "Completed course: ${CNAME}"
done

echo ""
echo "=== Generation Complete ==="
echo "All 4 courses × 8 modules × 7 files created."
