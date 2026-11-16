#!/usr/bin/env python3
"""Active Inference Institute Course Publishing Pipeline.

Top-level orchestrator that reads publish.toml and drives the full generation
and publishing pipeline for all configured courses.

Usage:
    python publish.py [OPTIONS]

Options:
    --dry-run           Show what would be generated without generating
    --override-formats  Comma-separated formats to override publish.toml
    --course COURSE     Override to process only this course ID
    --skip-clear        Skip clearing existing generation and publication outputs
    --no-website        Skip website generation
    --skip-labs         Skip lab rendering
    --generate-dashboards  Generate interactive dashboards
    --publish-only      Re-publish existing outputs without regenerating
    --verbose           Enable verbose output

Examples:
    python publish.py                              # Full pipeline per publish.toml
    python publish.py --dry-run                    # Preview what would be generated
    python publish.py --course ai-philosophy       # Only one course
    python publish.py --override-formats txt,md    # Quick text-only generation
    python publish.py --publish-only               # Re-publish without regenerating
"""

import argparse
import logging
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # Fallback for older Python
    except ImportError:
        print(
            "ERROR: Python 3.11+ required, or install 'tomli' package.", file=sys.stderr
        )
        sys.exit(1)


sys.path.insert(0, str(Path(__file__).resolve().parent / "software"))
from src.batch_processing.config import AVAILABLE_FORMATS, COURSE_REGISTRY
from src.batch_processing.utils import find_modules_for_course


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_config(config_path: Path) -> dict:
    """Load and parse publish.toml configuration.

    Args:
        config_path: Path to the publish.toml file

    Returns:
        Parsed configuration dictionary
    """
    if not config_path.exists():
        logger.error(f"Configuration file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "rb") as f:
        return tomllib.load(f)


def get_enabled_formats(config: dict) -> list:
    """Extract enabled output formats from config.

    Args:
        config: Parsed publish.toml config

    Returns:
        List of enabled format strings
    """
    formats_section = config.get("formats", {})
    return [fmt for fmt, enabled in formats_section.items() if enabled]


def get_enabled_courses(config: dict) -> list:
    """Extract enabled course IDs from config.

    Args:
        config: Parsed publish.toml config

    Returns:
        List of enabled course ID strings
    """
    courses_section = config.get("courses", {})
    return [course for course, enabled in courses_section.items() if enabled]


def _validate_selection(courses: list[str], formats: list[str] | None = None) -> bool:
    """Reject the entire selection before any pipeline side effects."""
    valid = True
    if not courses:
        logger.error("No courses selected")
        valid = False
    invalid_courses = [course for course in courses if course not in COURSE_REGISTRY]
    if invalid_courses:
        logger.error("Unknown course IDs: %r", invalid_courses)
        valid = False

    if formats is not None:
        if not formats:
            logger.error("No output formats selected")
            valid = False
        invalid_formats = [fmt for fmt in formats if fmt not in AVAILABLE_FORMATS]
        if invalid_formats:
            logger.error("Unknown output formats: %r", invalid_formats)
            valid = False
    return valid


def _is_authored_markdown(
    path: Path, generated_markdown: set[str] | None = None
) -> bool:
    """Treat Markdown without registry-declared generated ownership as authored."""
    return path.suffix.lower() in {".md", ".markdown"} and (
        generated_markdown is None or path.name not in generated_markdown
    )


def _clean_generated_destination(
    destination: Path, generated_markdown: set[str] | None = None
) -> None:
    """Remove payload files only inside a discovered generated destination.

    Keep authored Markdown, hidden entries and directory identities. In particular,
    never recursively remove a selected course, unit, module or static tree.
    """
    for path in destination.rglob("*"):
        if any(part.startswith(".") for part in path.relative_to(destination).parts):
            continue
        if path.is_file() and not _is_authored_markdown(path, generated_markdown):
            path.unlink()


def run_youtube_scaffold(repo_root: Path, dry_run: bool = False) -> bool:
    """Scaffold YouTube courses with real transcripts before generation.

    Ensures module.md files contain actual transcript text rather than
    template placeholders. Uses --force-scaffold to overwrite any stale
    module.md files with real transcript content.

    Args:
        repo_root: Path to repository root
        dry_run: If True, log what would happen without executing

    Returns:
        True if scaffolding succeeded, False otherwise
    """
    logger.info("Pre-generation: scaffolding YouTube transcripts...")

    if dry_run:
        logger.info(
            "  [DRY RUN] Would scaffold YouTube module.md files with real transcripts"
        )
        return True

    cmd = [
        "uv",
        "run",
        "python",
        str(repo_root / "software" / "scripts" / "render_youtube_courses.py"),
        "--force-scaffold",
        "--skip-render",
        "--skip-whisper",
    ]

    result = subprocess.run(cmd, cwd=str(repo_root / "software"))
    if result.returncode != 0:
        logger.error("YouTube scaffold failed")
        return False

    logger.info("YouTube scaffold complete — real transcripts injected")
    return True


def run_generation(
    repo_root: Path,
    courses: list,
    formats: list,
    dry_run: bool = False,
    skip_clear: bool = False,
    no_website: bool = False,
    skip_labs: bool = False,
) -> bool:
    """Run the generation pipeline for specified courses and formats.

    Args:
        repo_root: Path to repository root
        courses: List of course IDs to process
        formats: List of output format strings
        dry_run: If True, show what would be generated
        skip_clear: If True, don't clear outputs first
        no_website: If True, skip website generation
        skip_labs: If True, skip lab rendering

    Returns:
        True if generation succeeded, False otherwise
    """
    if not _validate_selection(courses, formats):
        return False

    for course in courses:
        cmd = [
            "uv",
            "run",
            "python",
            str(repo_root / "software" / "scripts" / "generate_all_outputs.py"),
            "--course",
            course,
            "--formats",
            ",".join(formats),
        ]

        if skip_clear:
            cmd.append("--skip-clear")
        if no_website:
            cmd.append("--no-website")
        if skip_labs:
            cmd.append("--skip-labs")

        logger.info(
            f"{'[DRY RUN] ' if dry_run else ''}Generating {course}: {', '.join(formats)}"
        )
        if not dry_run:
            result = subprocess.run(cmd, cwd=str(repo_root / "software"))

            if result.returncode != 0:
                logger.error(f"Generation failed for {course}")
                return False

        # Only clear on first course run
        skip_clear = True

    return True


def run_publish(
    repo_root: Path,
    courses: list,
    output_dir: str,
    dry_run: bool = False,
    clean_before_publish: bool = True,
    skip_clear: bool = False,
) -> bool:
    """Copy generated outputs to the published directory.

    Args:
        repo_root: Path to repository root
        courses: List of course IDs to process
        output_dir: Name of the output directory
        dry_run: If True, show what would be published
        clean_before_publish: If True, clean selected generated destinations first
        skip_clear: If True, retain old generated artifacts regardless of config

    Returns:
        True if publishing succeeded, False otherwise
    """
    if not _validate_selection(courses):
        return False

    published_path = repo_root / output_dir
    if not dry_run:
        published_path.mkdir(parents=True, exist_ok=True)
    clean = clean_before_publish and not skip_clear

    total_copied = 0
    for course_id in courses:
        reg = COURSE_REGISTRY[course_id]
        course_path = repo_root / reg["rel_path"]

        if not course_path.exists():
            logger.warning(f"Course path not found: {course_path}")
            continue

        course_pub = published_path / course_id
        if not dry_run:
            course_pub.mkdir(parents=True, exist_ok=True)

        # Copy module outputs
        modules = find_modules_for_course(course_path, course_id)
        content_names = {Path(name).name for name in reg.get("content_files", [])}

        if clean:
            if dry_run:
                logger.info(
                    "  [DRY RUN] Would clean generated destinations for %s", course_id
                )
            else:
                # Discover existing publication modules too, so removed source
                # modules do not leave stale generated files behind.
                for module_pub in find_modules_for_course(course_pub, course_id):
                    generated_markdown = content_names | {
                        f"{module_pub.name}-{name}" for name in content_names
                    }
                    _clean_generated_destination(module_pub, generated_markdown)
                for static_dir in reg.get("static_dirs", []):
                    _clean_generated_destination(course_pub / static_dir)

        for module_dir in modules:
            output_dir_path = module_dir / "output"
            if not output_dir_path.exists():
                continue

            # For two-level courses (unit_glob), include parent (unit) name
            # to avoid collisions (e.g. youtube/bookstreams/01_video)
            if module_dir.parent != course_path:
                module_pub = course_pub / module_dir.parent.name / module_dir.name
            else:
                module_pub = course_pub / module_dir.name
            generated_markdown = content_names | {
                f"{module_dir.name}-{name}" for name in content_names
            }
            if not dry_run:
                module_pub.mkdir(parents=True, exist_ok=True)

            if dry_run:
                file_count = sum(1 for _ in output_dir_path.rglob("*") if _.is_file())
                logger.info(
                    f"  Would copy {file_count} files from {module_dir.name}/output/"
                )
            else:
                for f in output_dir_path.rglob("*"):
                    if f.is_file():
                        dest = module_pub / f.relative_to(output_dir_path)
                        if dest.exists() and _is_authored_markdown(
                            dest, generated_markdown
                        ):
                            continue
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(f, dest)
                        total_copied += 1

            # Copy dashboard.html if present
            dashboard = module_dir / "dashboard.html"
            if dashboard.exists():
                if not dry_run:
                    shutil.copy2(dashboard, module_pub / "dashboard.html")
                    total_copied += 1

        logger.info(f"  {reg['display_name']}: published {len(modules)} modules")

        # Copy static directories if configured
        static_dirs = reg.get("static_dirs", [])
        for static_dir in static_dirs:
            # static_dir is relative to course root (from config)
            # e.g. "04_computer_science/src/active_inference"
            source_dir = course_path / static_dir

            if not source_dir.exists():
                logger.warning(f"Static dir not found: {source_dir}")
                continue

            # Destination preserves structure relative to course
            dest = course_pub / static_dir

            if dry_run:
                file_count = sum(1 for _ in source_dir.rglob("*") if _.is_file())
                logger.info(
                    f"  Would copy static dir {static_dir} ({file_count} files)"
                )
            else:
                dest.mkdir(parents=True, exist_ok=True)
                created_files = 0
                for source in source_dir.rglob("*"):
                    target = dest / source.relative_to(source_dir)
                    if source.is_dir():
                        target.mkdir(parents=True, exist_ok=True)
                    elif source.is_file():
                        if target.exists() and _is_authored_markdown(target):
                            continue
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(source, target)
                        created_files += 1
                total_copied += created_files
                logger.info(
                    f"  Copied static dir: {static_dir} ({created_files} files)"
                )

    if not dry_run:
        logger.info(f"Published {total_copied} files to {published_path}")
    return True


def main() -> int:
    """Run the full publish pipeline."""
    parser = argparse.ArgumentParser(
        description="Active Inference Institute Course Publishing Pipeline"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview without generating"
    )
    parser.add_argument(
        "--override-formats", type=str, help="Comma-separated format override"
    )
    parser.add_argument("--course", type=str, help="Process only this course ID")
    parser.add_argument(
        "--skip-clear", action="store_true", help="Skip clearing outputs"
    )
    parser.add_argument(
        "--no-website", action="store_true", help="Skip website generation"
    )
    parser.add_argument("--skip-labs", action="store_true", help="Skip lab rendering")
    parser.add_argument(
        "--generate-dashboards",
        action="store_true",
        help="Regenerate interactive dashboards",
    )
    parser.add_argument(
        "--publish-only",
        action="store_true",
        help="Re-publish existing outputs without regenerating",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    repo_root = Path(__file__).parent
    config = load_config(repo_root / "publish.toml")

    # Verbose: CLI flag or toml config option
    if args.verbose or config.get("options", {}).get("verbose", False):
        logging.getLogger().setLevel(logging.DEBUG)

    # Determine courses and formats
    if args.course is not None:
        courses = [args.course]
    else:
        courses = get_enabled_courses(config)

    if args.override_formats is not None:
        formats = [f.strip().lower() for f in args.override_formats.split(",")]
    else:
        formats = get_enabled_formats(config)

    if not _validate_selection(courses, formats):
        return 1

    output_dir = config.get("general", {}).get("output_dir", "published")
    options = config.get("options", {})

    # CLI flags override config options
    no_website = args.no_website or not options.get("generate_website", True)
    skip_labs = args.skip_labs or options.get("skip_labs", False)
    generate_dashboards = args.generate_dashboards or options.get(
        "generate_dashboards", False
    )

    logger.info("=" * 60)
    logger.info("Active Inference Institute — Course Publishing Pipeline")
    logger.info(f"Courses: {', '.join(courses)}")
    logger.info(f"Formats: {', '.join(formats)}")
    logger.info(f"Output:  {output_dir}/")
    logger.info("=" * 60)

    # Skip generation if --publish-only
    if not args.publish_only:
        # Step 0 (optional): Generate dashboards
        if generate_dashboards and not args.dry_run:
            logger.info("Generating interactive dashboards...")
            dash_script = repo_root / "software" / "scripts" / "generate_dashboards.py"
            if dash_script.exists():
                dash_cmd = ["uv", "run", "python", str(dash_script)]
                if args.course:
                    dash_cmd.extend(["--course", args.course])
                result = subprocess.run(dash_cmd, cwd=str(repo_root / "software"))
                if result.returncode != 0:
                    logger.warning("Dashboard generation had errors (continuing)")
            else:
                logger.warning(f"Dashboard script not found: {dash_script}")

        # Step 0.5: Scaffold YouTube transcripts (if youtube course is being published)
        if "youtube" in courses:
            scaffold_ok = run_youtube_scaffold(repo_root, dry_run=args.dry_run)
            if not scaffold_ok:
                logger.warning(
                    "YouTube scaffold had errors (continuing with generation)"
                )

        # Step 1: Generate outputs
        success = run_generation(
            repo_root,
            courses,
            formats,
            dry_run=args.dry_run,
            skip_clear=args.skip_clear,
            no_website=no_website,
            skip_labs=skip_labs,
        )

        if not success:
            logger.error("Generation failed. Aborting publish.")
            return 1
    else:
        logger.info("--publish-only: skipping generation, copying existing outputs")

    # Step 2: Publish (copy to output directory)

    success = run_publish(
        repo_root,
        courses,
        output_dir,
        dry_run=args.dry_run,
        clean_before_publish=config.get("general", {}).get("clean_before_publish", True),
        skip_clear=args.skip_clear,
    )

    if not success:
        return 1

    logger.info("=" * 60)
    logger.info("Publishing complete!" if not args.dry_run else "Dry run complete!")
    logger.info("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
