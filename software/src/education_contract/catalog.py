"""Read the authored course tree into an ``education-contract/v1`` bundle.

Extraction is transcription, not invention: every field comes from a named place in
the tree, and the rules below are the only ones the extractor applies.

* unit        -- a ``<course>/<discipline>/NN_<topic>/`` directory that holds ``module.md``
* title       -- the first ``# `` heading of that ``module.md``
* topic       -- the ``<topic>`` suffix of the directory name, kept only when it is one
                 of the eight-topic spine (``docs/workflows/education.md``)
* objectives  -- the numbered items under ``## Learning Objectives``, verbatim, with
                 positional ids ``obj-1..N``
* glossary    -- the bold-bullet entries of ``<course>/resources/glossary.md``
* prerequisites -- always empty: this tree states its prerequisite chain as prose and
                 ASCII art (``<course>/resources/learning_pathways.md``), so there is no
                 authored edge to transcribe. ``./run.sh contract`` proves the schema
                 accepts an edgeless document and rejects a wrong one.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
COURSE_DEVELOPMENT = ROOT / "course_development"
REPOSITORY = "ActiveInferenceInstitute/courses"

TOPICS = (
    "systems",
    "agents",
    "perception",
    "cognition",
    "action",
    "learning",
    "communication",
    "planning",
)

# course_development/AGENTS.md audience ladder. A course directory outside this map
# simply carries no audience_level.
COURSE_LEVELS = {
    "active_inference": "core",
    "active_inference_101": "101",
    "active_inference_401": "401",
    "active_inference_es": "es",
    "active_inference_family": "family",
    "active_inference_hs": "hs",
    "active_inference_ms": "ms",
}

DIR_RE = re.compile(r"^(\d{2})_([a-z0-9_]+)$")
NUMBERED_RE = re.compile(r"^\s*\d+[.)]\s+(\S.*)$")
BOLD_BULLET_RE = re.compile(r"^-\s+\*\*(?P<term>[^*]+)\*\*\s*[—:–-]\s*(?P<definition>.+)$")
SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(text: str) -> str:
    return SLUG_RE.sub("-", text.strip().lower()).strip("-")


def _heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _section(text: str, heading: str) -> str:
    match = re.search(rf"^##+ {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else ""


def read_objectives(module_path: Path) -> list[str]:
    """Return the numbered learning objectives of one ``module.md``, verbatim."""
    section = _section(module_path.read_text(encoding="utf-8"), "Learning Objectives")
    statements: list[str] = []
    for line in section.splitlines():
        match = NUMBERED_RE.match(line)
        if match:
            statements.append(match.group(1).strip())
    return statements


def read_glossary(glossary_path: Path) -> list[dict[str, Any]]:
    """Return the bold-bullet glossary entries, in file order."""
    terms: list[dict[str, Any]] = []
    seen: set[str] = set()
    for line in glossary_path.read_text(encoding="utf-8").splitlines():
        match = BOLD_BULLET_RE.match(line)
        if not match:
            continue
        term = match.group("term").strip()
        term_id = _slug(term)
        if not term_id or term_id in seen:
            continue
        seen.add(term_id)
        terms.append(
            {
                "term_id": term_id,
                "term": term,
                "definition": match.group("definition").strip(),
                "source": str(glossary_path.relative_to(ROOT)),
            }
        )
    return terms


def read_units(course_dir: Path, course_id: str) -> list[dict[str, Any]]:
    """Return one unit per ``<discipline>/NN_<topic>/module.md`` under ``course_dir``."""
    units: list[dict[str, Any]] = []
    for discipline in sorted(path for path in course_dir.iterdir() if path.is_dir()):
        if not DIR_RE.match(discipline.name):
            continue
        for module_dir in sorted(path for path in discipline.iterdir() if path.is_dir()):
            module_match = DIR_RE.match(module_dir.name)
            if module_match is None:
                continue
            module_path = module_dir / "module.md"
            if not module_path.is_file():
                continue
            objectives = read_objectives(module_path)
            if not objectives:
                raise ValueError(f"{module_path} has no numbered learning objectives")
            topic = module_match.group(2)
            unit: dict[str, Any] = {
                "unit_id": f"{course_id}.{discipline.name}.{module_dir.name}",
                "title": _heading(module_path.read_text(encoding="utf-8")) or module_dir.name,
            }
            level = COURSE_LEVELS.get(course_dir.name)
            if level:
                unit["audience_level"] = level
            if topic in TOPICS:
                unit["topic"] = topic
            unit["objectives"] = [
                {"objective_id": f"obj-{index}", "statement": statement}
                for index, statement in enumerate(objectives, start=1)
            ]
            unit["prerequisites"] = []
            unit["source_path"] = str(module_path.relative_to(ROOT))
            units.append(unit)
    return units


def build_bundle(course: str) -> dict[str, Any]:
    """Return the contract document for one course directory."""
    course_dir = COURSE_DEVELOPMENT / course
    if not course_dir.is_dir():
        raise ValueError(f"no course directory at {course_dir}")
    course_id = _slug(course)
    units = read_units(course_dir, course_id)
    if not units:
        raise ValueError(f"{course_dir} has no units in the <discipline>/NN_<topic> shape")
    glossary_path = course_dir / "resources" / "glossary.md"
    return {
        "schema": "education-contract/v1",
        "provenance": {
            "repository": REPOSITORY,
            "generator": f"software/scripts/export_education_bundle.py --course {course}",
        },
        "units": units,
        "prerequisite_edges": [],
        "glossary": read_glossary(glossary_path) if glossary_path.is_file() else [],
    }


def render_bundle(bundle: dict[str, Any]) -> str:
    """Serialize a bundle the one way this repository commits it."""
    return json.dumps(bundle, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
