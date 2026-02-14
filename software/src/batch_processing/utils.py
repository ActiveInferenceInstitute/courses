"""Utility functions for batch processing."""

import logging
import re
from pathlib import Path
from typing import List, Optional, Dict, Any

from . import config

logger = logging.getLogger(__name__)


def prettify_name(name: str) -> str:
    """Prettify a directory name (e.g. 01_intro -> Intro)."""
    return re.sub(r"^\d+_", "", name).replace("_", " ").title()


def extract_course_info_from_path(file_path: Path, base: Path) -> Dict[str, str]:
    """Extract course, unit, and module info from a file path using COURSE_REGISTRY.

    Args:
        file_path: Path to the file (e.g., .../active_inference/01_philosophy/01_intro/questions.md)
        base: Base directory (e.g., .../course_development)

    Returns:
        Dictionary with keys:
        - course: Registry ID (e.g. "ai-philosophy") or folder name
        - course_name: Display name
        - unit: Unit name (or "Core" if none)
        - module_num: Module number/prefix (e.g. "01")
        - module_topic: Module topic (e.g. "Intro")
    """
    try:
        rel = file_path.relative_to(base)
    except ValueError:
        # Fallback if not relative to base
        logger.warning(f"File {file_path} is not relative to base {base}")
        return {
            "course": "unknown", "course_name": "Unknown",
            "unit": "Unknown", "module_num": "00", "module_topic": "Unknown"
        }

    # Identify course from Registry
    matched_key = None
    matched_meta = None
    course_rel_path = None

    for key, meta in config.COURSE_REGISTRY.items():
        meta_path = Path(meta["rel_path"])
        
        # Determine registry path relative to base
        # If meta_path includes "course_development", strip it if base ends with it
        # But base IS the root.
        # Check if meta_path is absolute or relative to repo root?
        # Config says relative to repo root.
        # If base is .../course_development, we need meta path relative to that.
        
        if "course_development" in meta_path.parts:
            try:
                c_path = meta_path.relative_to("course_development")
            except ValueError:
                c_path = meta_path
        else:
            c_path = meta_path

        if str(rel).startswith(str(c_path)):
            matched_key = key
            matched_meta = meta
            course_rel_path = c_path
            break

    if matched_key and course_rel_path:
        course = matched_key
        course_name = matched_meta["display_name"]
        
        try:
            inner = rel.relative_to(course_rel_path)
            parts = inner.parts
            
            if "unit_glob" in matched_meta:
                # Expecting unit/module/...
                if len(parts) >= 2:
                    unit = prettify_name(parts[0])
                    module = parts[1]
                else:
                    unit = "Core"
                    module = parts[0] if parts else "Unknown"
            else:
                # Expecting module/...
                unit = "Core"
                module = parts[0] if parts else "Unknown"
        except (ValueError, IndexError):
            unit = "Unknown"
            module = "Unknown"
            
        module_topic = prettify_name(module)
    else:
        # Fallback for paths not in registry
        parts = rel.parts
        if len(parts) > 1 and parts[0] == "domains":
            course = parts[1]
            if len(parts) > 3:
                unit = prettify_name(parts[2])
                module = parts[3]
            else:
                unit = "Unknown"
                module = parts[-2] if len(parts) >= 2 else "Unknown"
            course_name = prettify_name(course)
        elif len(parts) >= 3:
            course = parts[0]
            unit = prettify_name(parts[1])
            module = parts[2]
            course_name = prettify_name(course)
        else:
            course = parts[0] if parts else "unknown"
            unit = "Core"
            module = parts[1] if len(parts) > 1 else "Unknown"
            course_name = prettify_name(course)

        module_topic = prettify_name(module)

    return {
        "course": course,
        "course_name": course_name,
        "unit": unit,
        "module_num": module[:2],
        "module_topic": module_topic,
    }


