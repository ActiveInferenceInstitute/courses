#!/usr/bin/env python3
"""Script to generate all renderings for syllabus files.

Usage:
    uv run python scripts/generate_syllabus_renderings.py [OPTIONS]

Options:
    --course COURSE    Course to process (e.g., ai-philosophy)
    --help             Show this help message

Examples:
    # Generate syllabus renderings for ai-philosophy (default)
    uv run python scripts/generate_syllabus_renderings.py

    # Generate syllabus renderings for ai-math
    uv run python scripts/generate_syllabus_renderings.py --course ai-math
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processing.config import COURSE_REGISTRY
from src.batch_processing.main import process_syllabus


def parse_args(argv=None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate all renderings for syllabus files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                         Generate for ai-philosophy syllabus (default)
  %(prog)s --course ai-math        Generate for ai-math syllabus
        """,
    )

    parser.add_argument(
        "--course",
        choices=list(COURSE_REGISTRY.keys()),
        default="ai-philosophy",
        help="Course to process (default: ai-philosophy)",
    )

    return parser.parse_args(argv)


def main(argv=None) -> int:
    """Generate all renderings for syllabus files."""
    args = parse_args(argv)

    # Paths
    repo_root = Path(__file__).parent.parent.parent
    
    if args.course not in COURSE_REGISTRY:
        print(f"Error: Course {args.course} not found in registry")
        return 1
        
    rel_path = COURSE_REGISTRY[args.course]["rel_path"]
    
    # Check if syllabus location is defined in registry, otherwise default to "syllabus"
    syllabus_loc = COURSE_REGISTRY[args.course].get("syllabus_location", "syllabus")
    
    # If syllabus_location is a file (ends in .md), get parent dir
    # If it's a dir, use it directly
    course_root = repo_root / rel_path
    
    if syllabus_loc.endswith(".md"):
        syllabus_path = course_root / Path(syllabus_loc).parent
    else:
        syllabus_path = course_root / syllabus_loc
        
    output_dir = syllabus_path / "output"

    if not syllabus_path.exists():
        print(f"Error: Syllabus path does not exist: {syllabus_path}")
        return 1

    print(f"Processing: {args.course}/syllabus")
    print(f"Output directory: {output_dir}")

    try:
        results = process_syllabus(str(syllabus_path), str(output_dir))

        # Print summary
        print("\n=== Generation Summary ===")
        print(f"PDF files: {results['summary']['pdf']}")
        print(f"Audio files (MP3): {results['summary']['mp3']}")
        print(f"DOCX files: {results['summary']['docx']}")
        print(f"HTML files: {results['summary']['html']}")
        print(f"TXT files: {results['summary']['txt']}")

        print("\n=== Files by Format ===")
        for format_type, files in results["by_format"].items():
            if files:
                print(f"\n{format_type}/ ({len(files)} files):")
                for file_path in sorted(files):
                    print(f"  - {Path(file_path).name}")

        if results["errors"]:
            print("\n=== Errors ===")
            for error in results["errors"]:
                print(f"  - {error}")
            return 1

        print("\n✓ All renderings generated successfully!")
        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
