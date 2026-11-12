# docs/ — agent guidance

Repository-level documentation. The publishing engine's technical guides live in
[`../software/docs/`](../software/docs/README.md); this directory documents the
gate, the CI workflow, and the documentation map.

## Rules

- **Generated files are not hand-edited.** `_generated/GATE_METRICS.md` and
  `_generated/ARM_TIMINGS.md` come from `software/scripts/generate_gate_metrics.py`.
  Change the producer, then run `./run.sh metrics`.
- **No hand-copied counts.** Test, module, script, page, and timing numbers are
  linked from `_generated/`, never retyped into prose.
- **One gate entry point.** `./run.sh <arm>` is the documented way to run a
  check, and `.github/workflows/ci.yml` calls the same arms. Do not add a second
  copy of a command to a guide or a workflow.
- **Relative links only** for in-repository targets; `./run.sh docs` resolves
  every one of them against the filesystem.

## Adding a document

1. Write it under this directory (or the owning subsystem's docs directory).
2. Add it to [`documentation-index.md`](documentation-index.md).
3. Add it to the relevant table in [`README.md`](README.md) if it is a hub-level
   entry point.
4. Run `./run.sh docs`.

## Related

- [Root operating contract](../AGENTS.md)
- [Run guide](RUN_GUIDE.md)
- [Documentation index](documentation-index.md)
