"""Main logic for the publish module.

Module discovery is driven by COURSE_REGISTRY metadata (batch_processing.config).
This eliminates the legacy hardcoded ``course/module-*`` glob pattern and supports
all three course layouts:

  - Legacy biology courses   : course/module-*/  (has_course_subdir=True, module-* glob)
  - Active Inference flat    : XX_topic/          (has_course_subdir=False, [0-9][0-9]_*)
  - Level-adapted / domain   : unit/XX_topic/     (unit_glob present, two-level discovery)
"""

from pathlib import Path
from typing import Dict, Any, Optional
import logging

from . import config
from .utils import clean_directory, copy_file, get_course_config
from ..batch_processing.config import COURSE_REGISTRY
from ..batch_processing.utils import require_contained, resolve_course_id, select_modules

logger = logging.getLogger(__name__)




def publish_course(
    course_path: str, publish_root: Optional[str] = None, *,
    course_id: Optional[str] = None, plan: Optional[dict] = None, clean: bool = False,
) -> Dict[str, Any]:
    """Publish source-relative module identities, retaining every copy failure.

    Cleaning removes only files this invocation owns; directory identities,
    authored guides and unselected payloads are preserved.
    """
    course_dir = Path(course_path)
    identity = course_id or resolve_course_id(course_dir) or course_dir.name
    out_root = (
        Path(publish_root) if publish_root is not None
        else Path(__file__).resolve().parents[3] / config.PUBLISH_ROOT_NAME
    )
    published_course = out_root / identity
    result: Dict[str, Any] = {
        "course": identity, "modules_published": 0, "syllabus_files": 0,
        "total_files": 0, "modules": [], "errors": [],
    }
    try:
        if course_id is not None and course_id not in COURSE_REGISTRY:
            raise ValueError(f"Unknown course: {course_id}")
        require_contained(published_course, out_root)
        if plan is not None and plan["path"].resolve() != course_dir.resolve():
            raise ValueError("Publication plan belongs to a different course")
        if plan is not None and plan["course_id"] not in (None, identity):
            raise ValueError("Publication plan belongs to a different registry identity")
        modules = plan["modules"] if plan is not None else select_modules(course_dir, course_id)
        conf = get_course_config(identity)
        copies: list[tuple[Path, Path, str]] = []
        if plan is not None:
            for artifact in plan["artifacts"]:
                source = artifact["destination"]
                module = artifact.get("module")
                if module is not None:
                    relative = module.relative_to(course_dir)
                    target = published_course / relative / source.relative_to(module / "output")
                    group = relative.as_posix()
                elif artifact["kind"] == "syllabus":
                    target = published_course / "syllabus" / source.name
                    group = "syllabus"
                else:
                    target = published_course / source.relative_to(course_dir)
                    group = artifact["kind"]
                copies.append((source, target, group))
        else:
            for module in modules:
                relative = module.relative_to(course_dir)
                source_dir = module / conf["module_source_dir"]
                if not source_dir.is_dir():
                    result["errors"].append(f"Rendered output directory missing: {source_dir}")
                    continue
                for source in sorted(source_dir.rglob("*")):
                    if source.is_file() and source.name not in ("README.md", "AGENTS.md") and not any(
                        part.startswith(".") for part in source.relative_to(source_dir).parts
                    ):
                        copies.append((
                            source, published_course / relative / source.relative_to(source_dir),
                            relative.as_posix(),
                        ))
                for extra in conf.get("additional_module_dirs", []):
                    extra_dir = module / extra
                    if extra_dir.is_dir():
                        for source in sorted(extra_dir.rglob("*")):
                            if source.is_file():
                                copies.append((
                                    source, published_course / relative / extra / source.relative_to(extra_dir),
                                    relative.as_posix(),
                                ))
        reg = COURSE_REGISTRY.get(identity, {})
        syllabus = course_dir / reg.get("syllabus_location", "syllabus")
        whole_course = plan is None or plan.get("include_course_extras", True)
        if whole_course and conf.get("include_syllabus"):
            if syllabus.is_file():
                copies.append((syllabus, published_course / syllabus.name, "syllabus"))
            elif plan is None and (syllabus / conf["syllabus_source_dir"]).is_dir():
                source_dir = syllabus / conf["syllabus_source_dir"]
                for source in sorted(source_dir.rglob("*")):
                    if source.is_file():
                        copies.append((
                            source, published_course / "syllabus" / source.relative_to(source_dir),
                            "syllabus",
                        ))
        if not copies:
            result["errors"].append(f"No generated outputs to publish for {identity}")
        for source, destination, _ in copies:
            require_contained(source, course_dir)
            require_contained(destination, out_root)
            if not source.is_file() or source.stat().st_size == 0:
                result["errors"].append(f"Required publication input missing or empty: {source}")
        if result["errors"]:
            return result
        if clean:
            clean_directory(out_root, files=[destination for _, destination, _ in copies])
        counts: dict[str, int] = {}
        for source, destination, group in copies:
            try:
                copy_file(source, destination, root=out_root)
                result["total_files"] += 1
                counts[group] = counts.get(group, 0) + 1
            except (OSError, ValueError) as error:
                result["errors"].append(f"{source} -> {destination}: {error}")
        result["syllabus_files"] = counts.get("syllabus", 0)
        for module in modules:
            name = module.relative_to(course_dir).as_posix()
            if counts.get(name):
                result["modules"].append({"name": name, "files": counts[name]})
        result["modules_published"] = len(result["modules"])
    except (OSError, ValueError) as error:
        result["errors"].append(str(error))
    return result
