"""Utility functions for batch processing."""

import logging
import re
from pathlib import Path
from typing import List, Optional, Dict

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
            "course": "unknown",
            "course_name": "Unknown",
            "unit": "Unknown",
            "module_num": "00",
            "module_topic": "Unknown",
        }

    # Identify course from Registry — pick the most specific match (longest rel_path)
    matched_key = None
    matched_meta = None
    course_rel_path = None

    candidates = []
    for key, meta in config.COURSE_REGISTRY.items():
        meta_path = Path(meta["rel_path"])

        # Determine registry path relative to base
        if "course_development" in meta_path.parts:
            try:
                c_path = meta_path.relative_to("course_development")
            except ValueError:
                c_path = meta_path
        else:
            c_path = meta_path

        if str(rel).startswith(str(c_path)):
            candidates.append((key, meta, c_path))

    # Pick the most specific match (longest rel_path)
    if candidates:
        candidates.sort(key=lambda x: len(str(x[2])), reverse=True)
        matched_key, matched_meta, course_rel_path = candidates[0]

    if matched_key and course_rel_path and matched_meta is not None:
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
            f"min-height: {height}px; padding: 8px; margin: 8px 0; "
            f'background-color: #fafafa;">'
            f'<em style="color: #999; font-size: 0.85em;">'
            f"Write your response here</em></div>\n"
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
            f"min-height: {height}px; padding: 8px; margin: 8px 0; "
            f'background-color: #fafafa;">'
            f'<em style="color: #999; font-size: 0.85em;">'
            f"Drawing area</em></div>\n"
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
    markdown_files: List[Path] = []
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
    audio_files: List[Path] = []
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
        (reg["rel_path"], reg["display_name"], cid) for cid, reg in config.COURSE_REGISTRY.items()
    ]

    if course_arg == "all":
        # Consolidated entries own their descendants during an all-course run.
        return [entry for entry in all_courses if not any(
            Path(entry[0]).is_relative_to(Path(other[0])) and entry[0] != other[0]
            for other in all_courses
        )]

    # Match by course ID in the registry
    if course_arg in config.COURSE_REGISTRY:
        reg = config.COURSE_REGISTRY[course_arg]
        return [(reg["rel_path"], reg["display_name"], course_arg)]

    raise ValueError(f"Unknown course: {course_arg}")


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
        raise ValueError(f"Unsupported or empty output formats: {invalid}")

    return list(dict.fromkeys(formats))


def find_modules_for_course(course_path: Path, course_id: Optional[str] = None) -> List[Path]:
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
    identity = course_id or resolve_course_id(course_path)
    reg = config.COURSE_REGISTRY.get(identity)

    if reg:
        module_glob = reg.get("module_glob", "module-*")
        has_course_subdir = reg.get("has_course_subdir", False)
        unit_glob = reg.get("unit_glob", None)
    else:
        # Unregistered temporary/legacy trees retain structural discovery.
        search = course_path / "course" if (course_path / "course").is_dir() else course_path
        if not search.is_dir():
            return []
        children = sorted(d for d in search.iterdir() if d.is_dir() and
                          re.match(r"^(?:module-\d+(?:-|$)|\d+_)", d.name))
        nested = [m for unit in children for m in sorted(unit.iterdir())
                  if m.is_dir() and re.match(r"^(?:module-\d+(?:-|$)|\d+_)", m.name)]
        return nested or children

    if has_course_subdir:
        search_dir = course_path / "course"
    else:
        search_dir = course_path

    if not search_dir.exists():
        return []

    import fnmatch

    # Two-level discovery: first find units, then modules inside each unit
    if unit_glob:
        units = sorted(
            [
                d
                for d in search_dir.iterdir()
                if d.is_dir()
                and not d.name.startswith(".")
                and not d.name.startswith("__")
                and fnmatch.fnmatch(d.name, unit_glob)
            ]
        )
        modules = []
        for unit_dir in units:
            unit_modules = sorted(
                [
                    d
                    for d in unit_dir.iterdir()
                    if d.is_dir()
                    and not d.name.startswith(".")
                    and not d.name.startswith("__")
                    and fnmatch.fnmatch(d.name, module_glob)
                ]
            )
            modules.extend(unit_modules)
        return modules

    # Single-level discovery (original behavior)
    modules = sorted(
        [
            d
            for d in search_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("__")
        ]
    )

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


def resolve_course_id(course_path: Path) -> Optional[str]:
    """Resolve a registry identity by complete path components, never a string prefix."""
    parts = course_path.parts
    matches = [(cid, reg) for cid, reg in config.COURSE_REGISTRY.items()
               if parts[-len(Path(reg["rel_path"]).parts):] == Path(reg["rel_path"]).parts]
    return max(matches, key=lambda item: len(Path(item[1]["rel_path"]).parts))[0] if matches else None


