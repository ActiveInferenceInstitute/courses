"""Real-file GNN admission/verdict regressions; no replacement GNN modules.

Set COURSES_GNN_BOOTSTRAP, COURSES_GNN_MANIFEST and COURSES_GNN_PACKAGE_ROOT
to the independently reviewed artifacts. COURSES_GNN_PYTHON selects an already
provisioned parser runtime. CI sets COURSES_GNN_TEST_REQUIRED=1 so absent
artifacts fail instead of skipping the integration cases.

The optional installed-origin cases require separately provisioned genuine
installations: COURSES_GNN_INSTALLED_PYTHON and COURSES_GNN_FOREIGN_PYTHON.
Both must resolve the full manifest-matching package. The foreign fixture must
have genuine mismatching Git-origin metadata, so origin rejection is tested
independently of content rejection.
Neither this suite nor the consumer creates distribution/VCS metadata or
installs anything. A skipped installed case is not installed-mode evidence.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
from scripts import verify_gnn_conformance as conformance

SOFTWARE = conformance.ROOT / "software"
SCRIPT = SOFTWARE / "scripts" / "verify_gnn_conformance.py"
TMAZE = (
    conformance.ROOT
    / "course_development/active_inference/04_computer_science/models/tmaze.gnn.md"
)


def _environment(tmp_path: Path) -> dict[str, str]:
    env = {
        key: value for key, value in os.environ.items()
        if not key.startswith("COURSES_GNN_")
    }
    env.update(
        PYTHONPATH=str(SOFTWARE),
        PYTHONNOUSERSITE="1",
        PYTHONDONTWRITEBYTECODE="1",
        GATE_TIMINGS="0",
        MPLCONFIGDIR=str(tmp_path / "matplotlib"),
        XDG_CACHE_HOME=str(tmp_path / "cache"),
        TMPDIR=str(tmp_path),
    )
    return env


@pytest.fixture(scope="module")
def artifacts() -> dict[str, Path]:
    names = {
        "bootstrap": "COURSES_GNN_BOOTSTRAP",
        "manifest": "COURSES_GNN_MANIFEST",
        "package": "COURSES_GNN_PACKAGE_ROOT",
    }
    values = {key: os.environ.get(name) for key, name in names.items()}
    missing = [names[key] for key, value in values.items() if not value]
    if missing:
        message = "Real GNN qualification artifacts required: " + ", ".join(missing)
        if any(values.values()) or os.environ.get("COURSES_GNN_TEST_REQUIRED") == "1":
            pytest.fail(message)
        pytest.skip(message + "; source qualification was not exercised")
    return {key: Path(value).resolve(strict=True) for key, value in values.items()}


@pytest.fixture
def source_env(tmp_path: Path, artifacts: dict[str, Path]) -> dict[str, str]:
    # Every writable package is a test-owned copy of the complete admitted tree.
    package = tmp_path / "source" / "gnn"
    shutil.copytree(artifacts["package"], package)
    env = _environment(tmp_path)
    env.update(
        COURSES_GNN_MODE="source",
        COURSES_GNN_BOOTSTRAP=str(artifacts["bootstrap"]),
        COURSES_GNN_MANIFEST=str(artifacts["manifest"]),
        COURSES_GNN_PACKAGE_ROOT=str(package),
        PYTHONPATH=os.pathsep.join((str(SOFTWARE), str(package.parent))),
        TMAZE=str(TMAZE),
    )
    return env


@pytest.fixture
def valid_models(tmp_path: Path) -> Path:
    """Exercise five files without changing or inventing scientific content."""
    models = tmp_path / "models"
    models.mkdir()
    for index in range(conformance.EXPECTED_EXEMPLARS):
        shutil.copyfile(TMAZE, models / f"model-{index}.md")
    return models


def _probe(
    body: str,
    env: dict[str, str],
    tmp_path: Path,
    *,
    python: str | None = None,
) -> subprocess.CompletedProcess[str]:
    # Each case gets a real fresh interpreter; no sys.modules eviction/reuse.
    prefix = """
import json
import os
import sys
from contextlib import redirect_stdout
from pathlib import Path
from scripts import verify_gnn_conformance as c

