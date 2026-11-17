#!/usr/bin/env python3
"""Run the courses GNN verdicts under the independently qualified v5.1.0 source.

Both admission modes require the reviewed bootstrap and independent full
manifest, supplied as files. Their digests are frozen here, not inferred from
the target package. Source mode additionally requires an explicit package root
already selected by Python's import resolution (normally via PYTHONPATH).
Installed mode requires the producer's actual PEP 610 Git-origin admission.

Use a fresh process. No installation, version-based reuse, or mode fallback is
performed. A successful receipt is returned only after the producer's guarded
import/execution context exits successfully. This is parser/type-checker
conformance, not scientific execution or dependency qualification.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager, redirect_stdout
from pathlib import Path
from types import ModuleType
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PIN_PATH = ROOT / ".github" / "gnn-pin.json"
MODELS_DIR = ROOT / "course_development" / "gnn" / "01_gnn_syntax" / "models"

PIN_SCHEMA = "gnn-importer-pin/v1"
EXPECTED_REPOSITORY = "ActiveInferenceInstitute/Generalized_Notation_Notation"
EXPECTED_EXEMPLARS = 5
EXPECTED_TAG = "v5.1.0"
EXPECTED_REVISION = "75c834bd8519dc7b5adc4d24f16bf393cfd1ecdf"
BOOTSTRAP_SHA256 = "f638d4c01fe7de31e43d793e59bf382d0c3d1a82f365c59238334a2b40adfb37"
MANIFEST_SHA256 = "43b33c0b2b40386afa3f306fec4cc13bc1fd7c3b570fbf11d5008bad5c8e6b51"
REVISION_RE = re.compile(r"^[0-9a-f]{40}$")


class ConformanceError(RuntimeError):
    """A pin or conformance check failed."""


def load_pin() -> dict[str, str]:
    """Read the repository pin without importing the package it describes."""
    try:
        pin = json.loads(PIN_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        raise ConformanceError(f"Cannot read GNN pin {PIN_PATH}: {exc}") from exc
    if not isinstance(pin, dict) or pin.get("schema") != PIN_SCHEMA:
        raise ConformanceError(f"Expected {PIN_SCHEMA} in {PIN_PATH}")
    if pin.get("repository") != EXPECTED_REPOSITORY:
        raise ConformanceError("GNN pin names a different repository")
    revision = pin.get("revision")
    if not isinstance(revision, str) or REVISION_RE.fullmatch(revision) is None:
        raise ConformanceError("GNN pin requires a full lowercase Git revision")
    if revision != EXPECTED_REVISION or pin.get("tag") != EXPECTED_TAG:
        raise ConformanceError("GNN pin does not match the independently reviewed v5.1.0 manifest")
    return pin


def _checked_bytes(path: Path, expected: str, label: str) -> bytes:
    try:
        payload = path.read_bytes()
    except OSError as exc:
        raise ConformanceError(f"Cannot read {label} {path}: {exc}") from exc
    if hashlib.sha256(payload).hexdigest() != expected:
        raise ConformanceError(f"{label} SHA-256 does not match the reviewed artifact")
    return payload


@contextmanager
def qualified_runtime(
    *,
    mode: str,
    bootstrap_path: Path,
    manifest_path: Path,
    package_root: Path | None = None,
) -> Iterator[dict[str, Any]]:
    """Guard all GNN imports and verdict execution in a fresh process.

    The yielded receipt is provisional inside the block. It is qualified only
    after successful exit. No sys.path alteration or installed-to-source
    fallback is made; the producer checks the caller's actual import resolution.
    """
    if mode not in {"installed", "source"}:
        raise ConformanceError("An explicit installed or source mode is required")
    if mode == "source" and package_root is None:
        raise ConformanceError("Source mode requires an explicit package root")
    pin = load_pin()
    bootstrap_path = bootstrap_path.resolve()
    bootstrap_bytes = _checked_bytes(bootstrap_path, BOOTSTRAP_SHA256, "bootstrap")
    manifest_bytes = _checked_bytes(manifest_path, MANIFEST_SHA256, "manifest")
    name = "_courses_qualified_gnn_bootstrap"
    if name in sys.modules:
        raise ConformanceError("A GNN qualification is already active; use a fresh process")
    bootstrap = ModuleType(name)
    bootstrap.__file__ = str(bootstrap_path)
    bootstrap.__package__ = ""
    sys.modules[name] = bootstrap
    try:
        # Execute precisely the bytes just checked: no source loader or pyc read.
        exec(
            compile(bootstrap_bytes, str(bootstrap_path), "exec", dont_inherit=True),
            bootstrap.__dict__,
        )
        producer_pin = bootstrap.ImporterPin(
            path=PIN_PATH,
            commit=pin["revision"],
            tag=pin["tag"],
            repository=pin["repository"],
            schema=pin["schema"],
            recorded=pin.get("recorded"),
            raw=pin,
        )
        try:
            with bootstrap.qualified_source(
                producer_pin,
                manifest=manifest_bytes,
                manifest_sha256=MANIFEST_SHA256,
                package_root=package_root,
                origin_mode=mode,
            ) as receipt:
                yield receipt
            if receipt["bootstrap"]["sha256"] != BOOTSTRAP_SHA256:
                raise ConformanceError("Bootstrap changed during guarded execution")
        except bootstrap.SourceQualificationError as exc:
            raise ConformanceError(f"{exc.code}: {exc}") from exc
    finally:
        del sys.modules[name]


def exemplar_paths(models_dir: Path = MODELS_DIR) -> list[Path]:
    """Keep the five-exemplar admission separate from producer source identity."""
    if not models_dir.is_dir():
        raise ConformanceError(f"Missing GNN exemplar directory: {models_dir}")
    paths = sorted(path for path in models_dir.glob("*.md") if path.name != "README.md")
    if len(paths) != EXPECTED_EXEMPLARS:
        raise ConformanceError(f"Expected {EXPECTED_EXEMPLARS} GNN exemplars, found {len(paths)}")
    return paths


def _typecheck(models_dir: Path) -> None:
    """Called only inside qualified_runtime; warnings are not conformance."""
    from gnn.type_checker import GNNTypeChecker

    with tempfile.TemporaryDirectory(prefix="courses-gnn-") as output:
        # Spawned workers would escape this process's checked-source loader.
        checked = GNNTypeChecker().validate_gnn_files(models_dir, Path(output), file_workers=1)
    if checked is not True:
        raise ConformanceError(f"GNN type checker did not succeed: {checked!r}")


def verify(
    *,
    mode: str,
    bootstrap_path: Path,
    manifest_path: Path,
    package_root: Path | None = None,
    models_dir: Path = MODELS_DIR,
) -> dict[str, Any]:
    """Return conformance evidence only after successful guarded execution."""
    paths = exemplar_paths(models_dir)
    with (
        redirect_stdout(sys.stderr),
        qualified_runtime(
            mode=mode,
            bootstrap_path=bootstrap_path,
            manifest_path=manifest_path,
            package_root=package_root,
        ) as source,
    ):
        from gnn import __version__
        from gnn.parsers.basic import parse_gnn_formal, validate_gnn_syntax

        if __version__ != EXPECTED_TAG.removeprefix("v"):
            raise ConformanceError(f"Unexpected admitted GNN version: {__version__}")
        for path in paths:
            content = path.read_text(encoding="utf-8")
            parsed = parse_gnn_formal(path)
            if parsed is None or parsed.parse_errors:
                errors = None if parsed is None else parsed.parse_errors
                raise ConformanceError(f"{path}: GNN parse failed: {errors}")
            valid, errors = validate_gnn_syntax(content, is_content=True)
            if valid is not True:
                raise ConformanceError(f"{path}: GNN syntax failed: {errors}")
        _typecheck(models_dir)
    return {
        "gnn-version": __version__,
        "parsed": len(paths),
        "type-checked": len(paths),
        "result": "verified",
        "source": source,
        "scope": "GNN parsing, syntax and type checking; no scientific execution",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode", choices=("installed", "source"), default=os.getenv("COURSES_GNN_MODE")
    )
    parser.add_argument(
        "--bootstrap",
        type=Path,
        default=os.getenv("COURSES_GNN_BOOTSTRAP"),
        help="Reviewed standalone producer bootstrap; digest is frozen in this consumer",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=os.getenv("COURSES_GNN_MANIFEST"),
        help="Independent full v5.1.0 source manifest; never generated from the target",
    )
    parser.add_argument(
        "--package-root",
        type=Path,
        default=os.getenv("COURSES_GNN_PACKAGE_ROOT"),
        help="Explicit gnn package directory; source mode also needs matching PYTHONPATH",
    )
    args = parser.parse_args(argv)
    for name in ("mode", "bootstrap", "manifest"):
        if not getattr(args, name):
            parser.error(f"--{name} or COURSES_GNN_{name.upper()} is required")
    try:
        result = verify(
            mode=args.mode,
            bootstrap_path=args.bootstrap,
            manifest_path=args.manifest,
            package_root=args.package_root,
        )
    except (ConformanceError, OSError, UnicodeError, ValueError, ImportError) as exc:
        print(f"GNN conformance failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
