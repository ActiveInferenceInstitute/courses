#!/usr/bin/env python3
"""Translate an entire course into a target language.

Recursively translates:
- module.md
- lab.md
- practice_quiz.md (attempts to preserve structure)

Outputs to a new directory: course_development/course_LANG/
"""

import argparse
import shutil
import sys
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY
from src.translation import translate_file

DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"


def translate_course(course_key: str, base: Path, lang: str, dry_run: bool, model: str = None, output_dir: Path = None):
    
    # Initialize client if not dry_run to fail early if offline
    from src.llm import OllamaClient
    client = None
    if not dry_run:
        client = OllamaClient(model=model) if model else OllamaClient()
        if not client.is_available():
            print("Error: Ollama is not available. Please run 'ollama serve'.")
            return

    print(f"Translating {course_key} to {lang} (model: {client.model if client else 'N/A'})...")
    
    # Locate course dir
    # Simplified logic: find dir matching registry key approximation or explicit path
    course_path = None
    # 1. Try registry path
    reg_path = COURSE_REGISTRY.get(course_key, {}).get("rel_path")
    if reg_path:
        # Check if reg_path is already absolute or relative to repo root
        # configured paths are relative to repo root, but base is course_development
        # so we need to be careful. 
        # Actually COURSE_REGISTRY paths are "course_development/..."
        # So if base is course_development, we need to strip that prefix or just use repo root logic.
        
        # Let's assume content acts on course_development as base.
        # If reg_path starts with course_development, we can relate it.
        
        repo_root = base.parent
        p = repo_root / reg_path
        if p.exists():
            course_path = p

    
    if not course_path:
        # Fallback search in base
        found = False
        for p in base.iterdir():
            if p.is_dir() and course_key in p.name:
                course_path = p
                found = True
                break
        if not found:
            print(f"Course directory not found for {course_key}")
            return

    if output_dir:
        # Use full language name if available, else code
        from src.translation.utils import get_language_name
        lang_name = get_language_name(lang).replace(" ", "_") # unexpected spaces safety
        target_root = output_dir / lang_name / "courses"
        target_dir = target_root / course_path.name
    else:
        target_root = course_path.parent
        target_dir = target_root / f"{course_path.name}_{lang}"

    print(f"Source: {course_path}")
    print(f"Target: {target_dir}")
    
    if dry_run:
        print("[Dry Run] Would duplicate and translate files...")
        return

    # Create target dir
    if target_dir.exists():
        print("Target directory exists. Updating/Overwriting...")
    else:
        # Copy structure first to preserve non-text assets (images, etc)
        # Use shutil.copytree with ignore to skip generated outputs if needed
        shutil.copytree(course_path, target_dir, dirs_exist_ok=True, 
                        ignore=shutil.ignore_patterns("output", "*.pdf", "__pycache__"))
        print("Copied directory structure.")

    # Translate MD files in place in the new directory
    for md_file in target_dir.rglob("*.md"):
        if "output" in md_file.parts:
            continue
            
        print(f"Translating {md_file.name}...")
        try:
            # We translate in place: read, translate, overwrite
            # Using translate_file usually produces _lang.md
            # Here we want to REPLACE the file content in the NEW directory
            # so the filename stays "module.md" (important for build scripts)
            
            # 1. Translate to temp file
            temp_out = translate_file(str(md_file), lang, client=client) # creates file_lang.md
            temp_path = Path(temp_out)
            
            # 2. Move temp file to original name (overwrite)
            temp_path.replace(md_file)
            
        except Exception as e:
            print(f"Failed to translate {md_file}: {e}")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Translate course to target language")
    parser.add_argument("--course", choices=list(COURSE_REGISTRY.keys()), required=True)
    parser.add_argument("--lang", required=True, help="Target language code (es, fr, de, etc.)")
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--model", help="Ollama model override")
    parser.add_argument("--output", type=Path, default=Path("published/translations"), help="Output directory base")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    translate_course(args.course, args.base, args.lang, args.dry_run, args.model, args.output)


if __name__ == "__main__":
    main()
