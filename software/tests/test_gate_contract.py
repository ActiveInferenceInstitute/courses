"""Exercise the real gate/checker/exporter, never substitute a passing command."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.check_education_contract import main as check_main
from src.education_contract import build_bundle, render_bundle, schema_digest
from src.education_contract.schema import DEFAULT_SCHEMA_PATH

ROOT = Path(__file__).resolve().parents[2]


def source_fixture(root):
    module = root / "course_development/active_inference/01_philosophy/01_systems/module.md"
    module.parent.mkdir(parents=True)
    module.write_text("# Systems\n\n## Learning Objectives\n\n1. Explain the boundary of a system.\n")
    rendered = render_bundle(build_bundle("active_inference", repo_root=root))
    output = root / "specs/education/active-inference.json"
    output.parent.mkdir(parents=True)
    output.write_text(rendered)
    return output, rendered


@pytest.mark.parametrize("failing_phase", ["checker", "exporter"])
def test_gate_forwards_relative_arguments_and_each_failure(tmp_path, failing_phase):
    root = tmp_path / "isolated-owner"
    output, rendered = source_fixture(root)
    caller = tmp_path / "caller"
    caller.mkdir()
    bundle = caller / "selected.json"
    bundle.write_text("{}" if failing_phase == "checker" else rendered)
    (caller / "schema.json").write_bytes(DEFAULT_SCHEMA_PATH.read_bytes())
    if failing_phase == "exporter":
        output.write_text(rendered + " ")
    before = output.read_bytes()
    result = subprocess.run(
        ["bash", str(ROOT / "run.sh"), "contract", "selected.json", "--schema", "schema.json",
         "--repo-root", str(root), "--json"],
        cwd=caller,
        env={**os.environ, "COURSES_PYTHON": sys.executable, "GATE_TIMINGS": "0",
             "UV_OFFLINE": "1", "UV_NO_SYNC": "1", "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True, text=True, check=False,
    )
    assert result.returncode != 0
    report = json.loads(result.stdout)
    assert report["ok"] is False
    assert report["bundles"][0]["ok"] is (failing_phase != "checker")
    assert report["export"]["ok"] is (failing_phase != "exporter")
    assert "arm=contract" in result.stderr
    assert output.read_bytes() == before
    assert not (root / "docs/_generated").exists()


def test_gate_success_stdout_is_one_complete_json_value(tmp_path):
    output, _ = source_fixture(tmp_path)
    result = subprocess.run(
        ["bash", str(ROOT / "run.sh"), "contract", str(output),
         "--repo-root", str(tmp_path), "--json"],
        env={**os.environ, "COURSES_PYTHON": sys.executable, "GATE_TIMINGS": "0",
             "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["ok"] is True and payload["export"]["ok"] is True


def test_strict_pending_member_fails_with_machine_readable_report(tmp_path, capsys):
    (tmp_path / "members/pending").mkdir(parents=True)
    (tmp_path / "contract.md").write_text("Fixture contract authority.")
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({
        "schema": "education-contract-registry/v1", "contract": "education-contract/v1",
        "schema_sha256": schema_digest(), "contract_doc": "contract.md",
        "members": [{"id": "pending", "repository": "ActiveInferenceInstitute/pending"}],
    }))
    code = check_main(["--registry", str(registry), "--repo-root", str(tmp_path),
                       "--member-root", str(tmp_path / "members"), "--strict", "--json"])
    assert code == 1
    report = json.loads(capsys.readouterr().out)
    assert report["ok"] is False
    assert report["counts"]["pending"] == 1
