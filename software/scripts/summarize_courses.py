#!/usr/bin/env python3
"""Generate 1-page summaries for courses using LLM.

Reads course module content and generates a concise summary of:
- What the course is about
- Target audience
- Key learning outcomes
"""

import argparse
import sys
from pathlib import Path

# Add software/ to path
software_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(software_dir))

from src.batch_processing.config import COURSE_REGISTRY  # noqa: E402
from src.llm import OllamaClient  # noqa: E402
from src.content_processing.labs import parse_module  # noqa: E402

DEFAULT_BASE = Path(__file__).resolve().parent.parent.parent / "course_development"

SUMMARY_PROMPT = """
You are an expert curriculum designer.
Analyze the following course modules and write a 1-PAGE summary (Markdown).

Course: {course_name}
Modules:
{module_summaries}

Your summary MUST include:
1. **Course Overview**: What is this course about?
2. **Target Audience**: Who is this for?
3. **What You Will Learn**: Key outcomes.
4. **Structure**: Brief mention of the progression.

Keep it engaging and professional.
"""


def get_course_modules(base: Path, course_key: str) -> list[Path]:
    """Get all module directories for a course."""
    # This assumes standard structure: course_dir/module_dir/module.md
    # COURSE_REGISTRY maps keys to directory names, but structure varies
    # We'll use a heuristic: find module.md files where path contains course key parts

    # Simplified search strategy: look for directories matching registry entry
    # But registry entries are just dicts. Use batch_processing logic if possible
    # Or just search base/COURSE_REGISTRY[course_key]

    # Actually, allow base search restricted by course info
    return sorted([m.parent for m in base.rglob("module.md") if course_key in str(m)])


def generate_summary(course_key: str, base: Path, client: OllamaClient, output_dir: Path):
    print(f"Summarizing {course_key}...")

    # 1. Gather content
    reg_entry = COURSE_REGISTRY.get(course_key, {})
    rel_path = reg_entry.get("rel_path")

    course_path = None
    if rel_path:
        # COURSE_REGISTRY paths are relative to repo root
        repo_root = base.parent
        course_path = repo_root / rel_path

    if not course_path or not course_path.exists():
        # Fallback search in base
        found = False
        for p in base.iterdir():
            if p.is_dir() and course_key in p.name:
                course_path = p
                found = True
                break
        if not found:
            print(f"Could not find directory for {course_key}")
            return

    module_files = sorted(course_path.rglob("module.md"))
    if not module_files:
        print("No modules found.")
        return

    module_texts = []
    for md_file in module_files:
        data = parse_module(md_file.parent)
        mod_num = md_file.parent.name
        title = data.get("title", "Unknown")
        overview = data.get("overview", "")[:500]  # Truncate
        module_texts.append(f"- Module {mod_num}: {title}\n  Overview: {overview}...")

    context = "\n".join(module_texts)

    # 2. Generate
    prompt = SUMMARY_PROMPT.format(course_name=course_key.upper(), module_summaries=context)

    try:
        summary = client.generate(prompt)

        # 3. Save
        out_file = output_dir / f"{course_key}_summary.md"
        out_file.write_text(summary, encoding="utf-8")
        print(f"Saved summary to {out_file}")
    except Exception as e:
        print(f"Error generating summary: {e}")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Generate 1-page course summaries via LLM")
    parser.add_argument(
        "--course",
        choices=list(COURSE_REGISTRY.keys()) + ["all"],
        required=True,
        help="Target course or 'all'",
    )
    parser.add_argument("--base", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--output", type=Path, default=Path("published/summaries"))
    parser.add_argument("--model", help="Ollama model override")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    args.output.mkdir(exist_ok=True)

    client = OllamaClient(model=args.model) if args.model else OllamaClient()

    if not client.is_available():
        print("Error: Ollama is not available. Please run 'ollama serve'.")
        sys.exit(1)

    courses = [args.course] if args.course != "all" else list(COURSE_REGISTRY.keys())

    for course in courses:
        generate_summary(course, args.base, client, args.output)


if __name__ == "__main__":
    main()
