#!/usr/bin/env bash
# Gate entry point. One arm per command; CI calls these same arms.
#
#   ./run.sh [arm]
#
# Arms: lint, types, no-mocks, test (default), test-full, docs, contract, gnn,
# metrics, all.
# Commands are documented in docs/RUN_GUIDE.md and measured in
# docs/_generated/ARM_TIMINGS.md. Nothing here re-implements a check: `gnn`
# delegates to software/scripts/verify_gnn_conformance.py, `docs` to
# software/scripts/check_docs.py, `contract` to check_education_contract.py plus the
# bundle staleness check, `metrics` to generate_gate_metrics.py.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
SOFTWARE="$ROOT/software"
ARM="${1:-test}"
if [[ $# -gt 0 ]]; then shift; fi

project_python() {
    if [[ -n "${COURSES_PYTHON:-}" ]]; then
        "$COURSES_PYTHON" "$@"
    elif [[ -n "${UV_PYTHON:-}" ]]; then
        uv run --project "$SOFTWARE" --no-sync --python "$UV_PYTHON" python "$@"
    else
        uv run --project "$SOFTWARE" --no-sync python "$@"
    fi
}

gnn_python() {
    local runtime="${COURSES_GNN_PYTHON:-$SOFTWARE/.venv-gnn/bin/python}"
    if [[ ! -x "$runtime" ]]; then
        echo "[run.sh] GNN runtime unavailable; provision it separately and set COURSES_GNN_PYTHON" >&2
        return 2
    fi
    "$runtime" -B "$@"
}

receipt_python() {
    if [[ "$ARM" == "gnn" ]]; then
        gnn_python "$@"
    else
        project_python "$@"
    fi
}


run_arm() {
    local arm="$1"
    shift
    local snapshot="" rc evidence_rc
    echo "[run.sh] arm=$arm" >&2
    if [[ "${GATE_TIMINGS:-1}" != "0" ]] && \
        { [[ "$arm" != "gnn" ]] || [[ -x "${COURSES_GNN_PYTHON:-$SOFTWARE/.venv-gnn/bin/python}" ]]; }; then
        snapshot="$(mktemp "${TMPDIR:-/tmp}/courses-gate.XXXXXX")"
        if ! receipt_python "$SOFTWARE/scripts/gate_receipt.py" start \
            --root "$ROOT" --arm "$arm" --out "$snapshot" -- "$@"; then
            rm -f "$snapshot"
            return 1
        fi
    elif [[ "${GATE_TIMINGS:-1}" != "0" ]]; then
        echo "[run.sh] GNN timing unmeasured: selected parser runtime is unavailable" >&2
    fi
    # Functions below explicitly combine statuses; Bash conditional context must
    # never be relied on for errexit inside a multi-command arm.
    if "$@"; then rc=0; else rc=$?; fi
    if [[ -n "$snapshot" ]]; then
        if receipt_python "$SOFTWARE/scripts/gate_receipt.py" finish \
            --root "$ROOT" --snapshot "$snapshot" --rc "$rc" \
            --log "${GATE_TIMINGS_LOG:-$ROOT/docs/_generated/arm-timings-v2.jsonl}"; then
            evidence_rc=0
        else
            evidence_rc=$?
        fi
        rm -f "$snapshot"
        if [[ $rc -eq 0 && $evidence_rc -ne 0 ]]; then rc=$evidence_rc; fi
    fi
    if [[ $rc -ne 0 ]]; then
        echo "[run.sh] arm=$arm FAILED (exit $rc)" >&2
    fi
    return "$rc"
}

arm_lint() {
    ( cd "$SOFTWARE" && project_python -m ruff check src/ scripts/ "$@" \
        && project_python -m ruff format --check src/ scripts/ "$@" )
}

arm_types() {
    ( cd "$SOFTWARE" && project_python -m mypy src/ "$@" )
}

arm_no_mocks() {
    project_python "$SOFTWARE/scripts/verify_no_mocks.py" "$@"
}

arm_test() {
    ( cd "$SOFTWARE" && project_python -m pytest tests/ \
        -m "not requires_internet and not requires_api and not requires_whisper" \
        --cov-report=xml --cov-report=json "$@" )
}

arm_test_full() {
    ( cd "$SOFTWARE" && project_python -m pytest tests/ "$@" )
}

arm_docs() {
    project_python "$SOFTWARE/scripts/check_docs.py" "$@"
}

arm_contract() {
    # One machine report includes both checker and exporter outcomes. The
    # checker preserves caller-relative paths and runs freshness even on failure.
    project_python "$SOFTWARE/scripts/check_education_contract.py" --check-export "$@"
}

arm_gnn() {
    # Admission mode and independent artifacts are explicit CLI/env inputs.
    # This arm never installs, probes an unqualified package, or changes modes.
    gnn_python "$SOFTWARE/scripts/verify_gnn_conformance.py" "$@"
}

arm_metrics() {
    project_python "$SOFTWARE/scripts/generate_gate_metrics.py" "$@"
}

case "$ARM" in
    lint) run_arm lint arm_lint "$@" ;;
    types) run_arm types arm_types "$@" ;;
    no-mocks) run_arm no-mocks arm_no_mocks "$@" ;;
    test) run_arm test arm_test "$@" ;;
    test-full) run_arm test-full arm_test_full "$@" ;;
    docs) run_arm docs arm_docs "$@" ;;
    contract) run_arm contract arm_contract "$@" ;;
    gnn) run_arm gnn arm_gnn "$@" ;;
    metrics) run_arm metrics arm_metrics "$@" ;;
    all)
        if [[ $# -ne 0 ]]; then
            echo "all does not accept shared arguments; select an arm" >&2
            exit 2
        fi
        for arm in lint types no-mocks test docs contract; do
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
