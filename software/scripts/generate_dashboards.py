#!/usr/bin/env python3
"""Generate interactive dashboards for all Active Inference course modules.

Thin orchestrator: delegates to src.content_processing.dashboards.
"""

import argparse
import sys
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.utils import extract_course_info_from_path as extract_course_info
from src.content_processing.dashboards import generate_dashboard_html, get_theme, DEFAULT_THEME

DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"


def generate_dashboard_files(module_dir: Path, base: Path, dry_run: bool = False) -> None:
    html = generate_dashboard_html(module_dir, base)
    if not dry_run:
        (module_dir / "dashboard.html").write_text(html, encoding="utf-8")


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate dashboards for AI courses.")
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()),
                        help="Only process this course")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE,
                        help="Base course_development directory")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-core", action="store_true",
                        help="Also regenerate active_inference core dashboards")
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    base = args.base

    modules = []
    for mmd in sorted(base.rglob("module.md")):
        md_dir = mmd.parent
        if "output" in md_dir.parts or any(p.startswith(("__", ".")) for p in md_dir.parts):
            continue
            
        info = extract_course_info(mmd, base)
        
        if args.course and info["course"] != args.course:
            continue
            
        modules.append(md_dir)

    generated = skipped = errors = 0
    for md_dir in modules:
        info = extract_course_info(md_dir / "module.md", base)
        
        is_core = info["course"].startswith("ai-") and not any(x in info["course"] for x in ["es", "ms", "hs", "101", "401", "embodied", "organizations", "robotics", "family"])
        
        if is_core and not args.include_core:
            skipped += 1
            continue
            
        try:
            generate_dashboard_files(md_dir, base, dry_run=args.dry_run)
            generated += 1
            action = "Would generate" if args.dry_run else "Generated"
            print(f"  {action}: {md_dir.relative_to(base)}/dashboard.html")
        except Exception as e:
            errors += 1
            print(f"  ERROR: {md_dir.relative_to(base)}: {e}")

    print(f"\nDone: {generated} generated, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
