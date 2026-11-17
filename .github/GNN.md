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
| Pinned release | `v5.1.0` |
| Pinned revision | `75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf` |

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
- Source-mode results are parsing/syntax/type evidence, not scientific execution
  or installed-origin qualification. Earlier v5.0.3 passes remain historical,
  not v5.1.0 acceptance. Genuine installed-positive and foreign-origin runtimes
  were unavailable; those two integration cases remain explicitly unqualified.
- Frozen bootstrap `f638d4c0…` has a disclosed malformed non-GitHub installed-origin
  URL-normalization limitation. This integration makes no installed-origin/VCS
  qualification claim; source mode never claims VCS verification. Any replacement
  bootstrap needs separately qualified producer delivery and consumer adoption.

## Setup actions

The workflow does **not** use the shared composite action
`ActiveInferenceInstitute/.github/.github/actions/setup-python-uv@7159e67315330aac8e414aebae0ad1e999a41448`.
The GNN job selects the exact source artifact and provisions dependencies outside
the gate. It downloads the independently reviewed bootstrap and v5.1.0 manifest
from immutable resource-delivery commit
`66d491f86895443cf588011cc6f40c37b8bae8fd`; the verifier enforces bootstrap
`f638d4c0…` and the complete 1,232-file manifest `43b33c0b…`. This resource commit
is not the parser pin, which stays at upstream's
`75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf`. No repository URL variables or
fallback selectors are needed. A local source-mode pass does not certify the
hosted job.

## Updating the pin

Pin migration is an owner decision, not a way to make a failing check green.
It requires a matching independently reviewed bootstrap/manifest, compatible
prepared runtime and actual affected consumer proof. Do not change the pin or
rewrite generated metrics merely to align releases across the estate.
