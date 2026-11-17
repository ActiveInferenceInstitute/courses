"""Root publication regressions using real registry metadata and disposable trees."""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest

from src.batch_processing.config import COURSE_REGISTRY


SOFTWARE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SOFTWARE_ROOT.parent
PUBLICATION_DIR = "course-site"


def _write(path: Path, content: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _configure(
    repo: Path,
    courses: tuple[str, ...] = ("ai-philosophy",),
    formats: tuple[str, ...] = ("txt",),
    clean_before_publish: bool = True,
) -> None:
    lines = [
        "[general]",
        f"output_dir = {json.dumps(PUBLICATION_DIR)}",
        f"clean_before_publish = {str(clean_before_publish).lower()}",
        "[courses]",
        *(f"{json.dumps(course)} = true" for course in courses),
        "[formats]",
        *(f"{json.dumps(fmt)} = true" for fmt in formats),
        "[options]",
        "generate_website = false",
        "generate_dashboards = false",
        "skip_labs = true",
    ]
    (repo / "publish.toml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _module(repo: Path, course_id: str, relative: str = "01_systems") -> Path:
    metadata = COURSE_REGISTRY[course_id]
    module = repo / metadata["rel_path"] / relative
    module.mkdir(parents=True, exist_ok=True)
    for name in metadata["content_files"]:
        (module / name).write_text(
            f"# {course_id}: {relative}\n\nCourse source content.\n", encoding="utf-8"
        )
    return module


def _snapshot(tree: Path) -> dict[str, bytes | str | None]:
    """Capture bytes and directory structure without traversing source symlinks."""
    if not tree.exists():
        return {}
    state: dict[str, bytes | str | None] = {}
    for path in [tree, *tree.rglob("*")]:
        key = path.relative_to(tree).as_posix()
        if path.is_symlink():
            state[key] = str(path.readlink())
        elif path.is_dir():
            state[key] = None
        else:
            state[key] = path.read_bytes()
    return state


def _run_cli(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    # The absolute interpreter can run the real CLI, but no generation executable
    # is available. An accidental child launch must fail, never render or network.
    environment = os.environ.copy()
    environment.update(
        PATH="",
        PYTHONPATH=str(repo / "software"),
        PYTHONDONTWRITEBYTECODE="1",
        UV_OFFLINE="1",
        UV_NO_SYNC="1",
    )
    return subprocess.run(
        [sys.executable, "-B", str(repo / "publish.py"), *args],
        cwd=repo,
        env=environment,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


@pytest.fixture

def publication_repo(temp_dir: Path) -> Path:
    """Share only real software sources; all writable publishing paths are local."""
    shutil.copy2(REPO_ROOT / "publish.py", temp_dir / "publish.py")
    (temp_dir / "software").mkdir()
    (temp_dir / "software" / "src").symlink_to(
        SOFTWARE_ROOT / "src", target_is_directory=True
    )
    _configure(temp_dir)
    return temp_dir


@pytest.fixture

def root_publish() -> ModuleType:
    spec = importlib.util.spec_from_file_location("course_root_publish", REPO_ROOT / "publish.py")
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load the real root publisher")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize(
    ("courses", "formats", "args", "error"),
    [
        pytest.param(
            ("ai-philosophy",), ("txt",), ("--course", "unknown-course"),
            "Unknown course IDs", id="cli-unknown-course",
        ),
        pytest.param(
            ("unknown-course",), ("txt",), (), "Unknown course IDs",
            id="config-unknown-course",
        ),
        pytest.param(
            ("ai-philosophy", "unknown-course"), ("txt",), (), "Unknown course IDs",
            id="config-mixed-courses",
        ),
        pytest.param((), ("txt",), (), "No courses selected", id="config-empty-courses"),
        pytest.param(
            ("ai-philosophy",), ("txt",), ("--course", ""), "Unknown course IDs",
            id="cli-empty-course",
        ),
        pytest.param(
            ("ai-philosophy",), ("txt",), ("--course", "   "), "Unknown course IDs",
            id="cli-whitespace-course",
        ),
        *(
            pytest.param(
                ("ai-philosophy",), ("txt",), ("--override-formats", value),
                "Unknown output formats", id=f"cli-invalid-formats-{index}",
            )
            for index, value in enumerate(
                ["unknown-format", "txt,unknown-format", "", "   ", "txt,", ",txt", "txt,,md"]
            )
        ),
        pytest.param(
            ("ai-philosophy",), (), (), "No output formats selected",
            id="config-empty-formats",
        ),
        pytest.param(
            ("ai-philosophy",), ("unknown-format",), (), "Unknown output formats",
            id="config-unknown-format",
        ),
        pytest.param(
            ("ai-philosophy",), ("txt", "unknown-format"), (), "Unknown output formats",
            id="config-mixed-formats",
        ),
        pytest.param(
            ("ai-philosophy",), ("txt", ""), (), "Unknown output formats",
            id="config-empty-format-token",
        ),
        pytest.param(
            ("ai-philosophy",), ("txt", "   "), (), "Unknown output formats",
            id="config-whitespace-format-token",
        ),
    ],
)
def test_invalid_cli_selection_is_nonmutating(
    publication_repo: Path,
    existing: bool,
    courses: tuple[str, ...],
    formats: tuple[str, ...],
    args: tuple[str, ...],
    error: str,
) -> None:
    """Publish-only rejects the whole request before mkdir, cleanup or copying."""
    repo = publication_repo
    _configure(repo, courses=courses, formats=formats)
    source = _module(repo, "ai-philosophy")
    _write(source / "output" / "new.txt", b"new source output\n")
    publication = repo / PUBLICATION_DIR
    if existing:
        _write(publication / "AGENTS.md", b"Authored publication guidance.\n")
        _write(publication / "ai-philosophy" / "01_systems" / "old.pdf", b"old output\n")
        (publication / "empty-directory").mkdir()
    before = _snapshot(repo)

    result = _run_cli(repo, "--publish-only", *args)

    assert result.returncode != 0
    assert error in result.stdout + result.stderr
    assert _snapshot(repo) == before
    assert publication.exists() is existing


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize(
    "courses", [(), ("unknown-course",), ("ai-philosophy", "unknown-course"), ("   ",)]
)
def test_direct_publish_rejects_invalid_courses_before_mkdir(
    publication_repo: Path, root_publish: ModuleType, existing: bool, courses: tuple[str, ...]
) -> None:
    """Direct callers cannot partially publish or clean a mixed course selection."""
    repo = publication_repo
    source = _module(repo, "ai-philosophy")
    _write(source / "output" / "new.txt", b"new output\n")
    publication = repo / PUBLICATION_DIR
    if existing:
        _write(publication / "ai-philosophy" / "01_systems" / "old.pdf", b"preserve\n")
    before = _snapshot(repo)

    assert root_publish.run_publish(repo, list(courses), PUBLICATION_DIR) is False

    assert _snapshot(repo) == before
    assert publication.exists() is existing


def test_invalid_selection_precedes_generation_and_scaffolding(publication_repo: Path) -> None:
    """Both invalid lists fail before dashboard, YouTube or generation work."""
    repo = publication_repo
    _configure(repo, courses=("youtube", "unknown-course"), formats=("txt", "unknown-format"))
    _module(repo, "youtube", "bookstreams/01_video")
    before = _snapshot(repo)

    result = _run_cli(repo, "--generate-dashboards")

    assert result.returncode != 0
    assert "Unknown course IDs" in result.stderr
    assert "Unknown output formats" in result.stderr
    assert _snapshot(repo) == before


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("publish_only", [False, True])
def test_dry_run_leaves_sources_and_publication_unchanged(
    publication_repo: Path, existing: bool, publish_only: bool
) -> None:
    """Generation/scaffold previews and publication previews are read-only."""
    repo = publication_repo
    _configure(repo, courses=("active-inference", "youtube"))
    core = _module(repo, "active-inference", "01_philosophy/01_systems")
    youtube = _module(repo, "youtube", "bookstreams/01_video")
    for module in (core, youtube):
        _write(module / "output" / "lecture-content" / f"{module.name}-module.txt", b"output\n")
        _write(module / "dashboard.html", b"<h1>Dashboard</h1>\n")
    core_path = repo / COURSE_REGISTRY["active-inference"]["rel_path"]
    for relative in COURSE_REGISTRY["active-inference"]["static_dirs"]:
        _write(core_path / relative / "content.txt", b"static source\n")
    publication = repo / PUBLICATION_DIR
    if existing:
        _write(publication / "AGENTS.md", b"Authored guidance.\n")
        _write(publication / "active-inference" / "01_philosophy" / "01_systems" / "old.pdf", b"old\n")
        (publication / "empty-directory").mkdir()
    before = _snapshot(repo)
    args = ["--dry-run", "--generate-dashboards"]
    if publish_only:
        args.append("--publish-only")

    result = _run_cli(repo, *args)

    assert result.returncode == 0, result.stdout + result.stderr
    assert _snapshot(repo) == before
    assert publication.exists() is existing


def test_selected_cleanup_preserves_other_courses_guides_and_unit_identities(
    publication_repo: Path,
) -> None:
    """Only selected generated files change, including stale removed modules."""
    repo = publication_repo
    _configure(repo, courses=("ai-es", "ai-family"))
    publication = repo / PUBLICATION_DIR
    selected = publication / "ai-es"
    expected: dict[Path, bytes] = {}
    stale: list[Path] = []
    authored: dict[Path, bytes] = {
        publication / "AGENTS.md": b"Publication agent guidance.\n",
        publication / "README.md": b"Publication readme.\n",
        publication / "GUIDE.md": b"Publication guide.\n",
        publication / "landing.html": b"<h1>Authored landing page</h1>\n",
        selected / "AGENTS.md": b"Course agent guidance.\n",
        selected / "README.md": b"Course readme.\n",
        selected / "COURSE_GUIDE.md": b"Course guide.\n",
        selected / "authored-library" / "notes.txt": b"Not a generated module.\n",
    }
    for unit in ("01_cognitive_science", "02_computational_neuroscience"):
        source = _module(repo, "ai-es", f"{unit}/01_systems")
        destination = selected / unit / "01_systems"
        for suffix, content in (("txt", f"{unit} text\n"), ("md", f"# {unit}\n")):
            relative = Path("lecture-content") / f"01_systems-module.{suffix}"
            _write(source / "output" / relative, content.encode())
            _write(destination / relative, b"previous rendering\n")
            expected[destination / relative] = content.encode()
        _write(source / "dashboard.html", f"<h1>{unit}</h1>\n".encode())
        expected[destination / "dashboard.html"] = (source / "dashboard.html").read_bytes()
        _write(source / "output" / "README.md", b"Do not overwrite the authored readme.\n")
        _write(source / "output" / "lecture-content" / "GUIDE.md", b"Source output guide.\n")
        authored[selected / unit / "README.md"] = b"Unit readme.\n"
        authored[destination / "AGENTS.md"] = b"Module agent guidance.\n"
        authored[destination / "README.md"] = b"Module readme.\n"
        authored[destination / "guide.md"] = b"Authored module guide.\n"
        authored[destination / "lecture-content" / "GUIDE.md"] = b"Nested authored guide.\n"
        stale.extend(
            [
                _write(destination / "obsolete.pdf", b"obsolete\n"),
                _write(destination / "study-guides" / "01_systems-practice_quiz.md", b"stale MD\n"),
            ]
        )
    retired = selected / "03_retired" / "02_agents"
    stale.append(_write(retired / "old.pdf", b"removed module output\n"))
    stale.append(_write(retired / "study-guides" / "02_agents-practice_quiz.md", b"stale MD\n"))
    authored[retired / "README.md"] = b"Retired module's authored guidance.\n"
    for path, content in authored.items():
        _write(path, content)
    other_source = _module(repo, "ai-family", "01_family/01_systems")
    _write(other_source / "output" / "new.txt", b"Unselected source output.\n")
    other = publication / "ai-family"
    _write(other / "01_family" / "01_systems" / "old.pdf", b"Unselected publication.\n")
    _write(other / "README.md", b"Unselected authored readme.\n")
    other_before = _snapshot(other)
    sources_before = _snapshot(repo / "course_development")
    identities = {
        path: path.stat().st_ino
        for path in (selected, selected / "01_cognitive_science", selected / "02_computational_neuroscience", retired)
    }

    result = _run_cli(repo, "--publish-only", "--course", "ai-es")

    assert result.returncode == 0, result.stdout + result.stderr
    assert _snapshot(other) == other_before
    assert _snapshot(repo / "course_development") == sources_before
    assert all(path.read_bytes() == content for path, content in authored.items())
    assert all(path.read_bytes() == content for path, content in expected.items())
    assert all(not path.exists() for path in stale)
    assert all(path.stat().st_ino == inode for path, inode in identities.items())
    assert not (repo / "published").exists()


@pytest.mark.parametrize("clean,skip_clear", [(True, True), (False, False)])
def test_cleanup_opt_out_retains_stale_files_and_copies_new_outputs(
    publication_repo: Path, clean: bool, skip_clear: bool
) -> None:
    """Either cleanup switch preserves old artifacts without blocking replacement."""
    repo = publication_repo
    _configure(repo, clean_before_publish=clean)
    source = _module(repo, "ai-philosophy")
    destination = repo / PUBLICATION_DIR / "ai-philosophy" / "01_systems"
    _write(source / "output" / "new.txt", b"current output\n")
    _write(destination / "new.txt", b"previous version\n")
    old_pdf = _write(destination / "old.pdf", b"retain old PDF\n")
    old_md = _write(destination / "study-guides" / "01_systems-practice_quiz.md", b"retain old MD\n")
    args = ["--publish-only"]
    if skip_clear:
        args.append("--skip-clear")

    result = _run_cli(repo, *args)

    assert result.returncode == 0, result.stdout + result.stderr
    assert (destination / "new.txt").read_bytes() == b"current output\n"
    assert old_pdf.read_bytes() == b"retain old PDF\n"
    assert old_md.read_bytes() == b"retain old MD\n"


@pytest.mark.parametrize("clean,skip_clear", [(True, False), (True, True), (False, False)])
def test_static_destinations_preserve_layout_guides_and_cleanup_switches(
    publication_repo: Path, clean: bool, skip_clear: bool
) -> None:
    """Registry static trees retain their relative paths and authored Markdown."""
    repo = publication_repo
    _configure(repo, courses=("active-inference",), clean_before_publish=clean)
    _module(repo, "active-inference", "01_philosophy/01_systems")
    course = repo / COURSE_REGISTRY["active-inference"]["rel_path"]
    selected = repo / PUBLICATION_DIR / "active-inference"
    destinations: list[Path] = []
    for relative in COURSE_REGISTRY["active-inference"]["static_dirs"]:
        source = course / relative
        destination = selected / relative
        _write(source / "package" / "current.py", b"COURSE_TITLE = 'Active Inference'\n")
        (source / "empty-directory").mkdir()
        _write(source / "README.md", b"Source static readme.\n")
        _write(destination / "obsolete.py", b"ARCHIVED_VERSION = 1\n")
        _write(destination / "README.md", b"Authored destination readme.\n")
        _write(destination / "GUIDE.md", b"Authored static guide.\n")
        destinations.append(destination)
    identities = {path: path.stat().st_ino for path in destinations}
    args = ["--publish-only"]
    if skip_clear:
        args.append("--skip-clear")

    result = _run_cli(repo, *args)

    assert result.returncode == 0, result.stdout + result.stderr
    for destination in destinations:
        assert (destination / "package" / "current.py").read_bytes() == b"COURSE_TITLE = 'Active Inference'\n"
        assert (destination / "empty-directory").is_dir()
        assert (destination / "README.md").read_bytes() == b"Authored destination readme.\n"
        assert (destination / "GUIDE.md").read_bytes() == b"Authored static guide.\n"
        assert (destination / "obsolete.py").exists() is (not clean or skip_clear)
        assert destination.stat().st_ino == identities[destination]


@pytest.mark.parametrize("alias", ["publication", "course", "unit", "module", "file", "static"])
@pytest.mark.parametrize("skip_clear", [False, True])
def test_publication_aliases_never_modify_authored_sources(
    publication_repo: Path, alias: str, skip_clear: bool
) -> None:
    """Reject real source aliases before either cleanup or copying can follow them."""
    repo = publication_repo
    course_id = "active-inference"
    _configure(repo, courses=(course_id,))
    source = _module(repo, course_id, "01_philosophy/01_systems")
    _write(source / "output" / "module.md", b"generated replacement\n")
    publication = repo / PUBLICATION_DIR
    course_pub = publication / course_id
    module_pub = course_pub / "01_philosophy/01_systems"
    course = repo / COURSE_REGISTRY[course_id]["rel_path"]
    if alias == "publication":
        link, target = publication, course
    elif alias == "course":
        link, target = course_pub, course
    elif alias == "unit":
        link, target = course_pub / "01_philosophy", source.parent
    elif alias == "module":
        link, target = module_pub, source
    elif alias == "file":
        link, target = module_pub / "module.md", source / "module.md"
    else:
        relative = COURSE_REGISTRY[course_id]["static_dirs"][0]
        target = course / relative
        _write(target / "authored.py", b"AUTHORED = True\n")
        link = course_pub / relative
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(target, target_is_directory=target.is_dir())
    before = _snapshot(repo)
    args = ["--publish-only"]
    if skip_clear:
        args.append("--skip-clear")

    result = _run_cli(repo, *args)

    assert result.returncode != 0
    assert "publication" in (result.stdout + result.stderr).lower()
    assert _snapshot(repo) == before


def test_publication_root_cannot_overlap_authored_course(publication_repo: Path) -> None:
    """A configured source directory is not an admissible publication root."""
    repo = publication_repo
    source = _module(repo, "ai-philosophy")
    _write(source / "output/new.txt", b"generated\n")
    config = repo / "publish.toml"
    config.write_text(config.read_text().replace(PUBLICATION_DIR, "course_development"))
    before = _snapshot(repo)

    result = _run_cli(repo, "--publish-only")

    assert result.returncode != 0
    assert "overlaps authored course source" in result.stdout + result.stderr
    assert _snapshot(repo) == before