kwargs = {
    "mode": os.environ["COURSES_GNN_MODE"],
    "bootstrap_path": Path(os.environ["COURSES_GNN_BOOTSTRAP"]),
    "manifest_path": Path(os.environ["COURSES_GNN_MANIFEST"]),
    "package_root": (
        Path(os.environ["COURSES_GNN_PACKAGE_ROOT"])
        if os.environ.get("COURSES_GNN_PACKAGE_ROOT") else None
    ),
}
receipt = None
try:
    with redirect_stdout(sys.stderr):
"""
    suffix = """
except Exception as exc:
    print(json.dumps({
        "error": str(exc),
        "error_type": type(exc).__name__,
        "gnn_imported": any(
            name == "gnn" or name.startswith("gnn.") for name in sys.modules
        ),
        "source_status": receipt["status"] if receipt is not None else None,
        "imports_verified": receipt["imports_verified"] if receipt is not None else False,
    }))
    sys.exit(1)
else:
    print(json.dumps(result))
"""
    code = prefix + textwrap.indent(textwrap.dedent(body), "        ") + suffix
    return subprocess.run(
        [python or os.environ.get("COURSES_GNN_PYTHON", sys.executable), "-B", "-c", code],
        env=env,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )


def _failure(result: subprocess.CompletedProcess[str], code: str) -> dict:
    assert result.returncode == 1, (result.stdout, result.stderr)
    payload = json.loads(result.stdout)
    assert code in payload["error"], (payload, result.stderr)
    assert "result" not in payload
    return payload


def test_bootstrap_digest_precedes_execution(tmp_path: Path) -> None:
    marker = tmp_path / "untrusted-code-executed"
    bootstrap = tmp_path / "bootstrap.py"
    bootstrap.write_text(
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('executed')\n",
        encoding="utf-8",
    )
    with pytest.raises(conformance.ConformanceError, match="bootstrap SHA-256"):
        with conformance.qualified_runtime(
            mode="source",
            bootstrap_path=bootstrap,
            manifest_path=tmp_path / "not-read.json",
            package_root=tmp_path / "gnn",
        ):
            pytest.fail("Unreviewed bootstrap was admitted")
    assert not marker.exists()


@pytest.mark.parametrize("arguments", [[], ["--install"]])
def test_cli_requires_explicit_admission_without_install(
    tmp_path: Path, arguments: list[str]
) -> None:
    result = subprocess.run(
        [sys.executable, "-B", str(SCRIPT), *arguments],
        env=_environment(tmp_path),
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 2
    assert result.stdout == ""
    assert "required" in result.stderr or "unrecognized arguments" in result.stderr


def test_gate_forwards_admission_failure_without_installing(tmp_path: Path) -> None:
    bootstrap = tmp_path / "unreviewed.py"
    bootstrap.write_bytes(b"raise RuntimeError('must not execute')\n")
    env = _environment(tmp_path)
    env["COURSES_GNN_PYTHON"] = sys.executable
    result = subprocess.run(
        [
            "bash", str(conformance.ROOT / "run.sh"), "gnn",
            "--mode", "source", "--bootstrap", str(bootstrap),
            "--manifest", str(tmp_path / "absent.json"),
            "--package-root", str(tmp_path / "gnn"),
        ],
        env=env,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert "bootstrap SHA-256" in result.stderr


def test_real_parser_receipt_is_provisional_until_guard_exit(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            assert receipt["ok"] is False
            assert receipt["imports_verified"] is False
            from gnn.parsers.basic import parse_gnn_formal, validate_gnn_syntax
            content = Path(os.environ["TMAZE"]).read_text(encoding="utf-8")
            parsed = parse_gnn_formal(Path(os.environ["TMAZE"]))
            assert parsed is not None and not parsed.parse_errors
            valid, errors = validate_gnn_syntax(content, is_content=True)
            assert valid is True, errors
            assert receipt["imports_verified"] is False
        result = receipt
        """,
        source_env, tmp_path,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)
    receipt = json.loads(result.stdout)
    assert receipt["status"] == "qualified"
    assert receipt["ok"] is True
    assert receipt["imports_verified"] is True
    assert receipt["execution_verified"] is False
    assert receipt["origin"]["kind"] == "explicit-source"
    assert receipt["origin"]["vcs_verified"] is False
    assert receipt["commit"] == conformance.EXPECTED_REVISION
    assert "gnn.parsers.basic" in receipt["loaded_modules"]


