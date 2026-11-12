"""Tests for the GNN conformance gate's interpretation of the checker result.

The checker returns ``True`` on success, ``2`` for invalid or missing files, and
``False`` for a hard failure. Only literal ``True`` may pass.
"""

from __future__ import annotations

import sys
import types

import pytest

from scripts import verify_gnn_conformance as conformance

PIN = {"tag": "v5.0.3"}


class FakeChecker:
    def __init__(self, result: object) -> None:
        self.result = result

    def validate_gnn_files(self, target, output, **kwargs):
        return self.result


def fake_gnn(monkeypatch: pytest.MonkeyPatch, result: object) -> None:
    """Install a minimal stand-in for the pinned parser package."""
    gnn = types.ModuleType("gnn")
    gnn.__version__ = "5.0.3"
    gnn.__path__ = []  # type: ignore[attr-defined]

    parsers = types.ModuleType("gnn.parsers")
    parsers.__path__ = []  # type: ignore[attr-defined]
    basic = types.ModuleType("gnn.parsers.basic")
    basic.parse_gnn_formal = lambda path: types.SimpleNamespace(parse_errors=[])
    basic.validate_gnn_syntax = lambda text: (True, [])

    type_checker = types.ModuleType("gnn.type_checker")
    type_checker.GNNTypeChecker = lambda: FakeChecker(result)

    modules = {
        "gnn": gnn,
        "gnn.parsers": parsers,
        "gnn.parsers.basic": basic,
        "gnn.type_checker": type_checker,
    }
    for name, module in modules.items():
        monkeypatch.setitem(sys.modules, name, module)
        if "." in name:
            parent, _, child = name.rpartition(".")
            setattr(modules[parent], child, module)


def exemplars(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    models = tmp_path / "models"
    models.mkdir()
    for index in range(conformance.EXPECTED_EXEMPLARS):
        (models / f"model_{index}.md").write_text("# exemplar\n", encoding="utf-8")
    monkeypatch.setattr(conformance, "MODELS_DIR", models)


def test_verify_accepts_literal_true(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    exemplars(tmp_path, monkeypatch)
    fake_gnn(monkeypatch, True)

    result = conformance.verify(PIN)

    assert result["result"] == "verified"
    assert result["type-checked"] == conformance.EXPECTED_EXEMPLARS


@pytest.mark.parametrize(
    "checked",
    [2, False, None, 0],
    ids=["warning-2", "hard-failure-false", "none", "zero"],
)
def test_verify_rejects_every_non_true_checker_result(
    tmp_path, monkeypatch: pytest.MonkeyPatch, checked: object
) -> None:
    exemplars(tmp_path, monkeypatch)
    fake_gnn(monkeypatch, checked)

    with pytest.raises(conformance.ConformanceError) as excinfo:
        conformance.verify(PIN)

    assert f"validate_gnn_files returned {checked!r}" in str(excinfo.value)
