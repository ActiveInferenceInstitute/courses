#!/usr/bin/env python3
"""Bind a gate observation to pre-execution source and the actual Python runtime."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "courses-gate-receipt/v2"
SOURCE_DIRS = ("software/src", "software/scripts", "software/tests", "software/docs",
               ".github", ".agents", "specs", "course_development", "docs")
SOURCE_FILES = ("run.sh", "publish.py", "publish.toml", "education-contract.json",
                "software/pyproject.toml", "software/uv.lock", "software/.python-version")
SKIP_DIRS = {".git", ".venv", ".venv-gnn", "__pycache__", ".pytest_cache", ".mypy_cache",
             ".ruff_cache", "output", "outputs", "htmlcov", "node_modules", "_generated"}
SOURCE_SUFFIXES = {".py", ".sh", ".toml", ".lock", ".json", ".yaml", ".yml", ".md", ".markdown", ".css", ".html", ".js"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_binding(root: Path) -> dict:
    """Hash authored engine/test/schema/curriculum inputs, including dirty bytes.

    Rendered output/cache directories are excluded by policy, not by Git status.
    The returned manifest states the exact closure; it is not a whole-vault claim.
    """
    root = root.resolve()
    paths = {root / name for name in SOURCE_FILES if (root / name).is_file()}
    paths.update(root.glob("*.md"))
    paths.update(root.glob("*.yaml"))
    paths.update(root.glob("*.yml"))
    for relative in SOURCE_DIRS:
        directory = root / relative
        if directory.is_symlink():
            raise ValueError(f"source directory symlink is not admitted: {directory}")
        if not directory.is_dir():
            continue
        for parent, dirs, files in os.walk(directory, followlinks=False):
            dirs[:] = sorted(name for name in dirs if name not in SKIP_DIRS)
            for name in dirs:
                if (Path(parent) / name).is_symlink():
                    raise ValueError(f"source directory symlink is not admitted: {Path(parent) / name}")
            paths.update(Path(parent) / name for name in files if Path(name).suffix in SOURCE_SUFFIXES)
    manifest = []
    for path in sorted(paths):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"source escapes admitted root: {path}")
        data = path.read_bytes()
        manifest.append({"path": path.relative_to(root).as_posix(), "bytes": len(data),
                         "sha256": hashlib.sha256(data).hexdigest()})
    encoded = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    return {"root": str(root), "sha256": hashlib.sha256(encoded).hexdigest(), "files": manifest}


def runtime_binding() -> dict:
    executable = Path(sys.executable).resolve()
    return {"executable": str(executable), "executable_sha256": digest(executable),
            "version": sys.version, "prefix": sys.prefix, "platform": platform.platform(),
            "distributions": sorted([dist.metadata.get("Name", ""), dist.version]
                                    for dist in importlib.metadata.distributions())}


def coverage_identity(root: Path) -> dict | None:
    path = root / "software/coverage.json"
    if not path.is_file():
        return None
    stat = path.stat()
    return {"sha256": digest(path), "bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def start_receipt(root: Path, arm: str, arguments: list[str]) -> dict:
    source = source_binding(root)
    runtime = runtime_binding()
    coverage = coverage_identity(root)
    return {"schema": SCHEMA, "arm": arm, "arguments": arguments,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "started_monotonic": time.monotonic(), "source_before": source,
            "runtime": runtime, "coverage_before": coverage}


def finish_receipt(root: Path, before: dict, rc: int) -> dict:
    finished = time.monotonic()
    if before.get("schema") != SCHEMA or before["source_before"]["root"] != str(root.resolve()):
        raise ValueError("gate receipt does not bind this source root")
    after = source_binding(root)
    runtime = runtime_binding()
    unchanged = before["source_before"]["sha256"] == after["sha256"]
    same_runtime = before["runtime"] == runtime
    coverage = coverage_identity(root)
    return {**before, "seconds": finished - before["started_monotonic"],
            "at": datetime.now(timezone.utc).isoformat(), "host": platform.node(), "rc": rc,
            "source_after_sha256": after["sha256"], "source_unchanged": unchanged,
            "runtime_unchanged": same_runtime,
            "attribution": "bound" if unchanged and same_runtime else "rejected-drift",
            "coverage": coverage if (before["arm"] == "test" and rc == 0 and unchanged
                                      and same_runtime and coverage is not None
                                      and coverage != before["coverage_before"]) else None}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    begin = sub.add_parser("start")
    begin.add_argument("--root", type=Path, required=True)
    begin.add_argument("--out", type=Path, required=True)
    begin.add_argument("--arm", required=True)
    begin.add_argument("arguments", nargs=argparse.REMAINDER)
    end = sub.add_parser("finish")
    end.add_argument("--root", type=Path, required=True)
    end.add_argument("--snapshot", type=Path, required=True)
    end.add_argument("--rc", type=int, required=True)
    end.add_argument("--log", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.operation == "start":
            payload = start_receipt(args.root, args.arm, args.arguments)
            args.out.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")
            return 0
        payload = finish_receipt(args.root, json.loads(args.snapshot.read_text()), args.rc)
        args.log.parent.mkdir(parents=True, exist_ok=True)
        with args.log.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(payload, sort_keys=True) + "\n")
        return 0 if payload["attribution"] == "bound" else 1
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"gate evidence unavailable: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
