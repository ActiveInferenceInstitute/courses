"""Exercise receipt binding and stale-evidence rejection with real files."""
import json
from pathlib import Path

import pytest

from scripts.gate_receipt import finish_receipt, source_binding, start_receipt
from scripts.generate_gate_metrics import read_coverage, read_timings, render_timings


def source_fixture(root):
    source = root / "software/src/example.py"
    source.parent.mkdir(parents=True)
    source.write_text("VALUE = 1\n")
    (root / "software/uv.lock").write_text("version = 1\n")
    return source


def coverage_fixture(root, percent):
    path = root / "software/coverage.json"
    path.write_text(json.dumps({"totals": {"percent_covered": percent}}))
    return path


def test_round_tripped_receipt_binds_actual_runtime_and_dirty_source(tmp_path):
    source = source_fixture(tmp_path)
    before = json.loads(json.dumps(start_receipt(tmp_path, "contract", ["--json"])))
    result = finish_receipt(tmp_path, before, 7)
    assert result["attribution"] == "bound"
    assert result["rc"] == 7
    assert result["runtime_unchanged"] is True
    assert result["runtime"]["executable_sha256"]
    assert result["source_before"]["files"][0]["path"].startswith("software/")
    assert result["coverage"] is None
    source.write_text("VALUE = 2\n")
    drift = finish_receipt(tmp_path, before, 0)
    assert drift["attribution"] == "rejected-drift"
    assert drift["source_unchanged"] is False
    assert drift["coverage"] is None


def test_coverage_requires_fresh_success_and_matching_source_runtime(tmp_path):
    source = source_fixture(tmp_path)
    coverage = coverage_fixture(tmp_path, 20)
    stale_start = start_receipt(tmp_path, "test", [])
    stale = finish_receipt(tmp_path, stale_start, 0)
    assert stale["coverage"] is None
    assert "unbound historical" in read_coverage(coverage, {"test": stale}, tmp_path)
    before = start_receipt(tmp_path, "test", [])
    coverage_fixture(tmp_path, 75)
    bound = finish_receipt(tmp_path, before, 0)
    assert "source/runtime-bound successful" in read_coverage(coverage, {"test": bound}, tmp_path)
    failed = finish_receipt(tmp_path, before, 1)
    assert failed["coverage"] is None
    assert "unbound historical" in read_coverage(coverage, {"test": failed}, tmp_path)
    source.write_text("VALUE = 3\n")
    assert "unbound historical" in read_coverage(coverage, {"test": bound}, tmp_path)


def test_legacy_receipts_are_preserved_and_labelled_unbound(tmp_path):
    source_fixture(tmp_path)
    legacy = tmp_path / "legacy.jsonl"
    legacy_bytes = b'{"arm":"test","seconds":1.5,"rc":1,"host":"old","commit":"abc"}\n'
    legacy.write_bytes(legacy_bytes)
    receipts = read_timings([legacy])
    rendered = render_timings(receipts, root=tmp_path)
    assert "historical/unbound" in rendered
    assert "| 1 | old | `abc` |" in rendered
    assert "not measured" in rendered
    assert legacy.read_bytes() == legacy_bytes


def test_source_binding_includes_new_authored_inputs_but_not_generated_outputs(tmp_path):
    source_fixture(tmp_path)
    before = source_binding(tmp_path)
    output = tmp_path / "course_development/example/01_systems/output/result.md"
    output.parent.mkdir(parents=True)
    output.write_text("generated")
    assert source_binding(tmp_path) == before
    authored = output.parents[1] / "module.md"
    authored.write_text("# Systems\n\nAuthored input.")
    after = source_binding(tmp_path)
    assert after["sha256"] != before["sha256"]
    assert any(row["path"] == str(authored.relative_to(tmp_path)) for row in after["files"])


def test_malformed_receipt_is_not_silently_dropped(tmp_path):
    path = tmp_path / "receipts.jsonl"
    path.write_text("null\n")
    with pytest.raises(ValueError, match="Invalid timing record"):
        read_timings([path])


def test_source_symlink_cannot_bind_an_external_file(tmp_path):
    root = tmp_path / "admitted"
    (root / "software/src").mkdir(parents=True)
    outside = tmp_path / "outside.py"
    outside.write_text("VALUE = 1\n")
    (root / "software/src/aliased.py").symlink_to(outside)
    with pytest.raises(ValueError, match="source escapes"):
        source_binding(root)
