# GNN Syntax Track

> **Quick Navigation**: [Curriculum Home](../README.md) | [Course Development AGENTS](../AGENTS.md) | [Lesson](./01_gnn_syntax/README.md)

A supplementary skills track for the Active Inference Institute curriculum:
reading, writing, and running **Generalized Notation Notation (GNN)**
specifications of generative models.

---

## Why this track exists

The fourteen curriculum courses teach Active Inference as theory, practice, and
domain application. This track adds the *specification layer*: a plain-text
notation in which a generative model is declared once and then checked,
rendered, and executed by the GNN processing pipeline.

GNN was introduced by Smékal and Friedman (2023) as an interlingua for Active
Inference — a notation that "bridges and respects gaps among different modeling
approaches" so that models can be compared and reused across frameworks. The
Institute's Active InferAnt Stream episodes
[014.1](https://www.youtube.com/watch?v=3tYOBVIOLyU) and
[014.2](https://www.youtube.com/watch?v=Y3-FMoaEZYE) document the project's
development, including the "triple play" of text, graph, and executable forms.

> **This track is not one of the fourteen 8-topic spiral courses.** It is not
> included in the 464-module count and does not follow the 8-topic unit
> structure. It is a supporting track, like the YouTube transcript archive.

---

## Contents

| Path | Description |
|------|-------------|
| [`01_gnn_syntax/`](./01_gnn_syntax/) | Lesson: reading a real GNN exemplar section by section, computing its perception update, and running the pipeline |
| [`01_gnn_syntax/models/`](./01_gnn_syntax/models/README.md) | Five verbatim GNN exemplars (GNN v5.0.3) mapped to course levels |

---

## Exemplar mapping

| Level | Exemplar | Concept introduced |
|-------|----------|--------------------|
| Elementary / Family | *(none shipped)* | Story and movement levels do not introduce a text notation |
| Middle school (guided) | `static_perception.md` | Perception as inference over a likelihood |
| High school | `dynamic_perception.md` | Belief updating over time |
| College 101 | `simple_mdp.md` | Action selection |
| Core curriculum | `actinf_pomdp_agent.md` | Canonical full Active Inference agent |
| Advanced 401 | `dirichlet_likelihood_learning.md` | Parameter learning |

---

## Running the pipeline over the exemplars

From a checkout of the GNN repository at the pinned revision:

```bash
python src/gnn/main.py --target-dir course_development/gnn/01_gnn_syntax/models --only-steps "3,5,11,12"
```

Steps 3 (parse) and 5 (type check) need no simulator; steps 11 (render) and 12
(execute) report `unsupported` for frameworks that cannot represent a given
model, and `skipped` when a toolchain is missing locally.

The repository's `gnn conformance (pinned)` CI job runs the same parser and type
checker over the five exemplars. It installs the revision recorded in
[`.github/gnn-pin.json`](../../.github/gnn-pin.json) (GNN `v5.0.3`) and fails if
an exemplar stops parsing or type-checking.

---

## Publishing

The track is registered in `COURSE_REGISTRY` (ID `gnn`) and enabled in
`publish.toml`, so the standard pipeline renders it like any other content tree:

```bash
cd software && uv run python scripts/generate_all_outputs.py --course gnn --formats txt,md
```

---

## References

- Smékal, J., & Friedman, D. A. (2023). *Generalized Notation Notation for
  Active Inference Models.* Zenodo. <https://zenodo.org/records/7803328>
- Active Inference Institute. *Generalized_Notation_Notation* repository.
  <https://github.com/ActiveInferenceInstitute/Generalized_Notation_Notation>
- Transcripts: [Episode 014.1](../youtube/active-inferant-stream/17_active-inferant-stream-014-1-generalized-notation-notation/module.md),
  [Episode 014.2](../youtube/active-inferant-stream/18_active-inferant-stream-014-2-generalized-notation-notation/module.md)

---

> *"Minimize surprise. Maximize evidence."* — Active Inference Institute
