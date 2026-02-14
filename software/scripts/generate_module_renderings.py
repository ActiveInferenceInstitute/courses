#!/usr/bin/env python3
"""Script to generate all renderings for a specific module.

Usage:
    uv run python scripts/generate_module_renderings.py [OPTIONS]

Options:
    --course COURSE    Course to process (e.g. ai-philosophy)
    --module MODULE    Module number to process (default: 1)
    --help             Show this help message

Examples:
    # Generate renderings for ai-philosophy module-1
    uv run python scripts/generate_module_renderings.py --course ai-philosophy --module 1

    # Generate renderings for ai-math module-2
    uv run python scripts/generate_module_renderings.py --course ai-math --module 2
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import process_module_by_type
from src.module_organization.utils import find_module_path


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate all renderings for a specific module.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --course ai-philosophy --module 1   Generate for ai-philosophy/module-1
  %(prog)s --course ai-math                    Generate for ai-math/module-1
  %(prog)s --course ai-math --module 3         Generate for ai-math/module-3
        """,
    )

    parser.add_argument(
        "--course",
        choices=list(COURSE_REGISTRY.keys()),
        help="Course to process",
        required=True
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

    print(f"Generating renderings for: {module_path.name}")
    print(f"Course: {args.course}")

    # Process all supported types for this module
    # We use module_path / "output" as the target
    output_dir = module_path / "output"
    
    # 1. Module (Lecture)
    process_module_by_type(str(module_path), str(output_dir))
    
    # 2. Lab
    if (module_path / "lab.md").exists():
        process_module_by_type(str(module_path), str(output_dir))
        
    # 3. Questions
    if (module_path / "questions.md").exists():
        process_module_by_type(str(module_path), str(output_dir))

    return 0



if __name__ == "__main__":
    sys.exit(main())
