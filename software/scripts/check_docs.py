#!/usr/bin/env python3
"""Check the documentation surfaces: relative links and generated facts.

The repository has no mkdocs or markdown-link-check configuration, so this
script is its documentation gate. It does two things:

1. Resolves every relative Markdown link in the documentation surfaces listed
   in `DOC_GLOBS` and fails on a target that does not exist on disk. Anchors are
   stripped before resolution and not validated; external URLs are not fetched.
2. Runs `generate_gate_metrics.py --check`, so a stale generated number fails
   the same arm as a broken link.

Course content under `course_development/` and generated output under
`published/` are out of scope: they are bulk content, not documentation, and
their links point at generated artifacts.

Usage:
    python software/scripts/check_docs.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]

# Documentation surfaces: root guides, the docs hub, the software technical
# guides, agent guidance, and the GitHub-side pointers. `:(top,glob)` anchors the
# patterns at the repository root and keeps `*` from crossing a `/`, so
# `published/` and `course_development/` content is never pulled in by accident.
DOC_GLOBS = (
    ":(top,glob)*.md",
    ":(top,glob)docs/**/*.md",
    ":(top,glob)software/*.md",
    ":(top,glob)software/docs/**/*.md",
    ":(top,glob)software/src/**/AGENTS.md",
    ":(top,glob)software/tests/*.md",
    ":(top,glob)software/scripts/*.md",
    ":(top,glob).github/*.md",
    ":(top,glob).agents/**/*.md",
    ":(top,glob)course_development/README.md",
    ":(top,glob)course_development/AGENTS.md",
    ":(top,glob)summaries/AGENTS.md",
    ":(top,glob)published/AGENTS.md",
)

FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "ftp://")


def documentation_files() -> list[Path]:
    """Return the documentation files, tracked and untracked-but-not-ignored.

    Untracked files are included so a new guide is link-checked before it is
    staged; `git ls-files` alone would silently skip it.
    """
    names: set[str] = set()
    for extra in ((), ("--others", "--exclude-standard")):
        proc = subprocess.run(
            ["git", "ls-files", "-z", *extra, "--", *DOC_GLOBS],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        names.update(name for name in proc.stdout.split("\0") if name)
    return sorted(ROOT / name for name in names)


def strip_non_prose(text: str) -> str:
    """Blank out code fences, inline code, and HTML comments, keeping line numbers."""
    for pattern in (FENCE_RE, HTML_COMMENT_RE, INLINE_CODE_RE):
        text = pattern.sub(lambda match: "\n" * match.group(0).count("\n"), text)
    return text


def check_file(path: Path) -> list[tuple[int, str]]:
    """Return (line, target) for every relative link whose target is missing."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return [(0, f"unreadable: {exc}")]

    broken: list[tuple[int, str]] = []
    for line_number, line in enumerate(strip_non_prose(text).splitlines(), start=1):
        for target in LINK_RE.findall(line):
            if target.startswith(SKIP_SCHEMES) or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0])
            if not relative:
                continue
            base = ROOT if relative.startswith("/") else path.parent
            resolved = (base / relative.lstrip("/")).resolve()
            if not resolved.exists():
                broken.append((line_number, target))
    return broken


def main() -> int:
    failures = 0
    checked = 0
    for path in documentation_files():
        checked += 1
        for line_number, target in check_file(path):
            failures += 1
            location = f"{path.relative_to(ROOT)}:{line_number}"
            print(f"  ✗ {location} — missing target {target}", file=sys.stderr)

    metrics = subprocess.run(
        [
            sys.executable,
            str(ROOT / "software" / "scripts" / "generate_gate_metrics.py"),
            "--check",
        ],
        cwd=ROOT,
        check=False,
    )
    if metrics.returncode != 0:
        failures += 1

    if failures:
        print(f"\n❌ Documentation check failed: {failures} problem(s).", file=sys.stderr)
        return 1

    print(
        f"✅ Documentation check: {checked} file(s), 0 broken relative links, generated facts current."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
