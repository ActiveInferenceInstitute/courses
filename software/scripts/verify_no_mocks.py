#!/usr/bin/env python3
"""Verify no-mocks policy: fail if any test file imports or uses mocks/stubs.

The courses repo enforces a strict 'no mocks' policy. All tests must exercise
real implementations. This script scans tests/ for prohibited patterns and
exits non-zero if any are found.

Usage:
    python scripts/verify_no_mocks.py           # run from software/ dir
    python software/scripts/verify_no_mocks.py  # run from repo root
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Patterns that indicate mock/stub usage.
# NOTE: pytest's built-in `monkeypatch` fixture is NOT a mock — it temporarily
# sets environment variables, current working directory, or sys.path entries.
# It does NOT create mock objects or stub out interfaces. It is intentionally
# excluded from this checker. Only unittest.mock imports and their classes
# (MagicMock, Mock, @patch, patch()) indicate policy violations.
PROHIBITED_PATTERNS: list[tuple[str, str]] = [
    (r"from unittest(\.mock)?\s+import", "unittest.mock import"),
    (r"import unittest\.mock", "unittest.mock import"),
    (r"\bMagicMock\b", "MagicMock"),
    (r"\bMockObject\b", "MockObject"),
    (r"\bpatch\s*\(", "patch()"),
    (r"@patch\b", "@patch decorator"),
    (r"\bMock\s*\(", "Mock()"),
    (r"import mock\b", "mock import"),
    (r"from mock\b", "mock import"),
    (r"\bresponses\b.*add\b", "responses mock library"),
    (r"\bhttpretty\b", "httpretty mock library"),
    (r"\brespx\b", "respx mock library"),
]


def find_tests_dir() -> Path:
    """Locate the tests/ directory relative to CWD."""
    cwd = Path.cwd()
    # Running from software/ or repo root
    for candidate in [cwd / "tests", cwd / "software" / "tests"]:
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(
        f"Could not find tests/ directory from {cwd}. "
        "Run from the software/ directory or the repository root."
    )


# Files that are themselves policy-enforcement tests — they legitimately contain
# the prohibited pattern strings as *regex literals*, not as actual mock usage.
EXCLUDED_FILES: set[str] = {"test_real_implementations.py"}


def check_file(path: Path) -> list[tuple[int, str, str]]:
    """Return list of (line_num, pattern_name, line) violations in a file."""
    if path.name in EXCLUDED_FILES:
        return []

    violations: list[tuple[int, str, str]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return violations

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Skip pure comment lines
        if stripped.startswith("#"):
            continue
        # Skip lines that are clearly pattern-definition string literals
        # e.g.  r"from unittest.mock import"  or  "MagicMock\("
        if re.match(r'^\s*r?["\'].*["\'],?\s*$', line) and (
            "import" in line or "\\" in line
        ):
            continue
        for pattern, name in PROHIBITED_PATTERNS:
            if re.search(pattern, line):
                violations.append((line_num, name, line.rstrip()))
    return violations


def main() -> int:
    try:
        tests_dir = find_tests_dir()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    test_files = list(tests_dir.rglob("test_*.py")) + list(
        tests_dir.rglob("conftest.py")
    )

    total_violations = 0
    for test_file in sorted(test_files):
        violations = check_file(test_file)
        if violations:
            for line_num, name, line in violations:
                rel = test_file.relative_to(tests_dir.parent)
                print(
                    f"  ✗ {rel}:{line_num} — prohibited '{name}'\n    {line}",
                    file=sys.stderr,
                )
                total_violations += 1

    if total_violations:
        print(
            f"\n❌ No-mocks policy violated: {total_violations} occurrence(s) found.\n"
            "   Use real implementations and real temp files instead of mocks.\n"
            "   See software/docs/CONTRIBUTING.md for the no-mocks policy.",
            file=sys.stderr,
        )
        return 1

    print(f"✅ No-mocks policy: {len(test_files)} file(s) checked, 0 violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
