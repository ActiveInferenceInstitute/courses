#!/usr/bin/env python3
"""Transcribe one course directory into an ``education-contract/v1`` bundle.

The transcription rules live in ``src/education_contract/catalog.py``; this script only
writes or checks the result.

Usage:
    python scripts/export_education_bundle.py                     # rewrite the bundle
    python scripts/export_education_bundle.py --check             # fail if it is stale
    python scripts/export_education_bundle.py --course active_inference_101 \\
        --out specs/education/active-inference-101.json
"""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

SOFTWARE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SOFTWARE))

from src.education_contract import build_bundle, render_bundle  # noqa: E402

ROOT = SOFTWARE.parent
DEFAULT_COURSE = "active_inference"
DEFAULT_OUT = ROOT / "specs" / "education" / "active-inference.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--course", default=DEFAULT_COURSE, help="directory under course_development/"
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--check", action="store_true", help="do not write; fail if the file differs"
    )
    args = parser.parse_args(argv)

    rendered = render_bundle(build_bundle(args.course))
    destination = args.out if args.out.is_absolute() else ROOT / args.out

    if args.check:
        if not destination.is_file():
            print(f"{destination} is missing; run without --check to create it")
            return 1
        current = destination.read_text(encoding="utf-8")
        if current == rendered:
            print(f"{destination.relative_to(ROOT)} is current")
            return 0
        diff = list(
            difflib.unified_diff(
                current.splitlines(keepends=True),
                rendered.splitlines(keepends=True),
                fromfile=f"{destination} (committed)",
                tofile=f"{destination} (transcribed from course_development/{args.course})",
                n=1,
            )
        )
        print("".join(diff[:80]), end="")
        print(f"\n{destination.relative_to(ROOT)} is stale; run without --check to rewrite it")
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(rendered, encoding="utf-8")
    print(f"wrote {destination.relative_to(ROOT)} for course_development/{args.course}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
