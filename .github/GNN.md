# GNN conformance

| Field | Value |
| --- | --- |
| Workflow | [`.github/workflows/ci.yml`](workflows/ci.yml) |
| Job key | `gnn-conformance` |
| Display name | `gnn conformance (pinned)` |
| Local arm | `./run.sh gnn` |
| Implementation | [`software/scripts/verify_gnn_conformance.py`](../software/scripts/verify_gnn_conformance.py) |
| Pin file | [`.github/gnn-pin.json`](gnn-pin.json) |
| Pin schema | `gnn-importer-pin/v1` |
| Pinned repository | `ActiveInferenceInstitute/Generalized_Notation_Notation` |
| Pinned release | `v5.0.3` |
| Pinned revision | `8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1` |

The job and the local arm run the same script; neither carries its own copy of
the check. The script reads the pin, installs that exact revision into a
dedicated seeded virtual environment (`software/.venv-gnn`, created by
`./run.sh gnn`), and refuses to continue if the installed parser's
`__version__` does not match the pinned tag.

## What it parses

- The five committed exemplars in
  [`course_development/gnn/01_gnn_syntax/models`](../course_development/gnn/01_gnn_syntax/models)
  (`README.md` in that directory is not an exemplar). The count is asserted, so
  adding or removing a sketch without updating the check fails the job.
- Each sketch must parse cleanly (`parse_gnn_formal`, no `parse_errors`) and
  pass `validate_gnn_syntax`.
- The whole exemplar directory must be accepted by `GNNTypeChecker`, writing
  rendered output to a temporary directory that is discarded.

## What it does not do

- It does not scan the rest of the repository for `*.gnn.md`; adding a
  repository-owned model elsewhere does not change the job's scope.
- It does not render framework code or execute models. Parse and type-check
  results do not depend on a renderer being installed.
- It is a pipeline and pin conformance baseline for the exemplar set, not a
  claim that the repository already contains a model.

## Setup actions

The workflow does **not** use the shared composite action
`ActiveInferenceInstitute/.github/.github/actions/setup-python-uv@7159e67315330aac8e414aebae0ad1e999a41448`.
Each job pins `astral-sh/setup-uv` by commit SHA and installs Python through
`uv`; the GNN job needs no `actions/setup-python` step because `uv venv --python
3.12` provisions the interpreter it uses.

## Updating the pin

1. Change `revision`, `tag`, and `recorded` in [`.github/gnn-pin.json`](gnn-pin.json).
2. Run `./run.sh gnn` and confirm it installs the new revision and passes.
3. Run `./run.sh metrics` so `docs/_generated/GATE_METRICS.md` carries the new tag and revision.
4. If the exemplar set changed, update the count assertion in the script and the
   provenance table in the models `README.md`.
