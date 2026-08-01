#!/usr/bin/env python3
"""Translate a published course into a target language.

Operates on the published output tree (e.g. published/active-inference/),
copies the full directory structure, and translates every .md file in-place
using the repo's OllamaClient and src.translation module.

Usage:
    uv run python scripts/translate_published.py --course active-inference --lang ru
    uv run python scripts/translate_published.py --course active-inference --lang ja --dry-run
"""

import argparse
import logging
import shutil
import sys
import time
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.translation import translate_file  # noqa: E402
from src.translation.config import SUPPORTED_LANGUAGES  # noqa: E402
from src.translation.utils import get_language_name  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_PUBLISHED = REPO_ROOT / "published"


def translate_published_course(
    course_name: str,
    lang: str,
    dry_run: bool = False,
    model: str = None,
    published_dir: Path = None,
):
    """Translate an entire published course tree into a target language.

    Args:
        course_name: Directory name under published/ (e.g. 'active-inference').
        lang: ISO language code (e.g. 'ru', 'ja', 'hi').
        dry_run: If True, log what would happen without executing.
        model: Optional Ollama model override.
        published_dir: Base published directory (default: published/).
    """
    if lang not in SUPPORTED_LANGUAGES:
        logger.error(
            f"Unsupported language code '{lang}'. Supported: {list(SUPPORTED_LANGUAGES.keys())}"
        )
        return False

    published_dir = published_dir or DEFAULT_PUBLISHED
    source_dir = published_dir / course_name

    if not source_dir.exists():
        logger.error(f"Published course not found: {source_dir}")
        return False

    lang_name = get_language_name(lang)
    target_dir = published_dir / "translations" / lang_name / course_name

    logger.info(f"{'[DRY RUN] ' if dry_run else ''}Translating '{course_name}' → {lang_name}")
    logger.info(f"  Source: {source_dir}")
    logger.info(f"  Target: {target_dir}")

    # Initialize Ollama client early to fail fast
    client = None
    if not dry_run:
        from src.llm import OllamaClient

        client = OllamaClient(model=model) if model else OllamaClient()
        if not client.is_available():
            logger.error("Ollama is not available. Please run 'ollama serve'.")
            return False
        logger.info(f"  Model:  {client.model}")

    # Discover all .md files in source
    md_files = sorted(source_dir.rglob("*.md"))
    logger.info(f"  Found {len(md_files)} markdown files to translate.")

    if dry_run:
        for md in md_files:
            rel = md.relative_to(source_dir)
            logger.info(f"  [DRY RUN] Would translate: {rel}")
        return True

    # Copy the full tree (preserving non-MD assets like HTML, CSS, images)
    if target_dir.exists():
        logger.info("  Target directory exists — updating in place.")
    else:
        logger.info("  Copying directory structure...")
        shutil.copytree(
            source_dir,
            target_dir,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"),
        )
        logger.info("  Directory structure copied.")

    # Translate each .md file in the target tree
    total = len(md_files)
    success_count = 0
    fail_count = 0
    start_time = time.time()

    for idx, source_md in enumerate(md_files, 1):
        rel_path = source_md.relative_to(source_dir)
        target_md = target_dir / rel_path

        logger.info(f"[{idx}/{total}] Translating {rel_path} ...")

        try:
            # translate_file writes to a _lang.md temp path; we move it back
            temp_out = translate_file(str(target_md), lang, client=client)
            temp_path = Path(temp_out)

            # Replace the original copy with the translated version
            temp_path.replace(target_md)
            success_count += 1

        except Exception as e:
            logger.error(f"  FAILED: {rel_path} — {e}")
            fail_count += 1

    elapsed = time.time() - start_time
    logger.info(
        f"\nTranslation complete: {success_count}/{total} succeeded, "
        f"{fail_count} failed. Elapsed: {elapsed:.0f}s"
    )
    return fail_count == 0


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Translate a published course into a target language"
    )
    parser.add_argument(
        "--course",
        default="active-inference",
        help="Published course directory name (default: active-inference)",
    )
    parser.add_argument(
        "--lang",
        required=True,
        choices=list(SUPPORTED_LANGUAGES.keys()),
        help="Target language code",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be translated without running LLM",
    )
    parser.add_argument(
        "--model",
        help="Ollama model override (default: gemma3:4b)",
    )
    parser.add_argument(
        "--published-dir",
        type=Path,
        default=DEFAULT_PUBLISHED,
        help="Path to published/ directory",
    )
    return parser.parse_args(argv)


def main():
    args = parse_args()
    ok = translate_published_course(
        course_name=args.course,
        lang=args.lang,
        dry_run=args.dry_run,
        model=args.model,
        published_dir=args.published_dir,
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
