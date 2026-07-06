"""CLI entry point and orchestration for course generation.

Provides functions for generating curricula, validating structure,
and listing available configurations.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from .config import ALL_CURRICULA, AGE_LEVEL_CURRICULA
from .logging_config import setup_logging, get_logger
from .scaffold import generate_curriculum
from .llm import OllamaClient, enrich_curriculum
from .utils import resolve_repo_root, validate_structure

logger = get_logger()


def generate(
    curriculum_id: str,
    output_dir: Optional[Path] = None,
    use_llm: bool = False,
    model: str = "llama3.2",
    overwrite: bool = False,
) -> dict:
    """Generate a single curriculum.

    Args:
        curriculum_id: ID from ALL_CURRICULA registry.
        output_dir: Output directory. Defaults to repo course_development/.
        use_llm: If True, use Ollama to enrich content.
        model: Ollama model name.
        overwrite: If True, overwrite existing files.

    Returns:
        Dictionary with generation stats.

    Raises:
        KeyError: If curriculum_id not found.
    """
    if curriculum_id not in ALL_CURRICULA:
        raise KeyError(
            f"Unknown curriculum: {curriculum_id}. "
            f"Available: {list(ALL_CURRICULA.keys())}"
        )

    config = ALL_CURRICULA[curriculum_id]

    if output_dir is None:
        repo_root = resolve_repo_root()
        output_dir = repo_root / config.parent_dir

    logger.info(f"Generating '{config.title}' → {output_dir / config.id}")
    stats = generate_curriculum(config, output_dir, overwrite=overwrite)

    if use_llm:
        logger.info(f"Enriching with Ollama (model: {model})...")
        client = OllamaClient(model=model)
        llm_stats = enrich_curriculum(
            client, str(output_dir / config.id), config
        )
        stats["llm_enriched"] = llm_stats.get("enriched", 0)
        stats["llm_errors"] = llm_stats.get("errors", 0)

    return stats


def generate_all(
    output_dir: Optional[Path] = None,
    use_llm: bool = False,
    model: str = "llama3.2",
    overwrite: bool = False,
) -> dict[str, dict]:
    """Generate all registered curricula.

    Args:
        output_dir: Base output directory.
        use_llm: If True, use Ollama to enrich content.
        model: Ollama model name.
        overwrite: If True, overwrite existing files.

    Returns:
        Dictionary mapping curriculum IDs to their generation stats.
    """
    results: dict[str, dict] = {}

    for cid in ALL_CURRICULA:
        config = ALL_CURRICULA[cid]
        # Resolve per-curriculum output dir based on parent_dir
        if output_dir is None:
            repo_root = resolve_repo_root()
            cur_output = repo_root / config.parent_dir
        else:
            cur_output = output_dir

        try:
            results[cid] = generate(
                cid, cur_output, use_llm=use_llm,
                model=model, overwrite=overwrite,
            )
        except Exception as exc:
            logger.error(f"Failed to generate {cid}: {exc}")
            results[cid] = {"error": str(exc)}

    return results


def validate(curriculum_dir: str) -> dict:
    """Validate the structure of a generated curriculum.

    Args:
        curriculum_dir: Path to the curriculum directory.

    Returns:
        Validation result dictionary.
    """
    path = Path(curriculum_dir)
    if not path.exists():
        return {"error": f"Directory does not exist: {curriculum_dir}"}

    return validate_structure(path)


def list_curricula() -> list[dict[str, str]]:
    """List all available curriculum configurations.

    Returns:
        List of dictionaries with id, title, audience, total_files.
    """
    return [
        {
            "id": config.id,
            "title": config.title,
            "audience": config.audience,
            "total_files": config.total_files,
            "type": "age-level" if config.id in AGE_LEVEL_CURRICULA else "domain",
        }
        for config in ALL_CURRICULA.values()
    ]


def main(argv: Optional[list[str]] = None) -> int:
    """CLI entry point.

    Args:
        argv: Command-line arguments (defaults to sys.argv).

    Returns:
        Exit code (0 for success).
    """
    parser = argparse.ArgumentParser(
        prog="course_generator",
        description="Generate Active Inference curricula",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # generate command
    gen_parser = subparsers.add_parser("generate", help="Generate a curriculum")
    gen_parser.add_argument(
        "curriculum_id",
        choices=list(ALL_CURRICULA.keys()) + ["all"],
        help="Curriculum ID or 'all'",
    )
    gen_parser.add_argument(
        "--output", "-o", type=Path, default=None,
        help="Output directory",
    )
    gen_parser.add_argument(
        "--llm", action="store_true",
        help="Use Ollama LLM for content enrichment",
    )
    gen_parser.add_argument(
        "--model", default="llama3.2",
        help="Ollama model name (default: llama3.2)",
    )
    gen_parser.add_argument(
        "--overwrite", action="store_true",
        help="Overwrite existing files",
    )

    # list command
    subparsers.add_parser("list", help="List available curricula")

    # validate command
    val_parser = subparsers.add_parser("validate", help="Validate a curriculum")
    val_parser.add_argument(
        "directory", type=Path,
        help="Path to curriculum directory",
    )

    args = parser.parse_args(argv)

    # Set up logging
    setup_logging()

    if args.command == "list":
        for info in list_curricula():
            print(
                f"  [{info['type']:>9}] {info['id']:<35} "
                f"{info['title']:<45} ~{info['total_files']} files"
            )
        return 0

    elif args.command == "generate":
        if args.curriculum_id == "all":
            results = generate_all(
                args.output, use_llm=args.llm,
                model=args.model, overwrite=args.overwrite,
            )
            total = sum(r.get("files_created", 0) for r in results.values())
            print(f"\nGenerated {total} files across {len(results)} curricula")
        else:
            stats = generate(
                args.curriculum_id, args.output,
                use_llm=args.llm, model=args.model,
                overwrite=args.overwrite,
            )
            print(f"\nGenerated {stats.get('files_created', 0)} files")
        return 0

    elif args.command == "validate":
        result = validate(str(args.directory))
        if "error" in result:
            print(f"Error: {result['error']}")
            return 1
        print(f"Present: {len(result.get('present', []))}")
        print(f"Missing: {len(result.get('missing', []))}")
        for m in result.get("missing", []):
            print(f"  MISSING: {m}")
        return 0 if not result.get("missing") else 1

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