def select_modules(course_path: Path, course_id: Optional[str] = None,
                   module_filter: Optional[int] = None, unit_filter: Optional[str] = None,
                   max_module: Optional[int] = None) -> List[Path]:
    """Admit one numeric identity or an explicit unit; ambiguity is an error."""
    from ..module_organization.utils import get_module_number_from_path

    if not course_path.is_dir():
        raise ValueError(f"Course directory does not exist: {course_path}")
    for value in (module_filter, max_module):
        if value is not None and (type(value) is not int or value < 1):
            raise ValueError("Module selectors must be positive integers")
    modules = find_modules_for_course(course_path, course_id)
    if unit_filter is not None:
        unit = Path(unit_filter)
        if unit.is_absolute() or len(unit.parts) != 1 or unit.name in ("", ".", ".."):
            raise ValueError(f"Invalid unit selector: {unit_filter}")
        modules = [m for m in modules if m.parent.relative_to(course_path).as_posix() == unit_filter]
    if module_filter is not None:
        modules = [m for m in modules if get_module_number_from_path(m) == module_filter]
        if len(modules) > 1:
            choices = ", ".join(m.relative_to(course_path).as_posix() for m in modules)
            raise ValueError(f"Ambiguous module {module_filter}: {choices}; supply --unit")
    if max_module is not None:
        modules = [m for m in modules if get_module_number_from_path(m) <= max_module]
    if not modules:
        raise ValueError(f"No modules match selection in {course_path}")
    for module in modules:
        require_contained(module, course_path)
    return modules


def require_contained(path: Path, root: Path) -> Path:
    """Reject escaped or symlink-aliased inputs and destinations before mutation."""
    root = root.absolute()
    path = path.absolute()
    if not path.is_relative_to(root) or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes {root}: {path}")
    current = path
    while current != root:
        if current.is_symlink():
            raise ValueError(f"Symlink not admitted: {current}")
        current = current.parent
    return path


def parse_limits(values: List[str]) -> Dict[str, int]:
    """Admit every course:positive-integer limit or reject the whole request."""
    limits = {}
    for value in values:
        course, separator, number = value.partition(":")
        if not separator or course not in config.COURSE_REGISTRY or not number.isdecimal() or int(number) < 1:
            raise ValueError(f"Invalid course limit: {value}")
        if course in limits:
            raise ValueError(f"Duplicate course limit: {course}")
        limits[course] = int(number)
    return limits


def module_sources(module_path: Path, skip_labs: bool = False) -> List[tuple]:
    """Return unique authored (source, output category, basename) records."""
    candidates = set(module_path.glob("*.md"))
    for folder in ("assignments", "resources"):
        candidates.update((module_path / folder).glob("*.md"))
    candidates.update(f for f in find_markdown_files(module_path)
                      if f.name.startswith(config.SAMPLE_FILE_PREFIX)
                      and "output" not in f.relative_to(module_path).parts)
    records = []
    destinations = set()
    for source in sorted(candidates):
        if source.name.startswith(("README", "AGENTS")):
            continue
        name = source.name
        if "assignment" in name or source.parent.name == "assignments":
            category = "assignments"
        elif "lab-protocol" in name or name == "lab.md":
            category = "lab-protocols"
        elif "lecture-content" in name or name == "module.md":
            category = "lecture-content"
        elif ("study-guide" in name or name in ("questions.md", "practice_quiz.md")
              or any(pattern in name for pattern in config.CONTENT_TYPE_PATTERNS)):
            category = "study-guides"
        else:
            continue
        if skip_labs and category == "lab-protocols":
            continue
        require_contained(source, module_path)
        base = source.stem
        if not base.startswith((module_path.name, "module-")):
            base = f"{module_path.name}-{base}"
        if (category, base) in destinations:
            raise ValueError(f"Conflicting module output: {category}/{base}")
        destinations.add((category, base))
        records.append((source, category, base))
    return records


def module_artifacts(module_path: Path, formats: List[str], *, output_dir: Optional[Path] = None,
                     skip_labs: bool = False) -> List[dict]:
    formats = get_formats_to_process(",".join(formats))
    output = output_dir if output_dir is not None else module_path / "output"
    return [{"source": source, "destination": output / category / f"{base}.{fmt}",
             "kind": "module", "category": category, "format": fmt, "module": module_path}
            for source, category, base in module_sources(module_path, skip_labs)
            for fmt in formats]


def syllabus_artifacts(course_path: Path, formats: List[str], course_id: Optional[str] = None) -> List[dict]:
    reg = config.COURSE_REGISTRY.get(course_id or resolve_course_id(course_path), {})
    syllabus = course_path / reg.get("syllabus_location", "syllabus")
    # File-style syllabi are copied at publication, not rendered by this producer.
    if not syllabus.is_dir():
        return []
    return document_artifacts(syllabus, syllabus / "output", formats, "syllabus")


def document_artifacts(source_dir: Path, output_dir: Path, formats: List[str], kind: str) -> List[dict]:
    return [{"source": source, "destination": output_dir / f"{source.stem}.{fmt}",
             "kind": kind, "format": fmt}
            for source in sorted(source_dir.glob("*.md"))
            if not source.name.startswith(("README", "AGENTS")) for fmt in formats]


