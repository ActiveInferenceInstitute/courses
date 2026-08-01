#!/usr/bin/env python3
"""Script to generate HTML website for a module.

Usage:
    uv run python scripts/generate_module_website.py [OPTIONS]

Options:
    --course COURSE    Course to process (e.g. ai-philosophy)
    --module MODULE    Module number to process (default: 1)
    --help             Show this help message

Examples:
    # Generate website for ai-philosophy module-1
    uv run python scripts/generate_module_website.py --course ai-philosophy --module 1

    # Generate website for ai-math module-2
    uv run python scripts/generate_module_website.py --course ai-math --module 2
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import process_module_website
from src.module_organization.utils import find_module_path


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate HTML website for a module.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --course ai-philosophy --module 1   Generate for ai-philosophy/module-1
  %(prog)s --course ai-math --module 2         Generate for ai-math/module-2
        """,
    )

    parser.add_argument(
        "--course", choices=list(COURSE_REGISTRY.keys()), help="Course to process", required=True
    )

    parser.add_argument(
        "--module",
        type=int,
        default=1,
        help="Module number to process (default: 1)",
    )

    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)

    # Paths
    repo_root = Path(__file__).parent.parent.parent

    # Resolve course path from registry
    if args.course not in COURSE_REGISTRY:
        print(f"Error: Course {args.course} not found in registry")
        return 1

    rel_path = COURSE_REGISTRY[args.course]["rel_path"]
    course_path = repo_root / rel_path

    # Find module path (supports both module-N and module-NN-topic patterns)
    module_path = find_module_path(course_path, args.module)

    if not module_path:
        print(f"Error: Module {args.module} not found in {course_path}")
        print("Available modules:")
        for p in sorted(course_path.glob("module-*")):
            print(f"  - {p.name}")
        return 1

    print(f"Generating website for: {module_path.name}")
    print(f"Course: {args.course}")

    # Generate website
    process_module_website(str(module_path))

    return 0


if __name__ == "__main__":
    sys.exit(main())