def preprocess_lab_markdown(content: str) -> str:
    """Preprocess lab markdown to expand fill directives into rendered HTML blocks.
    
    Transforms raw template directives like {fill:textarea rows=8} into
    visible bordered response areas suitable for PDF/HTML rendering.
    Strips <!-- lab:... --> comment directives.

    Args:
        content: Raw markdown content with lab directives.

    Returns:
        Preprocessed markdown with fill directives expanded to HTML blocks.
    """
    # Replace {fill:textarea rows=N} with a bordered response box
    def textarea_replacement(match: re.Match) -> str:
        attrs = match.group(1) if match.group(1) else ""
        rows_match = re.search(r"rows=(\d+)", attrs)
        rows = int(rows_match.group(1)) if rows_match else 4
        # Convert rows to approximate pixel height (1 row ≈ 24px)
        height = max(rows * 24, 80)
        return (
            f'\n<div style="border: 1px solid #ccc; border-radius: 4px; '
            f'min-height: {height}px; padding: 8px; margin: 8px 0; '
            f'background-color: #fafafa;">'
            f'<em style="color: #999; font-size: 0.85em;">'
            f'Write your response here</em></div>\n'
        )

    content = re.sub(
        r"\{fill:textarea\s*(.*?)\}",
        textarea_replacement,
        content,
    )

    # Replace {fill:text} with inline input placeholder
    content = re.sub(
        r"\{fill:text\}",
        '<span style="border-bottom: 1px solid #999; '
        'display: inline-block; min-width: 200px;">&nbsp;</span>',
        content,
    )

    # Replace {fill:number} with inline number placeholder
    content = re.sub(
        r"\{fill:number\}",
        '<span style="border-bottom: 1px solid #999; '
        'display: inline-block; min-width: 80px;">&nbsp;</span>',
        content,
    )

    # Replace {fill:drawing ...} with drawing area
    def drawing_replacement(match: re.Match) -> str:
        attrs = match.group(1) if match.group(1) else ""
        height_match = re.search(r"height=(\d+)", attrs)
        height = height_match.group(1) if height_match else "200"
        return (
            f'\n<div style="border: 1px solid #ccc; border-radius: 4px; '
            f'min-height: {height}px; padding: 8px; margin: 8px 0; '
            f'background-color: #fafafa;">'
            f'<em style="color: #999; font-size: 0.85em;">'
            f'Drawing area</em></div>\n'
        )

    content = re.sub(
        r"\{fill:drawing\s*(.*?)\}",
        drawing_replacement,
        content,
    )

    # Replace standalone {fill} with text input placeholder
    content = re.sub(
        r"\{fill\}",
        '<span style="border-bottom: 1px solid #999; '
        'display: inline-block; min-width: 200px;">&nbsp;</span>',
        content,
    )

    # Strip <!-- lab:reflection --> and <!-- /lab:reflection --> comments
    content = re.sub(r"<!--\s*/?\s*lab:\w+\s*-->", "", content)

    logger.debug("Preprocessed lab markdown: expanded fill directives")
    return content


def find_markdown_files(directory: Path) -> List[Path]:
    """Find all Markdown files in a directory recursively.

    Args:
        directory: Directory to search

    Returns:
        List of Markdown file paths
    """
    markdown_files = []
    for pattern in ["*.md", "*.markdown"]:
        markdown_files.extend(directory.rglob(pattern))
    return sorted(markdown_files)


def find_audio_files(directory: Path) -> List[Path]:
    """Find all audio files in a directory recursively.

    Args:
        directory: Directory to search

    Returns:
        List of audio file paths
    """
    audio_files = []
    for pattern in ["*.mp3", "*.wav", "*.m4a", "*.flac", "*.ogg"]:
        audio_files.extend(directory.rglob(pattern))
    return sorted(audio_files)


def should_process_file(file_path: Path, skip_dirs: List[str]) -> bool:
    """Check if a file should be processed (not in skip directories).

    Args:
        file_path: Path to file
        skip_dirs: List of directory names to skip

    Returns:
        True if file should be processed, False otherwise
    """
    for part in file_path.parts:
        if part in skip_dirs:
            return False
    return True


