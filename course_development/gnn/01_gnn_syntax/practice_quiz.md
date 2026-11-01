# Practice Quiz: GNN Syntax

**Name**: _________________ **Date**: _________________

## Part A: Multiple Choice

**1.** A GNN file is best described as:
A) A Python module with model classes
B) A plain-text specification of a generative model organized into named sections
C) A graphical diagram format
D) A database schema for storing simulations

**2.** The "triple play" of GNN refers to moving one model specification between:
A) Three programming languages
B) Plain text, graphical, and executable computational forms
C) Three levels of mathematics
D) Local, server, and cloud execution

**3.** In the state space block, `A[2,2,type=float]` declares:
A) Two observations and two hidden states with floating-point entries
B) A matrix of size 2 with integer entries
C) Two actions and two policies
D) The number of time steps

**4.** In the Static Perception Model, the convention `A[o,s] = P(o | s)` means:
A) Rows are hidden states and columns are observations
B) Rows are observations and columns are hidden states
C) The matrix is symmetric
D) `A` is the posterior `Q(s | o)`

**5.** With `D = (0.5, 0.5)` and the exemplar's `A = {(0.9, 0.2), (0.1, 0.8)}`, the posterior after observing `o = 0` is approximately:
A) `(0.5, 0.5)`
B) `(0.9, 0.1)`
C) `(0.818, 0.182)`
D) `(0.111, 0.889)`

**6.** The `ActInfOntologyAnnotation` section exists so that:
A) The pipeline can skip type checking
B) A symbol and its meaning are declared separately, allowing different interpretations and languages
C) Matrices can be stored as integers
D) The model runs faster

**7.** Which pipeline steps parse and type-check a specification without requiring a simulation framework?
A) Steps 11 and 12
B) Steps 3 and 5
C) Steps 1 and 2
D) Steps 23 and 24

## Part B: Short Answer

**1.** Explain, in your own words, why GNN's authors describe the notation as an *interlingua* for Active Inference. What problem does that solve for a research community that uses several software frameworks?

**2.** Take the Static Perception Model's transition tensor `B` and the uniform prior `D = (0.5, 0.5)`. For action 0, compute the predicted next-state belief `q_next = B[:,:,0] · q`. Show the multiplication and state the result.

**3.** A classmate edits a GNN file to change `A[2,2,type=float]` to `A[3,2,type=float]` but leaves the initial parameterization at the 2×2 values. Predict what happens at each of steps 3, 5, and 11, and explain why the pipeline separates these checks.