def lab_artifacts(course_path: Path, formats: List[str], course_id: Optional[str] = None,
                  max_lab: Optional[int] = None) -> List[dict]:
    if max_lab is not None and (type(max_lab) is not int or max_lab < 1):
        raise ValueError("Lab limit must be a positive integer")
    reg = config.COURSE_REGISTRY.get(course_id or resolve_course_id(course_path), {})
    base = course_path / "course" if reg.get("has_course_subdir", (course_path / "course").is_dir()) else course_path
    labs = base / "labs"
    records = []
    for source in sorted(labs.glob("*.md")):
        if source.name.startswith(("README", "AGENTS")):
            continue
        if max_lab is not None:
            match = re.match(r"lab-?(\d+)", source.stem, re.IGNORECASE)
            if match is None:
                raise ValueError(f"Cannot apply numeric lab limit to {source}")
            if int(match.group(1)) > max_lab:
                continue
        for fmt in formats:
            if fmt in ("pdf", "html"):
                records.append({"source": source, "destination": labs / "output" / fmt / f"{source.stem}.{fmt}",
                                "kind": "lab", "format": fmt})
    return records


def practice_artifacts(course_path: Path, formats: List[str]) -> List[dict]:
    if "pdf" not in formats:
        return []
    base = course_path / "course" if (course_path / "course").is_dir() else course_path
    source = base / "practice_tests"
    return document_artifacts(source, source / "output", ["pdf"], "practice")


def plan_course(course_path: Path, course_name: str, formats: List[str], *,
                course_id: Optional[str] = None, module_filter: Optional[int] = None,
                unit_filter: Optional[str] = None, max_module: Optional[int] = None,
                max_lab: Optional[int] = None, generate_website: bool = True,
                skip_labs: bool = False) -> dict:
    """One source-derived manifest for cleanup, generation and validation."""
    formats = get_formats_to_process(",".join(formats))
    modules = select_modules(course_path, course_id, module_filter, unit_filter, max_module)
    artifacts = []
    for module in modules:
        if not module_sources(module):
            raise ValueError(f"No authored renderable sources in {module}")
        artifacts.extend(module_artifacts(module, formats, skip_labs=skip_labs))
        if generate_website:
            artifacts.append({"source": module, "destination": module / "output/website/index.html",
                              "kind": "website", "format": "html", "module": module})
    if module_filter is None and unit_filter is None:
        artifacts.extend(syllabus_artifacts(course_path, formats, course_id))
        if not skip_labs:
            artifacts.extend(lab_artifacts(course_path, formats, course_id, max_lab))
        artifacts.extend(practice_artifacts(course_path, formats))
    destinations = set()
    for artifact in artifacts:
        require_contained(artifact["source"], course_path)
        destination = require_contained(artifact["destination"], course_path)
        if destination in destinations:
            raise ValueError(f"Conflicting generated destination: {destination}")
        if destination.exists() and not destination.is_file():
            raise ValueError(f"Generated destination is not a regular file: {destination}")
        destinations.add(destination)
    return {"course": course_name, "course_id": course_id, "path": course_path,
            "formats": formats, "modules": modules, "artifacts": artifacts,
            "include_course_extras": module_filter is None and unit_filter is None}


def plan_generation(repo_root: Path, courses: List[tuple], formats: List[str], *,
                    max_modules: Optional[dict] = None, max_labs: Optional[dict] = None,
                    **selection) -> List[dict]:
    if not courses:
        raise ValueError("No courses selected")
    ids = {entry[2] for entry in courses if len(entry) > 2}
    for limits in (max_modules or {}, max_labs or {}):
        if set(limits) - ids:
            raise ValueError(f"Limits name unselected courses: {sorted(set(limits) - ids)}")
    plans = []
    owned = set()
    for entry in courses:
        relative, name = entry[:2]
        cid = entry[2] if len(entry) > 2 else get_course_id_from_path(relative)
        path = require_contained(repo_root / relative, repo_root)
        plan = plan_course(path, name, formats, course_id=cid,
                           max_module=(max_modules or {}).get(cid), max_lab=(max_labs or {}).get(cid),
                           **selection)
        for artifact in plan["artifacts"]:
            if artifact["destination"] in owned:
                raise ValueError(f"Overlapping course selection: {artifact['destination']}")
            owned.add(artifact["destination"])
        plans.append(plan)
    return plans


def describe_generation(plans: List[dict]) -> str:
    return "\n".join(["DRY RUN - admitted generated destinations:"] +
                     [str(a["destination"]) for p in plans for a in p["artifacts"]] +
                     ["Dry run complete. No files were generated or removed."])


def generate_dry_run_report(repo_root: Path, courses: List[tuple], formats: List[str],
                            module_filter: Optional[int] = None, generate_website: bool = True,
                            skip_labs: bool = False, **selection) -> str:
    return describe_generation(plan_generation(repo_root, courses, formats,
        module_filter=module_filter, generate_website=generate_website, skip_labs=skip_labs, **selection))