def ensure_output_directory(output_dir: Path) -> None:
    """Ensure output directory exists.

    Args:
        output_dir: Path to output directory
    """
    output_dir.mkdir(parents=True, exist_ok=True)


def get_relative_output_path(source_file: Path, source_dir: Path, output_dir: Path) -> Path:
    """Get output path maintaining relative structure.

    Args:
        source_file: Source file path
        source_dir: Source directory path
        output_dir: Output directory path

    Returns:
        Output file path maintaining relative structure
    """
    relative_path = source_file.relative_to(source_dir)
    output_file = output_dir / relative_path
    return output_file


def get_courses_to_process(course_arg: str) -> List[tuple]:
    """Get list of courses to process based on argument.

    Args:
        course_arg: Course ID (e.g., "biol-1", "ai-philosophy") or "all"

    Returns:
        List of (relative_path, display_name, course_id) tuples
    """
    all_courses = [
        (reg["rel_path"], reg["display_name"], cid)
        for cid, reg in config.COURSE_REGISTRY.items()
    ]

    if course_arg == "all":
        return all_courses

    # Match by course ID in the registry
    if course_arg in config.COURSE_REGISTRY:
        reg = config.COURSE_REGISTRY[course_arg]
        return [(reg["rel_path"], reg["display_name"], course_arg)]

    # Fallback: match by path suffix
    return [(c, n, cid) for c, n, cid in all_courses if c.endswith(course_arg)]


def get_formats_to_process(formats_arg: str) -> List[str]:
    """Parse formats argument into list of valid formats.

    Args:
        formats_arg: Comma-separated format string or "all"

    Returns:
        List of valid format strings
    """
    if formats_arg == "all":
        return list(config.AVAILABLE_FORMATS)

    formats = [f.strip().lower() for f in formats_arg.split(",")]
    invalid = [f for f in formats if f not in config.AVAILABLE_FORMATS]
    if invalid:
        logger.warning(f"Unknown formats will be ignored: {invalid}")

    return [f for f in formats if f in config.AVAILABLE_FORMATS]


def find_modules_for_course(course_path: Path, course_id: str = None) -> List[Path]:
    """Discover module directories for a course using COURSE_REGISTRY metadata.

    Supports three patterns:
      - Legacy biology: course/module-*/
      - Active Inference core: XX_topic/ (flat)
      - Level-adapted / domain: unit_dir/XX_topic/ (two-level via unit_glob)

    Args:
        course_path: Absolute path to the course root directory
        course_id: Optional course registry ID for looking up metadata

    Returns:
        Sorted list of module directory paths
    """
    # Look up registry entry if course_id provided
    reg = None
    if course_id and course_id in config.COURSE_REGISTRY:
        reg = config.COURSE_REGISTRY[course_id]
    else:
        # Try to match by rel_path suffix
        for cid, r in config.COURSE_REGISTRY.items():
            if str(course_path).endswith(r["rel_path"]):
                reg = r
                course_id = cid
                break

    if reg:
        module_glob = reg.get("module_glob", "module-*")
        has_course_subdir = reg.get("has_course_subdir", True)
        unit_glob = reg.get("unit_glob", None)
    else:
        # Default: legacy biology pattern
        module_glob = "module-*"
        has_course_subdir = True
        unit_glob = None

    if has_course_subdir:
        search_dir = course_path / "course"
    else:
        search_dir = course_path

    if not search_dir.exists():
        return []

    import fnmatch

    # Two-level discovery: first find units, then modules inside each unit
    if unit_glob:
        units = sorted([
            d for d in search_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("__")
            and fnmatch.fnmatch(d.name, unit_glob)
        ])
        modules = []
        for unit_dir in units:
            unit_modules = sorted([
                d for d in unit_dir.iterdir()
                if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("__")
                and fnmatch.fnmatch(d.name, module_glob)
            ])
            modules.extend(unit_modules)
        return modules

    # Single-level discovery (original behavior)
    modules = sorted([
        d for d in search_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("__")
    ])

    # Filter by glob pattern
    modules = [m for m in modules if fnmatch.fnmatch(m.name, module_glob)]

    return modules


