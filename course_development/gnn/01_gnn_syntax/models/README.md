# GNN Exemplar Models

> **Quick Navigation**: [Lesson](./../module.md) | [Track Home](../../README.md) | [Agent Guidelines](./../AGENTS.md)

Five runnable GNN specifications, copied unmodified from the
Generalized Notation Notation (GNN) exemplar corpus, mapped to course levels.
Each file is a real generative-model spec that the GNN pipeline can parse,
type-check, render, and execute.

---

## Provenance

| Field | Value |
|-------|-------|
| Source repository | [ActiveInferenceInstitute/Generalized_Notation_Notation](https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation) |
| Release | v5.1.0 |
| Commit | `75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf` |
| Source folder | `input/gnn_files/` |
| License | [CC BY-NC-SA 4.0](https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation/blob/75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf/LICENSE.md) |

These copies are verbatim: no edits, no parameter changes. All five are
byte-identical at the earlier v5.0.3 commit `8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`
and at the v5.1.0 commit above (checked 2026-11-16). Verify a copy with:

```bash
# From a GNN checkout at the pinned commit:
git -C <gnn-checkout> show 75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf:input/gnn_files/basics/static_perception.md \
  | diff - models/static_perception.md
```

---

## The five exemplars

| File | Source path | Course level | Concept introduced |
|------|-------------|--------------|--------------------|
| `static_perception.md` | `basics/static_perception.md` | Middle school / High school | Perception as inference over a likelihood matrix `A` |
| `dynamic_perception.md` | `basics/dynamic_perception.md` | High school / College 101 | Belief updating over time with transition matrix `B` |
| `simple_mdp.md` | `discrete/simple_mdp.md` | College 101 | Action selection in a minimal Markov decision process |
| `actinf_pomdp_agent.md` | `discrete/actinf_pomdp_agent.md` | Core curriculum | Canonical full Active Inference agent (A–E matrices) |
| `dirichlet_likelihood_learning.md` | `learning/dirichlet_likelihood_learning.md` | Advanced 401 | Parameter learning with Dirichlet concentration updates |

The GNN corpus ships additional families (continuous-state, hierarchical,
multi-agent, precision, and scaling models). This set stays deliberately small:
it covers one model per course level and every file is an accepted exemplar from
the source repository.

---

## Running the exemplars

Use a GNN checkout at the [pinned revision](https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation/tree/75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf). From the GNN checkout root, install the pinned dependencies and set `MODELS` to the absolute path of the courses model directory.

```bash
uv sync --frozen --python 3.14
MODELS=/absolute/path/to/courses/course_development/gnn/01_gnn_syntax/models
uv run --frozen --no-sync python src/gnn/main.py --target-dir "$MODELS" --only-steps "3,5,11,12"
```

Step 3 parses the specs, Step 5 type-checks them, Step 11 renders framework
code, and Step 12 executes what the local toolchain supports. Render and execute
results depend on the frameworks installed in the GNN environment; parse and
type-check results do not require any renderer.

The repository's `gnn conformance (pinned)` CI job runs steps 3 and 5 over this
folder with the revision in [`.github/gnn-pin.json`](../../../../.github/gnn-pin.json).

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
