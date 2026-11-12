# docs/ — repository documentation hub

> **Navigation**: [Repository README](../README.md) | [Run guide](RUN_GUIDE.md) | [Documentation index](documentation-index.md) | [Generated facts](_generated/README.md)

This directory holds the repository-level documentation: how the gate runs, what
the CI workflow actually checks, and where every long-lived document lives. The
publishing engine's own technical guides stay in [`software/docs/`](../software/docs/README.md);
this hub routes to them rather than copying them.

---

## Quick reference

| Need | Document |
| --- | --- |
| Run one gate arm (lint, types, no-mocks, tests, docs, GNN) | [`RUN_GUIDE.md`](RUN_GUIDE.md) |
| Find any long-lived document | [`documentation-index.md`](documentation-index.md) |
| Current test/module/doc counts | [`_generated/GATE_METRICS.md`](_generated/GATE_METRICS.md) |
| Last measured wall time per arm | [`_generated/ARM_TIMINGS.md`](_generated/ARM_TIMINGS.md) |
| What the GNN conformance job parses | [`../.github/GNN.md`](../.github/GNN.md) |
| Engine install, rendering, publishing | [`../software/docs/README.md`](../software/docs/README.md) |
| Contribution rules and the no-mocks policy | [`../software/docs/CONTRIBUTING.md`](../software/docs/CONTRIBUTING.md) |

**Known gap:** `./run.sh test-full` is red on this host — one failure in the
YouTube playlist enumeration test, then a block on caption download. The offline
arms and `gnn` are green. Details in
[`RUN_GUIDE.md`](RUN_GUIDE.md#known-red-arm--test-full).

---

## Evidence and freshness

Documentation is a view over facts the repository already owns. Use the
narrowest authoritative source for each claim:

| Claim type | Authoritative source | Documentation rule |
| --- | --- | --- |
| Runtime behavior, defaults, precedence | `software/src/`, `publish.toml`, tests | Verify the command or code path; do not infer behavior from an older guide. |
| Test, module, script, and page counts | [`_generated/GATE_METRICS.md`](_generated/GATE_METRICS.md) | Link the generated table; never copy a count into prose that a script can produce. |
| Gate wall times and coverage | [`_generated/ARM_TIMINGS.md`](_generated/ARM_TIMINGS.md) | Report what was measured on the named host; do not generalize it. |
| GNN parser pin | [`.github/gnn-pin.json`](../.github/gnn-pin.json) (`gnn-importer-pin/v1`) | Quote the tag and revision from the pin file, not from memory. |
| CI behavior | [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) | The workflow calls the same `./run.sh` arms documented here; there is no second copy of a check. |
| Publication or release status | Fresh local gate runs and the remote commit | A green local run is not proof of a hosted run. |

`./run.sh docs` enforces the two mechanical parts of this table: relative links
must resolve, and [`_generated/GATE_METRICS.md`](_generated/GATE_METRICS.md) must
match a fresh generation.

---

## Layout

| Path | Purpose |
| --- | --- |
| [`RUN_GUIDE.md`](RUN_GUIDE.md) | The single gate entry point, its arms, and what each arm proves. |
| [`documentation-index.md`](documentation-index.md) | Flat index of every long-lived document in the repository. |
| [`AGENTS.md`](AGENTS.md) | Guidance for agents editing this directory. |
| [`_generated/`](_generated/README.md) | Script-produced facts. Never hand-edited. |
| [`../software/docs/`](../software/docs/README.md) | Engine architecture, CLI reference, testing, publishing. |

---

## Verification

```bash
./run.sh docs      # relative links + generated facts are current
./run.sh metrics   # rewrite docs/_generated/ from the current tree
```
