#!/usr/bin/env python3
"""Verify the pinned GNN parser against the committed exemplars.

This is the single implementation of the repository's GNN conformance check.
`.github/workflows/ci.yml` and `./run.sh gnn` both call this file; neither
carries its own copy of the logic.

The pin lives in `.github/gnn-pin.json` (schema `gnn-importer-pin/v1`) and names
the upstream repository, the exact commit, and the release tag. Conformance
means: the installed parser reports the pinned version, every committed exemplar
under `course_development/gnn/01_gnn_syntax/models` parses cleanly, and the GNN
type checker accepts the directory.

Usage:
    python software/scripts/verify_gnn_conformance.py            # verify
    python software/scripts/verify_gnn_conformance.py --install  # install pin, then verify

`--install` installs the pinned parser with pip into the running interpreter.
It is the only network step; verification itself is offline.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIN_PATH = ROOT / ".github" / "gnn-pin.json"
MODELS_DIR = ROOT / "course_development" / "gnn" / "01_gnn_syntax" / "models"

PIN_SCHEMA = "gnn-importer-pin/v1"
EXPECTED_REPOSITORY = "ActiveInferenceInstitute/Generalized_Notation_Notation"
EXPECTED_EXEMPLARS = 5
# Runtime dependencies of the pinned parser that its own metadata does not
# declare; installed explicitly so `--no-deps` stays honest.
PARSER_DEPENDENCIES = ("defusedxml", "psutil", "pyyaml")

REVISION_RE = re.compile(r"^[0-9a-f]{40}$")


class ConformanceError(RuntimeError):
    """A pin or conformance check failed."""


def load_pin() -> dict[str, str]:
    """Read and validate the canonical pin file."""
    try:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ConformanceError(f"cannot read {PIN_PATH.relative_to(ROOT)}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ConformanceError(f"{PIN_PATH.relative_to(ROOT)} is not valid JSON: {exc}") from exc

    if not isinstance(pin, dict):
        raise ConformanceError(f"{PIN_PATH.relative_to(ROOT)} must be a JSON object")
    if pin.get("schema") != PIN_SCHEMA:
        raise ConformanceError(f"pin schema is {pin.get('schema')!r}, expected {PIN_SCHEMA!r}")
    if pin.get("repository") != EXPECTED_REPOSITORY:
        raise ConformanceError(
            f"pin repository is {pin.get('repository')!r}, expected {EXPECTED_REPOSITORY!r}"
        )
    if not REVISION_RE.match(str(pin.get("revision", ""))):
        raise ConformanceError(f"pin revision is not a full commit SHA: {pin.get('revision')!r}")
    tag = str(pin.get("tag", ""))
    if not tag.startswith("v") or not tag[1:]:
        raise ConformanceError(f"pin tag is not a v-prefixed release: {tag!r}")
    return pin


def installed_version() -> str | None:
    """Return the importable parser version, or None when it is absent."""
    try:
        from gnn import __version__
    except ImportError:
        return None
    return str(__version__)


def ensure_pin(pin: dict[str, str]) -> None:
    """Install the pinned parser unless the running interpreter already has it."""
    if installed_version() == pin["tag"].removeprefix("v"):
        return
    spec = (
        "generalized-notation-notation @ "
        f"git+https://github.com/{pin['repository']}.git@{pin['revision']}"
    )
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            *PARSER_DEPENDENCIES,
        ]
    )
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-deps",
            spec,
        ]
    )


def exemplar_paths() -> list[Path]:
    """Return the committed exemplar sketches, excluding the folder README."""
    if not MODELS_DIR.is_dir():
        raise ConformanceError(f"missing exemplar directory: {MODELS_DIR.relative_to(ROOT)}")
    sketches = sorted(path for path in MODELS_DIR.glob("*.md") if path.name != "README.md")
    if len(sketches) != EXPECTED_EXEMPLARS:
        raise ConformanceError(
            f"expected {EXPECTED_EXEMPLARS} GNN exemplars, found {len(sketches)}"
        )
    return sketches


def verify(pin: dict[str, str]) -> dict[str, object]:
    """Check the installed parser and every exemplar against the pin."""
    try:
        from gnn import __version__
        from gnn.parsers.basic import parse_gnn_formal, validate_gnn_syntax
        from gnn.type_checker import GNNTypeChecker
    except ImportError as exc:
        raise ConformanceError(
            f"the pinned GNN parser is not importable ({exc}); run with --install"
        ) from exc

    expected_version = pin["tag"].removeprefix("v")
    if __version__ != expected_version:
        raise ConformanceError(
            f"installed GNN {__version__!r} does not match pinned tag {pin['tag']!r}"
        )

    sketches = exemplar_paths()
    for sketch in sketches:
        parsed = parse_gnn_formal(sketch)
        if parsed is None or getattr(parsed, "parse_errors", None):
            raise ConformanceError(f"{sketch.name} did not parse cleanly")
        valid, errors = validate_gnn_syntax(sketch.read_text(encoding="utf-8"))
        if not valid:
            raise ConformanceError(f"{sketch.name} syntax errors: {errors!r}")

    with tempfile.TemporaryDirectory(prefix="courses-gnn-") as output_dir:
        if not GNNTypeChecker().validate_gnn_files(MODELS_DIR, Path(output_dir)):
            raise ConformanceError("GNN type checker rejected the exemplar directory")

    return {
        "gnn-version": __version__,
        "parsed": len(sketches),
        "type-checked": len(sketches),
        "result": "verified",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--install",
        action="store_true",
        help="pip-install the pinned parser before verifying (network access required)",
    )
    args = parser.parse_args(argv)

    try:
        pin = load_pin()
        if args.install:
            ensure_pin(pin)
        result = verify(pin)
    except ConformanceError as exc:
        print(f"GNN conformance failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
