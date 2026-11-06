# Models — agent guidelines

> **Quick Navigation**: [Course](../AGENTS.md) | [Action module](../05_action/AGENTS.md) | [Upstream exemplars](../../../gnn/01_gnn_syntax/models/)

This directory holds repository-owned Generalized Notation Notation (GNN) models for the computer-science course.

## Directory Contents

| Path | Type | Description |
|------|------|-------------|
| `AGENTS.md` | File | This guide |
| `tmaze.gnn.md` | File | Repository-owned GNN expression of the course T-maze fixture |

- `tmaze.gnn.md` is the GNN expression of the T-maze fixture in `../tests/conftest.py::tmaze_model` and the benchmark described in `../05_action/module.md`. The fixture is the source of truth; update the model and fixture together.
- The model is separate from the five verbatim upstream exemplars under `course_development/gnn/01_gnn_syntax/models/`. Do not copy or edit those exemplars here.
- Validate with the pinned GNN v5.0.3 parser at `8f293d9b` using `gnn validate <path> --strict` and the type checker. The repository's `gnn conformance (pinned)` job currently parses only the five exemplars and does not scan this directory; a green job is not evidence that this model was exercised.
- Do not add a habit prior E, learning or policy inference just to make the model look complete; the fixture and course module define the scope.
