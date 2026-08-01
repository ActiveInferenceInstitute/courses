#!/usr/bin/env python3
"""Translate YouTube playlists into a target language.

Recursively translates:
- module.md
- *.md files in video directories

Outputs to: published/translations/{LANGUAGE}/youtube/
"""

import argparse
import shutil
import sys
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.translation import translate_file  # noqa: E402
from src.translation.utils import get_language_name  # noqa: E402


def translate_youtube(
    playlist_name: str, lang: str, dry_run: bool, model: str = None, output_base: Path = None
):
    # Initialize client if not dry_run
    client = None
    if not dry_run:
        from src.llm import OllamaClient

        client = OllamaClient(model=model) if model else OllamaClient()
        if not client.is_available():
            print("Error: Ollama is not available. Please run 'ollama serve'.")
            return

    # Define source and target roots
    source_root = Path(__file__).resolve().parent.parent.parent / "course_development" / "youtube"

    if output_base:
        target_base = output_base
    else:
        target_base = Path(__file__).resolve().parent.parent.parent / "published" / "translations"

    lang_name = get_language_name(lang).replace(" ", "_")
    target_root = target_base / lang_name / "youtube"

    print(f"Translating YouTube content to {lang} ({lang_name})...")
    print(f"Source: {source_root}")
    print(f"Target: {target_root}")

    # Identify playlists to process
    playlists = []
    if playlist_name:
        p_path = source_root / playlist_name
        if not p_path.exists():
            print(f"Playlist not found: {playlist_name}")
            return
        playlists.append(p_path)
    else:
        for p in source_root.iterdir():
            if p.is_dir() and not p.name.startswith("."):  # Skip hidden and files
                playlists.append(p)

    print(f"Found {len(playlists)} playlists to process.")

    for playlist in playlists:
        print(f"\nProcessing Playlist: {playlist.name}")

        # Iterate through video directories in the playlist
        for video_dir in playlist.iterdir():
            if not video_dir.is_dir() or video_dir.name.startswith("."):
                continue

            # Construct target path
            target_video_dir = target_root / playlist.name / video_dir.name

            if dry_run:
                print(f"[Dry Run] Would translate {video_dir.name} -> {target_video_dir}")
                continue

            # Create target directory and copy assets
            if target_video_dir.exists():
                print(f"  Updating {target_video_dir}")
            else:
                print(f"  Creating {target_video_dir}")
                # Copy everything first, ignoring output/cache
                shutil.copytree(
                    video_dir,
                    target_video_dir,
                    dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("output", "*.pdf", "__pycache__", ".DS_Store"),
                )

            # Logic to find the "best" markdown file to be the module.md
            # 1. Look for output/lecture-content/*module.md
            # 2. Look for existing module.md

            source_file = None
            lecture_content_dir = video_dir / "output" / "lecture-content"

            if lecture_content_dir.exists():
                # Try to find exactly one markdown file ending in module.md or just any md
                md_candidates = list(lecture_content_dir.glob("*-module.md"))
                if not md_candidates:
                    md_candidates = list(lecture_content_dir.glob("*.md"))

                if md_candidates:
                    # Pick the first one (usually there's only one relevant one)
                    source_file = md_candidates[0]
                    print(f"    Found lecture content: {source_file.name}")

            # If no lecture content, fallback to root module.md
            if not source_file:
                root_module = video_dir / "module.md"
                if root_module.exists():
                    source_file = root_module
                    print("    Using root module.md")

            if source_file:
                # Target file is always module.md in the target dir
                target_file = target_video_dir / "module.md"

                print(f"    Translating {source_file.name} -> module.md...")
                try:
                    # Translate to temp file
                    temp_out = translate_file(str(source_file), lang, client=client)
                    temp_path = Path(temp_out)

                    # Move to target location
                    temp_path.replace(target_file)

                except Exception as e:
                    print(f"    Failed to translate {source_file.name}: {e}")


def parse_args():
    parser = argparse.ArgumentParser(description="Translate YouTube playlists to target language")
    parser.add_argument("--playlist", help="Specific playlist name to translate (optional)")
    parser.add_argument("--lang", required=True, help="Target language code (es, fr, de, etc.)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without translating")
    parser.add_argument("--model", help="Ollama model override")
    parser.add_argument(
        "--output", type=Path, help="Output directory base (default: published/translations)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    translate_youtube(args.playlist, args.lang, args.dry_run, args.model, args.output)


if __name__ == "__main__":
    main()
