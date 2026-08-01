#!/usr/bin/env python3
"""Script to flatten the PUBLISHED directory structure.

Thin orchestrator - delegates to src.publish.utils.

Usage:
    uv run python scripts/flatten_published.py
    uv run python scripts/flatten_published.py --path /custom/PUBLISHED
    uv run python scripts/flatten_published.py --dry-run --verbose
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.publish.utils import flatten_published


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Flatten the PUBLISHED directory structure.")
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        help="Path to PUBLISHED directory (default: auto-detect relative to repo root)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be flattened without doing it"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Show detailed file-level operations"
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Flatten all module directories in PUBLISHED."""
    args = parse_args(argv)

    if args.path:
        published_dir = Path(args.path)
    else:
        published_dir = Path(__file__).parent.parent.parent / "PUBLISHED"

    if not published_dir.exists():
        print(f"ERROR: PUBLISHED directory not found: {published_dir}")
        return 1

    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"{prefix}Flattening PUBLISHED directory: {published_dir}")
    print("=" * 60)

    # Delegate to module function
    moved = flatten_published(published_dir, dry_run=args.dry_run, verbose=args.verbose)

    print("\n" + "=" * 60)
    print(f"{prefix}Flattening complete! {moved} files moved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
