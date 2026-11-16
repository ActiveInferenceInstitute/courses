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

The job and local arm use the same non-mutating verifier. Select an already
prepared `COURSES_GNN_PYTHON` and explicit `COURSES_GNN_MODE=source|installed`.
Both modes require independent frozen bootstrap and complete manifest bytes via
`COURSES_GNN_BOOTSTRAP` and `COURSES_GNN_MANIFEST`. Source mode additionally
requires `COURSES_GNN_PACKAGE_ROOT` and `PYTHONPATH` resolving that exact source.
Installed mode requires genuine matching PEP 610 Git origin plus full content;
it never falls back to source mode. Neither the gate nor its controls install GNN.

The bootstrap digest is checked before executing those exact bytes. All parser
imports and verdicts stay inside the source guard. Receipts remain provisional
until the post-execution guard succeeds; prior imports, foreign roots and
changed/missing/extra package files are rejected.

## What it parses

- The five committed exemplars in
  [`course_development/gnn/01_gnn_syntax/models`](../course_development/gnn/01_gnn_syntax/models)
  (`README.md` in that directory is not an exemplar). The count is asserted, so
  adding or removing a sketch without updating the check fails the job.
- Each sketch is passed by filesystem path to `parse_gnn_formal`, must have no
  parse errors, and must pass `validate_gnn_syntax`.
- The real serial type checker runs inside the same guard and must return
  literal `True`; warning value `2` is not success.

## What it does not do

- It does not scan the rest of the repository for `*.gnn.md`; adding a
  repository-owned model elsewhere does not change the job's scope.
- It does not render framework code or execute models. Parse and type-check
  results do not depend on a renderer being installed.
- The five-exemplar gate passed in explicit source mode at the unchanged pin.
  This is parsing/syntax/type evidence, not scientific execution or an
  installed-origin qualification. Genuine installed-positive and foreign-origin
  runtimes were unavailable; those two integration cases remain explicitly skipped.

## Setup actions

The workflow does **not** use the shared composite action
`ActiveInferenceInstitute/.github/.github/actions/setup-python-uv@7159e67315330aac8e414aebae0ad1e999a41448`.
The GNN job selects the exact source artifact and provisions dependencies outside
the gate. `COURSES_GNN_BOOTSTRAP_URL` and `COURSES_GNN_MANIFEST_URL` must point to
the reviewed frozen artifacts; publication and repository-variable setup remain
unqualified. A local source-mode pass does not certify the hosted job.

## Updating the pin

Pin migration is an owner decision, not a way to make a failing check green.
It requires a matching independently reviewed bootstrap/manifest, compatible
prepared runtime and actual affected consumer proof. Do not change the pin or
rewrite generated metrics merely to align releases across the estate.
