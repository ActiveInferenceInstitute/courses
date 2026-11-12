# docs/_generated/ — script-produced facts

Every file here except this one is written by
[`software/scripts/generate_gate_metrics.py`](../../software/scripts/generate_gate_metrics.py).
Do not edit them by hand: a hand edit is overwritten and, until it is, fails
`./run.sh docs`.

| File | Producer | Refresh |
| --- | --- | --- |
| `GATE_METRICS.md` | `generate_gate_metrics.py` | `./run.sh metrics` |
| `ARM_TIMINGS.md` | `generate_gate_metrics.py` from `arm-timings.jsonl` | `./run.sh metrics` |
| `arm-timings.jsonl` | `./run.sh` (one line per arm run, `CI` unset) | running any arm |

`GATE_METRICS.md` is deterministic for a given tree, so `./run.sh docs` compares
it byte-for-byte with a fresh generation and fails when a count has drifted.

One caveat: the tracked-Markdown count reads the Git index, so stage new
documentation (`git add`) before running `./run.sh metrics`, or the count will
be regenerated again on the next commit.

`ARM_TIMINGS.md` is a record of measurements, not a contract: each row names the
host, commit, and exit code it came from, and a missing arm is reported as
`not measured` rather than guessed.