def test_real_verdicts_remain_inside_the_checked_source_lifetime(
    source_env: dict[str, str], valid_models: Path, tmp_path: Path
) -> None:
    env = {**source_env, "MODELS": str(valid_models), "GNN_FILE_WORKERS": "4"}
    result = _probe(
        'result = c.verify(**kwargs, models_dir=Path(os.environ["MODELS"]))\n',
        env, tmp_path,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)
    payload = json.loads(result.stdout)
    assert payload["result"] == "verified"
    assert payload["parsed"] == payload["type-checked"] == 5
    assert payload["source"]["status"] == "qualified"
    assert payload["source"]["imports_verified"] is True
    assert "gnn.type_checker.checking.core" in payload["source"]["loaded_modules"]
    assert "gnn.schema_validator.validator" in payload["source"]["loaded_modules"]
    assert payload["source"]["manifest_sha256"] == conformance.MANIFEST_SHA256


@pytest.mark.parametrize("change", ["changed", "extra", "missing"])
def test_same_version_package_requires_complete_content(
    source_env: dict[str, str], tmp_path: Path, change: str
) -> None:
    package = Path(source_env["COURSES_GNN_PACKAGE_ROOT"])
    if change == "changed":
        with (package / "README.md").open("ab") as stream:
            stream.write(b"\nForeign package content.\n")
    elif change == "missing":
        (package / "README.md").unlink()
    else:
        (package / "foreign.txt").write_text("undeclared", encoding="utf-8")
    # __init__.py and its actual v5.0.3 version are untouched.
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        source_env, tmp_path,
    )
    payload = _failure(result, "source-content-mismatch")
    assert payload["gnn_imported"] is False


def test_target_cannot_supply_its_own_expected_manifest(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    package = Path(source_env["COURSES_GNN_PACKAGE_ROOT"])
    changed = package / "README.md"
    changed.write_bytes(changed.read_bytes() + b"\nForeign content.\n")
    manifest = json.loads(Path(source_env["COURSES_GNN_MANIFEST"]).read_bytes())
    manifest["files"]["src/gnn/README.md"] = hashlib.sha256(changed.read_bytes()).hexdigest()
    self_attested = tmp_path / "self-attested.json"
    self_attested.write_text(json.dumps(manifest), encoding="utf-8")
    env = {**source_env, "COURSES_GNN_MANIFEST": str(self_attested)}
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        env, tmp_path,
    )
    payload = _failure(result, "manifest SHA-256")
    assert payload["gnn_imported"] is False


def test_explicit_root_cannot_be_replaced_by_same_version_sibling(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    selected = tmp_path / "different-source" / "gnn"
    shutil.copytree(Path(source_env["COURSES_GNN_PACKAGE_ROOT"]), selected)
    env = {
        **source_env,
        "PYTHONPATH": os.pathsep.join((str(SOFTWARE), str(selected.parent))),
    }
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        env, tmp_path,
    )
    payload = _failure(result, "source-origin-mismatch")
    assert payload["gnn_imported"] is False


def test_installed_mode_never_falls_back_to_source_artifact(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        {**source_env, "COURSES_GNN_MODE": "installed"}, tmp_path,
    )
    payload = _failure(result, "source-origin-")
    assert payload["gnn_imported"] is False


def test_real_invalid_spec_does_not_publish_success(
    source_env: dict[str, str], valid_models: Path, tmp_path: Path
) -> None:
    (valid_models / "model-0.md").write_text("# Not a GNN specification\n", encoding="utf-8")
    result = _probe(
        'result = c.verify(**kwargs, models_dir=Path(os.environ["MODELS"]))\n',
        {**source_env, "MODELS": str(valid_models)}, tmp_path,
    )
    payload = _failure(result, "GNN")
    assert payload["error_type"] == "ConformanceError"
    assert payload["gnn_imported"] is True


