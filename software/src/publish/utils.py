"""Utility functions for the publish module."""

import hashlib
import json
import shutil
import os
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

from . import config
from ..batch_processing.utils import (
    find_modules_for_course, get_courses_to_process, require_contained,
)

logger = logging.getLogger(__name__)


def get_course_config(course_name: str) -> Dict[str, Any]:
    """Get configuration for a specific course.

    Args:
        course_name: Name of the course directory (e.g., 'biol-1')

    Returns:
        Dictionary with configuration options
    """
    return config.COURSE_CONFIGS.get(course_name, config.DEFAULT_CONFIG)


def clean_directory(path: Path, *, files: List[Path]) -> None:
    """Remove explicitly owned payloads, preserving guides and directory identities."""
    for file in files:
        require_contained(file, path)
        if file.exists() and not file.is_file():
            raise ValueError(f"Not a regular generated file: {file}")
    for file in files:
        if file.name not in ("README.md", "AGENTS.md") and file.is_file():
            file.unlink()


def copy_file(source: Path, destination: Path, *, root: Path) -> None:
    """Atomically replace one admitted payload without risking the previous bytes."""
    require_contained(destination, root)
    if not source.is_file():
        raise FileNotFoundError(source)
    if destination.name in ("README.md", "AGENTS.md") and destination.exists():
        if destination.is_file() and destination.read_bytes() == source.read_bytes():
            return
        raise ValueError(f"Refusing to replace authored guide: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
            temporary = Path(stream.name)
        shutil.copy2(source, temporary)
        os.replace(temporary, destination)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def copy_directory_contents(
    src: Path, dst: Path, exclude_patterns: Optional[List[str]] = None
) -> int:
    """Copy a directory, raising on failure rather than returning a success count."""
    if not src.is_dir():
        raise FileNotFoundError(src)
    excluded = config.EXCLUDE_PATTERNS if exclude_patterns is None else exclude_patterns
    files = [
        path for path in sorted(src.rglob("*")) if path.is_file()
        and not any(part.startswith(".") for part in path.relative_to(src).parts)
        and not any(path.match(pattern) for pattern in excluded)
    ]
    for source in files:
        require_contained(source, src)
        require_contained(dst / source.relative_to(src), dst)
    for source in files:
        copy_file(source, dst / source.relative_to(src), root=dst)
    return len(files)


# =============================================================================
# Flattening Functions (migrated from scripts/flatten_published.py)
# =============================================================================


_FLATTEN_CATEGORIES = {
    "assignments", "lab-protocols", "lecture-content", "study-guides",
    "pdf", "docx", "html", "txt", "md", "mp3",
}
_FLATTEN_RECEIPT_NAME = ".flatten-receipt.json"
_FLATTEN_RECEIPT_SCHEMA = "courses-publication-flatten/v1"


def _file_sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def _load_flatten_receipt(module_dir: Path) -> Dict[str, Dict[str, str]]:
    """Admit only our source-relative, uniquely owned flattened file bindings."""
    receipt_path = module_dir / _FLATTEN_RECEIPT_NAME
    require_contained(receipt_path, module_dir)
    if not receipt_path.exists():
        return {}
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if (
        not isinstance(receipt, dict)
        or receipt.get("schema") != _FLATTEN_RECEIPT_SCHEMA
        or not isinstance(receipt.get("artifacts"), dict)
    ):
        raise ValueError(f"Invalid flattened publication receipt: {receipt_path}")
    bindings = receipt["artifacts"]
    targets = set()
    for origin, binding in bindings.items():
        if not isinstance(origin, str) or not isinstance(binding, dict):
            raise ValueError(f"Invalid flattened publication binding: {receipt_path}")
        relative = Path(origin)
        name, digest = binding.get("path"), binding.get("sha256")
        if (
            len(relative.parts) < 2
            or relative.parts[0] not in _FLATTEN_CATEGORIES
            or relative.as_posix() != origin
            or any(part.startswith(".") for part in relative.parts)
            or not isinstance(name, str)
            or not name
            or Path(name).name != name
            or name.startswith(".")
            or name not in (relative.name, f"{relative.parts[0]}_{relative.name}")
            or name in ("README.md", "AGENTS.md")
            or name in targets
            or not isinstance(digest, str)
            or len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
        ):
            raise ValueError(f"Invalid flattened publication binding: {receipt_path}")
        require_contained(module_dir / relative, module_dir)
        require_contained(module_dir / name, module_dir)
        targets.add(name)
    return bindings


def _save_flatten_receipt(module_dir: Path, bindings: Dict[str, Dict[str, str]]) -> None:
    """Publish ownership atomically, using the same receipt pattern as rendering."""
    receipt_path = module_dir / _FLATTEN_RECEIPT_NAME
    require_contained(receipt_path, module_dir)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=module_dir, delete=False,
        ) as stream:
            temporary = Path(stream.name)
            json.dump(
                {"schema": _FLATTEN_RECEIPT_SCHEMA, "artifacts": bindings},
                stream, sort_keys=True,
            )
            stream.write("\n")
        os.replace(temporary, receipt_path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def flatten_module(module_dir: Path, dry_run: bool = False, verbose: bool = False) -> int:
    """Replace only byte-bound owned artifacts; foreign root files keep their bytes.

    Each generated category-relative source keeps its flattened identity across
    publications. An absent receipt, or a changed destination digest, never grants
    overwrite authority, even when a foreign file happens to match the new bytes.
    Admit every collision before moving any file or updating the hidden receipt.
    """
    bindings = _load_flatten_receipt(module_dir)
    claimed = {binding["path"]: origin for origin, binding in bindings.items()}
    moves = []
    for directory in sorted(module_dir.iterdir()):
        if not directory.is_dir() or directory.name not in _FLATTEN_CATEGORIES:
            continue
        for source in sorted(directory.rglob("*")):
            if (
                not source.is_file()
                or source.name in ("README.md", "AGENTS.md")
                or any(part.startswith(".") for part in source.relative_to(module_dir).parts)
            ):
                continue
            require_contained(source, module_dir)
            origin = source.relative_to(module_dir).as_posix()
            previous = bindings.get(origin)
            names = ([previous["path"]] if previous is not None else []) + [
                source.name, f"{directory.name}_{source.name}",
            ]
            for name in dict.fromkeys(names):
                target = module_dir / name
                require_contained(target, module_dir)
                if name in claimed and claimed[name] != origin:
                    continue
                if target.exists() and (
                    not target.is_file()
                    or previous is None
                    or previous["path"] != name
                    or _file_sha256(target) != previous["sha256"]
                ):
                    continue
                claimed[name] = origin
                bindings[origin] = {"path": name, "sha256": _file_sha256(source)}
                moves.append((source, target))
                break
            else:
                raise FileExistsError(
                    f"Ambiguous flattened payload: {module_dir / names[-1]}"
                )
    if moves and not dry_run:
        for source, target in moves:
            os.replace(source, target)
        _save_flatten_receipt(module_dir, bindings)
    return len(moves)


def flatten_published(
    published_dir: Path, skip_dirs: Optional[List[str]] = None,
    dry_run: bool = False, verbose: bool = False, *,
    courses: Optional[List[str]] = None, modules: Optional[List[Path]] = None,
) -> int:
    """Flatten selected modules while retaining their full course/unit identities."""
    if not published_dir.is_dir():
        raise FileNotFoundError(published_dir)
    if modules is None:
        course_dirs = (
            [published_dir / cid for cid in courses] if courses is not None
            else [p for p in sorted(published_dir.iterdir()) if p.is_dir() and not p.name.startswith(".")]
        )
        modules = [
            module for course in course_dirs
            for module in find_modules_for_course(course, course.name)
            if module.name not in (skip_dirs or [])
        ]
    for module in modules:
        require_contained(module, published_dir)
    return sum(flatten_module(module, dry_run, verbose) for module in modules)


def clean_published(published_dir: Path, *, destinations: List[Path]) -> None:
    """Clear only an explicitly supplied publication manifest."""
    clean_directory(published_dir, files=destinations)


# =============================================================================
# Copy Functions (migrated from scripts/publish_all.py)
# =============================================================================


def _course_paths(repo_root: Path, courses: Optional[List[str]]) -> List[tuple]:
    """Admit every selected course before copying any extras."""
    from ..batch_processing.config import COURSE_REGISTRY

    identities = [entry[2] for entry in get_courses_to_process("all")] if courses is None else courses
    entries = []
    for identity in identities:
        if identity not in COURSE_REGISTRY:
            raise ValueError(f"Unknown course: {identity}")
        meta = COURSE_REGISTRY[identity]
        path = repo_root / meta["rel_path"]
        require_contained(path, repo_root)
        if not path.is_dir():
            raise FileNotFoundError(path)
        entries.append((identity, path, meta))
    return entries


def copy_labs_and_dashboards(
    repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False,
    *, plans: Optional[List[dict]] = None, skip_labs: bool = False,
) -> int:
    """Copy selected lab sources/outputs and module-owned dashboards."""
    published = repo_root / config.PUBLISH_ROOT_NAME
    total = 0
    by_id = {plan["course_id"]: plan for plan in plans} if plans is not None else {}
    for identity, course, meta in _course_paths(repo_root, courses):
        plan = by_id.get(identity)
        modules = plan["modules"] if plan is not None else find_modules_for_course(course, identity)
        for module in modules:
            dashboard = module / "dashboard.html"
            if dashboard.is_file():
                require_contained(dashboard, course)
                copy_file(
                    dashboard, published / identity / module.relative_to(course) / dashboard.name,
                    root=published,
                )
                total += 1
        if skip_labs or (plan is not None and not plan.get("include_course_extras", True)):
            continue
        base = course / "course" if meta.get("has_course_subdir", False) else course
        labs = base / "labs"
        if plan is not None:
            # Generated lab files are already in the publication plan.
            sources = sorted({a["source"] for a in plan["artifacts"] if a["kind"] == "lab"})
        else:
            sources = sorted(p for p in labs.rglob("*") if p.is_file())
        for source in sources:
            if source.name in ("README.md", "AGENTS.md"):
                continue
            require_contained(source, course)
            copy_file(source, published / identity / "labs" / source.relative_to(labs), root=published)
            total += 1
    return total


def copy_slides(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int:
    total = 0
    published = repo_root / config.PUBLISH_ROOT_NAME
    for identity, course, _ in _course_paths(repo_root, courses):
        for source in sorted((course / "resources/slides").glob("*.pdf")):
            require_contained(source, course)
            copy_file(source, published / identity / "slides" / source.name, root=published)
            total += 1
    return total


def copy_slides_to_modules(
    repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False,
    *, selected_modules: Optional[Dict[str, List[Path]]] = None,
) -> int:
    """Copy slides by source-relative module identity; refuse ambiguous shared slides."""
    copies = []
    from ..module_organization.utils import get_module_number_from_path

    for identity, source_course, _ in _course_paths(repo_root, courses):
        modules = (
            selected_modules[identity] if selected_modules is not None
            else find_modules_for_course(source_course, identity)
        )
        for module in modules:
            number = get_module_number_from_path(module)
            unit_slides = module.parent / "resources/slides"
            slides = unit_slides if unit_slides.is_dir() else source_course / "resources/slides"
            matches = sorted(set(
                list(slides.glob(f"module-{number}-slides-*.pdf"))
                + list(slides.glob(f"Module {number:02d} - *.pdf"))
                + list(slides.glob(f"Module {number} - *.pdf"))
            ))
            if matches and slides == source_course / "resources/slides" and sum(
                get_module_number_from_path(other) == number
                for other in find_modules_for_course(source_course, identity)
            ) > 1:
                raise ValueError(f"Ambiguous course-wide slide number {number} in {identity}")
            require_contained(module, source_course)
            destination = repo_root / config.PUBLISH_ROOT_NAME / identity / module.relative_to(source_course)
            for source in matches:
                require_contained(source, source_course)
                require_contained(destination / source.name, repo_root / config.PUBLISH_ROOT_NAME)
                copies.append((source, destination / source.name))
    for source, target in copies:
        copy_file(source, target, root=repo_root / config.PUBLISH_ROOT_NAME)
    return len(copies)


def copy_exams(repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False) -> int:
    """Explicit exam export only; ordinary publication does not call this API."""
    total = 0
    published = repo_root / config.PUBLISH_ROOT_NAME
    for identity, course, meta in _course_paths(repo_root, courses):
        base = course / "course" if meta.get("has_course_subdir", False) else course
        exams = base / "exams"
        for source in sorted(exams.rglob("*")):
            if not source.is_file() or source.stem.endswith("_key") or source.name in ("README.md", "AGENTS.md"):
                continue
            require_contained(source, course)
            copy_file(source, published / identity / "exams" / source.relative_to(exams), root=published)
            total += 1
    return total


def copy_practice_tests(
    repo_root: Path, courses: Optional[List[str]] = None, verbose: bool = False,
    *, formats: Optional[List[str]] = None,
) -> int:
    from ..batch_processing.config import AVAILABLE_FORMATS
    from ..batch_processing.utils import get_formats_to_process

    active = get_formats_to_process(",".join(AVAILABLE_FORMATS if formats is None else formats))
    total = 0
    published = repo_root / config.PUBLISH_ROOT_NAME
    for identity, course, meta in _course_paths(repo_root, courses):
        base = course / "course" if meta.get("has_course_subdir", False) else course
        source_dir = base / "practice_tests"
        for source in sorted(source_dir.rglob("*")):
            if not source.is_file() or source.suffix.lstrip(".") not in active:
                continue
            if source.name in ("README.md", "AGENTS.md"):
                continue
            require_contained(source, course)
            copy_file(
                source, published / identity / "practice_tests" / source.relative_to(source_dir),
                root=published,
            )
            total += 1
    return total


# =============================================================================
# Category Reorganization Functions
# =============================================================================


def reorganize_to_categories(
    published_dir: Path, courses: Optional[List[str]] = None, verbose: bool = False,
    *, modules: Optional[List[Path]] = None,
) -> int:
    """Move category files without erasing their course/unit/module identities."""
    selected = [entry[2] for entry in get_courses_to_process("all")] if courses is None else courses
    total = 0
    for identity in selected:
        course = published_dir / identity
        if not course.is_dir():
            raise FileNotFoundError(course)
        selected_modules = (
            [module for module in modules if module.is_relative_to(course)]
            if modules is not None else find_modules_for_course(course, identity)
        )
        for module in selected_modules:
            relative = module.relative_to(course)
            for source in sorted(module.iterdir()):
                if not source.is_file() or source.name in ("README.md", "AGENTS.md"):
                    continue
                name = source.name.lower()
                category = (
                    "homework" if "questions" in name else
                    "module_keys" if "keys-to-success" in name else
                    "slides" if name.endswith(".pdf") and ("slides" in name or name.startswith("module ")) else
                    None
                )
                if category is None:
                    continue
                target = course / category / relative / source.name
                require_contained(source, published_dir)
                require_contained(target, published_dir)
                # This exact course/unit/module/category identity belongs to
                # the selected source. Replace atomically, never flatten its ID.
                copy_file(source, target, root=published_dir)
                source.unlink()
                total += 1
    return total