def get_course_id_from_path(course_rel_path: str) -> Optional[str]:
    """Look up the course registry ID from a relative path.

    Args:
        course_rel_path: Relative path like "course_development/active_inference/01_philosophy"

    Returns:
        Course ID string or None if not found
    """
    for cid, reg in config.COURSE_REGISTRY.items():
        if reg["rel_path"] == course_rel_path:
            return cid
    return None


def generate_dry_run_report(
    repo_root: Path,
    courses: List[tuple],
    formats: List[str],
    module_filter: Optional[int] = None,
    generate_website: bool = True,
    skip_labs: bool = False,
) -> str:
    """Generate a dry-run report of what would be processed.

    Args:
        repo_root: Path to repository root
        courses: List of (relative_path, display_name, course_id) tuples
        formats: List of format strings
        module_filter: Optional module number to filter
        generate_website: Whether website generation is enabled
        skip_labs: Whether lab rendering is skipped

    Returns:
        Report string describing what would be processed
    """
    from src.module_organization.utils import matches_module_number

    lines = [
        "",
        "=" * 60,
        "DRY RUN - Files that would be processed:",
        "=" * 60,
    ]

    for entry in courses:
        # Support both 2-tuple (legacy) and 3-tuple (new) formats
        if len(entry) >= 3:
            course_dir, course_name, course_id = entry[0], entry[1], entry[2]
        else:
            course_dir, course_name = entry[0], entry[1]
            course_id = get_course_id_from_path(course_dir)
        course_path = repo_root / course_dir
        if not course_path.exists():
            continue

        lines.append(f"\n{course_name}:")

        # Use registry-aware module discovery
        course_id = get_course_id_from_path(course_dir)
        modules = find_modules_for_course(course_path, course_id)

        if module_filter is not None:
            modules = [
                m for m in modules if matches_module_number(m.name, module_filter)
            ]

        for module_dir in modules:
            md_files = list(module_dir.glob("*.md"))
            assignment_files = (
                list((module_dir / "assignments").glob("*.md"))
                if (module_dir / "assignments").exists()
                else []
            )
            lines.append(
                f"  {module_dir.name}: {len(md_files)} root files, "
                f"{len(assignment_files)} assignments"
            )
            lines.append(f"    Would generate: {', '.join(formats)}")
            if generate_website:
                lines.append("    Would generate: website/index.html")

        # Check for syllabus using registry syllabus_location
        reg = config.COURSE_REGISTRY.get(course_id, {}) if course_id else {}
        syllabus_loc = reg.get("syllabus_location", "syllabus")
        syllabus_path = course_path / syllabus_loc
        if syllabus_path.exists() and syllabus_path.is_dir():
            syllabus_files = list(syllabus_path.glob("*.md"))
            lines.append(f"  Syllabus: {len(syllabus_files)} files")
            lines.append(f"    Would generate: {', '.join(formats)}")
        elif syllabus_path.exists() and syllabus_path.is_file():
            lines.append("  Syllabus: 1 file")
            lines.append(f"    Would generate: {', '.join(formats)}")
        elif (course_path / "syllabus.md").exists():
            # Fallback for courses without registry entry
            lines.append("  Syllabus: 1 file")
            lines.append(f"    Would generate: {', '.join(formats)}")

        if not skip_labs:
            # Check both course/labs (biology) and direct labs (Active Inference)
            labs_dir = course_path / "course" / "labs"
            if not labs_dir.exists():
                labs_dir = course_path / "labs"
            if labs_dir.exists():
                lab_files = list(labs_dir.glob("lab-*.md")) + list(labs_dir.glob("lab.md"))
                lab_formats = [f for f in formats if f in ("pdf", "html")]
                lines.append(f"  Labs: {len(lab_files)} files")
                lines.append(
                    f"    Would generate: "
                    f"{', '.join(lab_formats) if lab_formats else 'none (no compatible formats)'}"
                )

    lines.append("\nDry run complete. No files were generated.")
    return "\n".join(lines)
