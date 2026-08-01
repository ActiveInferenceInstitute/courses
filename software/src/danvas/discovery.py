"""Course discovery and module scanning for Danvas.

Reads the ``COURSE_REGISTRY`` from ``batch_processing.config`` when
available; otherwise falls back to directory scanning within the
``course_development/`` tree.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from ..batch_processing.logging_config import get_logger
except Exception:
    import logging

    def get_logger(name: str) -> logging.Logger:
        """Fallback logger factory."""
        _logger = logging.getLogger(name)
        if not _logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))
            _logger.addHandler(handler)
            _logger.setLevel(logging.INFO)
        return _logger


logger = get_logger("danvas.discovery")


# ──────────────────────────────────────────────────────────────────────────────
# Course discovery
# ──────────────────────────────────────────────────────────────────────────────


def discover_courses(repo_root: Path) -> List[Dict[str, Any]]:
    """Discover courses from the repository's ``course_development/`` tree.

    Reads the ``COURSE_REGISTRY`` from ``batch_processing.config`` when
    available; otherwise falls back to directory scanning.

    The registry stores each course's path in ``rel_path`` (relative to
    ``repo_root``) and its display title in ``display_name``.

    Args:
        repo_root: Root of the courses repository.

    Returns:
        List of dicts, each with at least ``id``, ``title``, ``path``, and
        ``module_count``.
    """
    courses: List[Dict[str, Any]] = []

    # Try the registry first
    registry: Optional[Dict[str, Dict[str, Any]]] = None
    try:
        from ..batch_processing import config as bp_config

        registry = getattr(bp_config, "COURSE_REGISTRY", None)
    except Exception:
        pass

    dev_root = repo_root / "course_development"
    if not dev_root.exists():
        logger.warning("course_development/ not found at %s", repo_root)
        return courses

    if registry:
        for cid, reg in registry.items():
            # Use rel_path (e.g. "course_development/active_inference_101")
            rel_path = reg.get("rel_path", "")
            if rel_path:
                course_dir = repo_root / rel_path
            else:
                # Legacy fallback: try dir_name, then course id
                course_dir = dev_root / reg.get("dir_name", cid)

            if not course_dir.is_dir():
                continue

            modules = _count_modules(course_dir)
            courses.append(
                {
                    "id": cid,
                    "title": reg.get(
                        "display_name", reg.get("title", cid.replace("_", " ").title())
                    ),
                    "path": str(course_dir),
                    "module_count": modules,
                    "description": reg.get("description", ""),
                }
            )

    # Fallback: if the registry import failed or produced no results
    # (e.g. paths don't match this repo_root), scan the directory directly.
    if not courses:
        for child in sorted(dev_root.iterdir()):
            if child.is_dir() and not child.name.startswith("."):
                modules = _count_modules(child)
                courses.append(
                    {
                        "id": child.name,
                        "title": child.name.replace("_", " ").title(),
                        "path": str(child),
                        "module_count": modules,
                        "description": "",
                    }
                )

    logger.info("Discovered %d courses", len(courses))
    return courses


def get_course_by_id(course_id: str, repo_root: Path) -> Optional[Dict[str, Any]]:
    """Return a single course dict, or ``None``."""
    for c in discover_courses(repo_root):
        if c["id"] == course_id:
            return c
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Module scanning
# ──────────────────────────────────────────────────────────────────────────────


def get_course_modules(course_path: Path) -> List[Dict[str, Any]]:
    """List numbered module directories inside a course.

    Args:
        course_path: Absolute path to the course directory.

    Returns:
        Sorted list of dicts with ``number``, ``name``, ``path``, ``files``.
    """
    modules: List[Dict[str, Any]] = []
    if not course_path.is_dir():
        return modules

    for child in sorted(course_path.iterdir()):
        if child.is_dir() and not child.name.startswith("."):
            # Attempt to parse XX_name pattern
            parts = child.name.split("_", 1)
            num_str = parts[0]
            try:
                num = int(num_str)
            except ValueError:
                continue
            name = parts[1] if len(parts) > 1 else child.name
            files = [f.name for f in child.iterdir() if f.is_file()]
            modules.append(
                {
                    "number": num,
                    "name": name.replace("_", " ").title(),
                    "path": str(child),
                    "dir_name": child.name,
                    "files": files,
                }
            )

    modules.sort(key=lambda m: m["number"])
    return modules


def _count_modules(course_dir: Path) -> int:
    """Count numbered module sub-directories."""
    count = 0
    for child in course_dir.iterdir():
        if child.is_dir():
            parts = child.name.split("_", 1)
            try:
                int(parts[0])
                count += 1
            except ValueError:
                pass
    return count
