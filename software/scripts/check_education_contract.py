#!/usr/bin/env python3
"""Check the group's education contract: the canonical schema and every member copy.

Two modes, one implementation:

* no arguments -- read ``specs/education/contract.json``, then each member checkout
  named there. A member is ``adopted`` when its vendored ``specs/education/schema.json``
  is byte-identical to the canonical one, its ``education-contract.json`` pointer names
  the current digest, and every bundle it declares validates. A member with nothing is
  ``pending``. A member with a stale copy, a stale pointer, or an invalid bundle is
  ``diverged`` and fails the gate. ``--strict`` makes ``pending`` fail too.
* bundle paths -- validate exactly those documents (schema, then the coherence rules).

Usage:
    python scripts/check_education_contract.py
    python scripts/check_education_contract.py --strict
    python scripts/check_education_contract.py --json
    python scripts/check_education_contract.py specs/education/active-inference.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SOFTWARE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SOFTWARE))

from src.education_contract import (  # noqa: E402
    ADOPTED,
    DIVERGED,
    PENDING,
    UNAVAILABLE,
    Issue,
    check_contract,
    load_registry,
    run_rules,
    schema_digest,
    validate_document,
)
from src.education_contract.registry import REGISTRY_PATH  # noqa: E402
from src.education_contract.schema import DEFAULT_SCHEMA_PATH  # noqa: E402

ROOT = SOFTWARE.parent


def _print_issues(issues: tuple[Issue, ...]) -> None:
    for issue in issues:
        print(f"      {issue}")


def run_members(registry_path: Path, member_root: Path, schema_path: Path) -> tuple[int, dict]:
    """Check every member; return (exit code, machine-readable report)."""
    registry = load_registry(registry_path)
    report = check_contract(
        registry,
        member_root=member_root,
        canonical_schema=schema_path,
        repo_root=ROOT,
    )

    print(f"education contract: {registry.contract}  schema sha256 {schema_digest(schema_path)}")
    print(f"member root: {member_root}")
    print()
    print(f"{'member':34s} {'state':12s} detail")
    for member in report.members:
        print(f"{member.id:34s} {member.state:12s} {member.detail}")
        if member.state == DIVERGED:
            _print_issues(member.issues)
    if report.registry_issues:
        print()
        print("registry problems:")
        _print_issues(report.registry_issues)

    counts = {
        state: len(report.by_state(state)) for state in (ADOPTED, PENDING, DIVERGED, UNAVAILABLE)
    }
    print()
    print(
        f"contract: {'OK' if report.ok else 'FAILED'} -- "
        f"{counts[ADOPTED]} adopted, {counts[PENDING]} pending, "
        f"{counts[DIVERGED]} diverged, {counts[UNAVAILABLE]} unavailable"
    )
    payload = {
        "contract": registry.contract,
        "schema_sha256": schema_digest(schema_path),
        "ok": report.ok,
        "counts": counts,
        "registry_issues": [str(issue) for issue in report.registry_issues],
        "members": [
            {
                "id": member.id,
                "repository": member.repository,
                "state": member.state,
                "detail": member.detail,
                "bundles": list(member.bundles),
                "issues": [str(issue) for issue in member.issues],
            }
            for member in report.members
        ],
    }
    return (0 if report.ok else 1), payload


def run_bundles(paths: list[Path], schema_path: Path) -> tuple[int, dict]:
    """Validate the named documents directly."""
    failed = 0
    results = []
    for path in paths:
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            print(f"{path}: unreadable: {error}")
            results.append({"path": str(path), "ok": False, "issues": [str(error)]})
            failed += 1
            continue
        if not isinstance(document, dict):
            print(f"{path}: must hold a JSON object")
            results.append({"path": str(path), "ok": False, "issues": ["not an object"]})
            failed += 1
            continue
        issues = validate_document(document, schema_path) + run_rules(document)
        units = len(document.get("units", [])) if isinstance(document.get("units"), list) else 0
        edges = (
            len(document.get("prerequisite_edges", []))
            if isinstance(document.get("prerequisite_edges"), list)
            else 0
        )
        terms = (
            len(document.get("glossary", [])) if isinstance(document.get("glossary"), list) else 0
        )
        if issues:
            print(f"{path}: FAILED ({len(issues)} issue(s))")
            for issue in issues:
                print(f"  {issue}")
            failed += 1
        else:
            print(f"{path}: OK -- {units} unit(s), {edges} edge(s), {terms} term(s)")
        results.append(
            {"path": str(path), "ok": not issues, "issues": [str(issue) for issue in issues]}
        )
    return (0 if failed == 0 else 1), {"bundles": results}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundles", nargs="*", type=Path, help="validate these documents instead")
    parser.add_argument("--registry", type=Path, default=ROOT / REGISTRY_PATH)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA_PATH)
    parser.add_argument(
        "--member-root",
        type=Path,
        default=ROOT.parent,
        help="directory holding one checkout per member (default: this repository's parent)",
    )
    parser.add_argument("--strict", action="store_true", help="treat pending members as failures")
    parser.add_argument("--json", action="store_true", help="print a JSON report to stdout")
    args = parser.parse_args(argv)

    if args.bundles:
        code, payload = run_bundles(args.bundles, args.schema)
    else:
        code, payload = run_members(args.registry, args.member_root, args.schema)
        if args.strict and code == 0:
            pending = payload["counts"][PENDING] + payload["counts"][UNAVAILABLE]
            if pending:
                print(f"strict: {pending} member(s) have not adopted the contract")
                payload["ok"] = False
                code = 1

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
