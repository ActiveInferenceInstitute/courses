# GNN conformance

`gnn conformance (pinned)` is defined in `.github/workflows/ci.yml` and reads
`.github/gnn-pin.json`, which pins
`ActiveInferenceInstitute/Generalized_Notation_Notation` at `v5.0.3`
(`8f293d9ba810e6eda5c09842d9c7ed9ffa5f92c1`).

The job verifies the pin and installed parser, parses the five committed
exemplars under `course_development/gnn/01_gnn_syntax/models`, and type-checks
that directory. It does not scan the rest of the repository for `*.gnn.md`;
adding a repository-owned model elsewhere does not change the job's scope.
This is a pipeline and pin conformance baseline for the exemplar set, not a
claim that the repository already contains a model.
