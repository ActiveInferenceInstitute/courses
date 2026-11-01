# Lab: Reading and Running a GNN Specification

> **Learning Goal:** Read a real GNN exemplar section by section, compute the perception update it describes, and run the GNN pipeline over the shipped models.

## Part 1: Read the Exemplar

> **Learning Goal:** Identify each section of a GNN file and what it declares.

Open [`models/static_perception.md`](./models/static_perception.md). For each section listed below, write the value the exemplar gives:

| Section | Value in the exemplar |
|---------|-----------------------|
| `ModelName` | {fill:textarea rows=1} |
| `StateSpaceBlock` — dimensions and type of `A` | {fill:textarea rows=1} |
| `StateSpaceBlock` — dimensions and type of `D` | {fill:textarea rows=1} |
| `Connections` — which variables point into `o` | {fill:textarea rows=1} |
| `Time` | {fill:textarea rows=1} |
| `ActInfOntologyAnnotation` — what `A` means | {fill:textarea rows=1} |
| `ModelParameters` — `num_hidden_states`, `num_obs` | {fill:textarea rows=1} |

Then answer: which two sections separate *declaration* from *value*, and why is that separation useful when comparing two models?

{fill:textarea}

## Part 2: Run the Pipeline

> **Learning Goal:** Observe the parse, type-check, render, and execute steps on a real specification.

You need a GNN checkout. From the GNN repository root:

```bash
# Parse and type-check the shipped exemplars (steps 3 and 5)
python src/gnn/main.py --target-dir <path-to-this-folder>/models --only-steps "3,5"

# Add rendering and execution (steps 11 and 12)
python src/gnn/main.py --target-dir <path-to-this-folder>/models --only-steps "3,5,11,12"
```

Record what the run reports for each step. Note especially which steps succeed for all five models and which frameworks report `unsupported` for a model.

| Step | What it reported | Which models were affected |
|------|------------------|----------------------------|
| 3 — parse | {fill:textarea rows=1} | {fill:textarea rows=1} |
| 5 — type check | {fill:textarea rows=1} | {fill:textarea rows=1} |
| 11 — render | {fill:textarea rows=1} | {fill:textarea rows=1} |
| 12 — execute | {fill:textarea rows=1} | {fill:textarea rows=1} |

Why can steps 3 and 5 run on any machine, while steps 11 and 12 depend on the environment?

{fill:textarea}

## Part 3: Compute the Perception Update

> **Learning Goal:** Apply the exemplar's equation to a sequence of observations.

The exemplar declares `A = {(0.9, 0.2), (0.1, 0.8)}` and `D = (0.5, 0.5)`. The update is:

```text
q(s) = D[s] · A[o,s] / Σ_j D[j] · A[o,j]
```

1. Compute `q(s)` for `o = 0`. Show numerator, denominator, and the two posterior values.
2. Compute `q(s)` for `o = 1`. Show the same steps.
3. Compare: how much more confident is the agent after `o = 0` than after `o = 1`? Explain the asymmetry in terms of the matrix values.

You can check your arithmetic with a calculator or a short Python session — the numbers must match the equation, not the other way around.

{fill:textarea}

## Part 4: Follow the Model Up the Levels

> **Learning Goal:** See how each curriculum level adds one new idea to the same notation.

Pick the exemplar for your level from the table in [`module.md`](./module.md#5-which-model-for-which-course-level) and open it.

| Level | File | New sections or variables compared with `static_perception.md` |
|-------|------|----------------------------------------------------------------|
| Dynamic perception | `dynamic_perception.md` | {fill:textarea rows=1} |
| Simple MDP | `simple_mdp.md` | {fill:textarea rows=1} |
| Full POMDP agent | `actinf_pomdp_agent.md` | {fill:textarea rows=1} |
| Parameter learning | `dirichlet_likelihood_learning.md` | {fill:textarea rows=1} |

What is the smallest change that turns the static model into a model that *acts*?

{fill:textarea}

## Part 5: Reflection

In 150 words, reflect: how does reading the model as text change your understanding compared with reading only its equations or only its code?

{fill:textarea}

## Lab Summary

| Part | Skill Practiced | Key Concept |
|------|----------------|-------------|
| 1 | Reading GNN sections | Declaration vs. value, ontology annotation |
| 2 | Running the pipeline | Parse, type-check, render, execute |
| 3 | Hand computation | Bayes' rule as a likelihood update |
| 4 | Model comparison | One new idea per level |
| 5 | Reflection | Notation as a shared language |
