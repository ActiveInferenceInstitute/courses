# Practice Quiz: Research Methods

## Part A: Multiple Choice

1. What does Dynamic Causal Modelling (DCM) provide that Granger causality and SEM do not?
A) Correlation-based connectivity measures
B) An explicit neuronal generative model that distinguishes reciprocal connections, modulatory effects, and hidden neuronal states
C) Data-driven clustering of brain regions
D) Machine learning classification of brain states

2. Why is parameter recovery analysis essential for computational phenotyping?
A) It proves that the model is the correct model of the brain
B) It demonstrates that the fitting procedure can reliably recover known parameter values from simulated data, ensuring identifiability
C) It eliminates the need for model comparison
D) It replaces the need for behavioral data

3. In Active Inference, what behavioral measure most directly indexes prediction error (surprise)?
A) Reaction time
B) Pupil dilation
C) Choice accuracy
D) Response vigor

4. How does pymdp differ from RxInfer.jl in its primary use case?
A) pymdp is for continuous control; RxInfer.jl is for discrete decision-making
B) pymdp focuses on discrete POMDP models; RxInfer.jl handles continuous-time message passing on factor graphs
C) pymdp is written in Julia; RxInfer.jl is written in Python
D) They are identical tools with different names

5. What is computational phenotyping?
A) Measuring physical characteristics of patients (height, weight, blood pressure)
B) Fitting Active Inference model parameters to individual behavioral data to characterize each person's unique inference profile
C) Using brain imaging to classify psychiatric diagnoses
D) Performing genetic sequencing to predict behavior

6. What is the primary advantage of pre-registration in computational modeling studies?
A) It guarantees that the study will be published
B) It prevents post-hoc model selection and p-hacking by committing to models and analyses before seeing data
C) It eliminates the need for model comparison
D) It reduces the computational cost of analysis

7. How does Active Inference's built-in epistemic value (information gain) differ from ε-greedy exploration in reinforcement learning?
A) They are mathematically equivalent
B) Active Inference's exploration is principled and directed toward uncertainty reduction, while ε-greedy is random
C) Active Inference never explores; it only exploits
D) ε-greedy provides better exploration than Active Inference in all environments

## Part B: Short Answer

1. Design a behavioral experiment that dissociates epistemic value from pragmatic value. Specify the task structure, manipulations, dependent variables, and the specific predictions that Active Inference makes about behavior in each condition.

2. Describe the 5-step translational pipeline from computational theory to clinical treatment in computational psychiatry. For each step, give a concrete example from the Active Inference literature.

3. How should Active Inference research be communicated to different audiences (neuroscientists, engineers, clinicians, philosophers)? Identify the three most common misunderstandings about Active Inference and explain how to address each.
