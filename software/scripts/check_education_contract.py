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
import subprocess
from contextlib import redirect_stdout
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
    run_cross_rules,
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


def run_members(
    registry_path: Path,
    member_root: Path,
    schema_path: Path,
    *,
    repo_root: Path = ROOT,
    member_paths: dict[str, Path] | None = None,
) -> tuple[int, dict]:
    """Check every member; return (exit code, machine-readable report)."""
    registry = load_registry(registry_path)
    member_paths = dict(member_paths or {})
    if any(member.id == "courses" for member in registry.members):
        member_paths.setdefault("courses", repo_root)
    report = check_contract(
        registry,
        member_root=member_root,
        canonical_schema=schema_path,
        repo_root=repo_root,
        member_paths=member_paths,
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
    admitted: dict[str, list[dict]] = {}
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
        issues = validate_document(document, schema_path)
        if not issues:
            admitted.setdefault(document["provenance"]["repository"], []).append(document)
            issues.extend(run_rules(document))
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
    group_issues = run_cross_rules(admitted)
    for issue in group_issues:
        print(str(issue))
    return (1 if failed or group_issues else 0), {
        "ok": not failed and not group_issues,
        "bundles": results,
        "group_issues": [str(issue) for issue in group_issues],
    }


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
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=ROOT,
        help="registry owner root for contract_doc containment",
    )
    parser.add_argument(
        "--member-path",
        action="append",
        default=[],
        metavar="ID=PATH",
        help="actual isolated member checkout; repeat for multiple members",
    )
    parser.add_argument("--strict", action="store_true", help="treat pending members as failures")
    parser.add_argument("--json", action="store_true", help="print a JSON report to stdout")
    parser.add_argument(
        "--check-export",
        action="store_true",
        help="also check authored courses bundle freshness without writing",
    )
    args = parser.parse_args(argv)

    try:
        member_paths = {}
        for value in args.member_path:
            identity, separator, path = value.partition("=")
            if not separator or not identity or not path or identity in member_paths:
                raise ValueError(f"invalid or duplicate --member-path: {value}")
            member_paths[identity] = Path(path).resolve()
        # Human diagnostics go to stderr even when a caller asks for one JSON value.
        with redirect_stdout(sys.stderr):
            if args.bundles:
                code, payload = run_bundles(args.bundles, args.schema)
            else:
                code, payload = run_members(
                    args.registry,
                    args.member_root,
                    args.schema,
                    repo_root=args.repo_root,
                    member_paths=member_paths,
                )
                if args.strict:
                    pending = payload["counts"][PENDING] + payload["counts"][UNAVAILABLE]
                    if pending:
                        print(f"strict: {pending} member(s) have not adopted the contract")
                        payload["ok"] = False
                        code = 1
    except (OSError, ValueError, RuntimeError) as error:
        code, payload = 1, {"ok": False, "issues": [str(error)]}
        print(f"education contract: {error}", file=sys.stderr)
    if args.check_export:
        try:
            exported = subprocess.run(
                [
                    sys.executable,
                    str(SOFTWARE / "scripts/export_education_bundle.py"),
                    "--check",
                    "--repo-root",
                    str(args.repo_root),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            payload["export"] = {
                "ok": exported.returncode == 0,
                "exit_code": exported.returncode,
                "stdout": exported.stdout,
                "stderr": exported.stderr,
            }
            if exported.stdout:
                print(exported.stdout, file=sys.stderr, end="")
            if exported.stderr:
                print(exported.stderr, file=sys.stderr, end="")
            if exported.returncode:
                code = code or exported.returncode
                payload["ok"] = False
        except OSError as error:
            payload["export"] = {"ok": False, "issues": [str(error)]}
            payload["ok"], code = False, code or 1
            print(f"education export: {error}", file=sys.stderr)
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
