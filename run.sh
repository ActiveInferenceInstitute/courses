#!/usr/bin/env bash
# Gate entry point. One arm per command; CI calls these same arms.
#
#   ./run.sh [arm]
#
# Arms: lint, types, no-mocks, test (default), test-full, docs, gnn, metrics, all.
# Commands are documented in docs/RUN_GUIDE.md and measured in
# docs/_generated/ARM_TIMINGS.md. Nothing here re-implements a check: `gnn`
# delegates to software/scripts/verify_gnn_conformance.py, `docs` to
# software/scripts/check_docs.py, `metrics` to generate_gate_metrics.py.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
SOFTWARE="$ROOT/software"
ARM="${1:-test}"

now() { python3 -c 'import time; print(f"{time.time():.3f}")'; }

record() { # record <arm> <seconds> <rc>
    # CI sets GATE_TIMINGS=0: a hosted run must not rewrite a tracked receipt.
    [[ "${GATE_TIMINGS:-1}" == "0" ]] && return 0
    local log="$ROOT/docs/_generated/arm-timings.jsonl"
    mkdir -p "$(dirname "$log")"
    printf '{"arm":"%s","seconds":%s,"rc":%s,"at":"%s","host":"%s","commit":"%s"}\n' \
        "$1" "$2" "$3" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$(hostname -s)" \
        "$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)" >>"$log"
}

run_arm() { # run_arm <arm> <command...>
    local arm="$1"
    shift
    echo "[run.sh] arm=$arm"
    local start end rc
    start="$(now)"
    set +e
    "$@"
    rc=$?
    set -e
    end="$(now)"
    record "$arm" "$(python3 -c "print(f'{$end - $start:.3f}')")" "$rc"
    if [[ $rc -ne 0 ]]; then
        echo "[run.sh] arm=$arm FAILED (exit $rc)" >&2
    fi
    return $rc
}

arm_lint() {
    ( cd "$SOFTWARE" && uv run ruff check src/ scripts/ && uv run ruff format --check src/ scripts/ )
}

arm_types() {
    ( cd "$SOFTWARE" && uv run mypy src/ )
}

arm_no_mocks() {
    ( cd "$SOFTWARE" && uv run python scripts/verify_no_mocks.py )
}

arm_test() {
    ( cd "$SOFTWARE" && uv run pytest tests/ \
        -m "not requires_internet and not requires_api and not requires_whisper" \
        --cov-report=xml --cov-report=json )
}

arm_test_full() {
    ( cd "$SOFTWARE" && uv run pytest tests/ )
}

arm_docs() {
    ( cd "$SOFTWARE" && uv run python scripts/check_docs.py )
}

arm_gnn() {
    # The pinned parser is a separate toolchain: its own seeded venv, pinned by
    # .github/gnn-pin.json, installed only when the version does not match.
    local venv="$SOFTWARE/.venv-gnn"
    if [[ ! -x "$venv/bin/python" ]]; then
        uv venv --seed --python 3.12 "$venv" >/dev/null
    fi
    "$venv/bin/python" "$SOFTWARE/scripts/verify_gnn_conformance.py" --install
}

arm_metrics() {
    ( cd "$SOFTWARE" && uv run python scripts/generate_gate_metrics.py )
}

case "$ARM" in
    lint) run_arm lint arm_lint ;;
    types) run_arm types arm_types ;;
    no-mocks) run_arm no-mocks arm_no_mocks ;;
    test) run_arm test arm_test ;;
    test-full) run_arm test-full arm_test_full ;;
    docs) run_arm docs arm_docs ;;
    gnn) run_arm gnn arm_gnn ;;
    metrics) run_arm metrics arm_metrics ;;
    all)
        for arm in lint types no-mocks test docs; do
            "$ROOT/run.sh" "$arm"
        done
        ;;
    help | --help | -h)
        sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'
        ;;
    *)
        echo "unknown arm: $ARM (see ./run.sh help)" >&2
        exit 2
        ;;
esac