def test_real_typechecker_warning_two_is_not_true(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    empty = tmp_path / "no-models"
    empty.mkdir()
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            c._typecheck(Path(os.environ["MODELS"]))
        result = {"result": "verified", "source": receipt}
        """,
        {**source_env, "MODELS": str(empty)}, tmp_path,
    )
    payload = _failure(result, "GNN type checker did not succeed: 2")
    assert payload["source_status"] == "failed"
    assert payload["imports_verified"] is False


def test_package_change_after_real_verdict_invalidates_guard_exit(
    source_env: dict[str, str], valid_models: Path, tmp_path: Path
) -> None:
    result = _probe(
        """
        with c.qualified_runtime(**kwargs) as receipt:
            from gnn.parsers.basic import validate_gnn_syntax
            valid, errors = validate_gnn_syntax(Path(os.environ["TMAZE"]))
            assert valid is True, errors
            c._typecheck(Path(os.environ["MODELS"]))
            changed = kwargs["package_root"] / "README.md"
            with changed.open("ab") as stream:
                stream.write(b"\\nChanged after verdict.\\n")
        result = {"result": "verified", "source": receipt}
        """,
        {**source_env, "MODELS": str(valid_models)}, tmp_path,
    )
    payload = _failure(result, "source-content-mismatch")
    assert payload["source_status"] == "failed"
    assert payload["imports_verified"] is False


def test_previously_qualified_imports_cannot_be_reused(
    source_env: dict[str, str], tmp_path: Path
) -> None:
    result = _probe(
        """
        with c.qualified_runtime(**kwargs):
            from gnn.parsers.basic import validate_gnn_syntax
            valid, errors = validate_gnn_syntax(Path(os.environ["TMAZE"]))
            assert valid is True, errors
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        source_env, tmp_path,
    )
    payload = _failure(result, "source-already-imported")
    assert payload["gnn_imported"] is True


def test_actual_installed_origin_and_content(
    artifacts: dict[str, Path], valid_models: Path, tmp_path: Path
) -> None:
    python = os.environ.get("COURSES_GNN_INSTALLED_PYTHON")
    if not python:
        pytest.skip("No independently provisioned installed runtime; not installed evidence")
    env = _environment(tmp_path)
    env.update(
        COURSES_GNN_MODE="installed",
        COURSES_GNN_BOOTSTRAP=str(artifacts["bootstrap"]),
        COURSES_GNN_MANIFEST=str(artifacts["manifest"]),
        MODELS=str(valid_models),
    )
    result = _probe(
        'result = c.verify(**kwargs, models_dir=Path(os.environ["MODELS"]))\n',
        env, tmp_path, python=python,
    )
    assert result.returncode == 0, (result.stdout, result.stderr)
    payload = json.loads(result.stdout)
    assert payload["result"] == "verified"
    assert payload["source"]["origin"]["kind"] == "installed-vcs"
    assert payload["source"]["origin"]["vcs_verified"] is True
    assert payload["source"]["commit"] == conformance.EXPECTED_REVISION
    assert payload["source"]["imports_verified"] is True


def test_actual_same_version_foreign_installed_origin(
    artifacts: dict[str, Path], tmp_path: Path
) -> None:
    python = os.environ.get("COURSES_GNN_FOREIGN_PYTHON")
    if not python:
        pytest.skip("No genuine same-version foreign installation; not origin-rejection evidence")
    env = _environment(tmp_path)
    env.update(
        COURSES_GNN_MODE="installed",
        COURSES_GNN_BOOTSTRAP=str(artifacts["bootstrap"]),
        COURSES_GNN_MANIFEST=str(artifacts["manifest"]),
    )
    result = _probe(
        """
        from importlib.metadata import distribution
        installed = distribution("generalized-notation-notation")
        assert installed.version == "5.0.3"
        origin = json.loads(installed.read_text("direct_url.json"))
        assert origin["vcs_info"]["vcs"] == "git"
        with c.qualified_runtime(**kwargs) as receipt:
            result = receipt
        """,
        env, tmp_path, python=python,
    )
    payload = _failure(result, "source-origin-mismatch")
    assert payload["gnn_imported"] is False
