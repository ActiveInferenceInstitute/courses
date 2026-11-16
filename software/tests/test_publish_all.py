"""Run the complete local Markdown pipeline against isolated authored files."""
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.publish_all import main


def test_pipeline_generates_validates_publishes_lowercase_unit_identities(tmp_path):
    course = tmp_path / "course_development/active_inference"
    for unit in ("01_philosophy", "02_cognitive_science"):
        module = course / unit / "01_systems"
        module.mkdir(parents=True)
        (module / "module.md").write_text(f"# Systems\n\n{unit} content.")
    args = ["--repo-root", str(tmp_path), "--course", "active-inference",
            "--formats", "md", "--no-website", "--skip-copy-extras"]
    assert main(args) == 0
    for unit in ("01_philosophy", "02_cognitive_science"):
        output = tmp_path / "published/active-inference" / unit / "01_systems/01_systems-module.md"
        assert output.read_bytes() == (course / unit / "01_systems/module.md").read_bytes()
    names = {path.name for path in tmp_path.iterdir()}
    assert "published" in names and "PUBLISHED" not in names


def test_generation_error_never_proceeds_to_publication(tmp_path):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_bytes(b"\xff")
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--formats", "txt", "--no-website"]) == 1
    assert not (tmp_path / "published").exists()


def test_filtered_pipeline_keeps_other_publication_and_website(tmp_path):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nSelected.")
    untouched = tmp_path / "published/active-inference/02_cognitive_science/01_systems/old.md"
    untouched.parent.mkdir(parents=True)
    untouched.write_text("custody")
    assert main(["--repo-root", str(tmp_path), "--course", "active-inference",
                 "--unit", "01_philosophy", "--module", "1", "--formats", "md",
                 "--clean", "--skip-copy-extras"]) == 0
    assert untouched.read_text() == "custody"
    assert (tmp_path / "published/active-inference/01_philosophy/01_systems/website/index.html").is_file()


@pytest.mark.parametrize("clean", [False, True])
def test_pipeline_republishes_changed_sources_at_owned_flattened_paths(tmp_path, clean):
    """First publication and two changed-source republishes share stable targets."""
    course = tmp_path / "course_development/active_inference"
    modules = [course / unit / "01_systems"
               for unit in ("01_philosophy", "02_cognitive_science")]
    for module in modules:
        module.mkdir(parents=True)
    args = ["--repo-root", str(tmp_path), "--course", "active-inference",
            "--formats", "md", "--no-website", "--skip-copy-extras"]
    if clean:
        args.append("--clean")
    for revision in range(3):
        for module in modules:
            (module / "module.md").write_text(f"# Systems\n\n{module.parent.name}: revision {revision}.")
        assert main(args) == 0
        for module in modules:
            published = tmp_path / "published/active-inference" / module.relative_to(course)
            target = published / "01_systems-module.md"
            assert target.read_bytes() == (module / "module.md").read_bytes()
            assert list(published.glob("*.md")) == [target]
            assert not (published / "lecture-content/01_systems-module.md").exists()


@pytest.mark.parametrize("matching_bytes", [False, True])
def test_pipeline_preserves_unknown_root_collision_across_republishes(tmp_path, matching_bytes):
    """A generated prefix is replaceable, but the unknown original never is."""
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    published = tmp_path / "published/ai-philosophy/01_systems"
    published.mkdir(parents=True)
    foreign = published / "01_systems-module.md"
    first_source = "# Systems\n\nRevision 0."
    foreign.write_text(first_source if matching_bytes else "authored root file")
    guide = published / "README.md"
    guide.write_text("authored publication guide")
    protected = {path: path.read_bytes() for path in (foreign, guide)}
    args = ["--repo-root", str(tmp_path), "--course", "ai-philosophy",
            "--formats", "md", "--no-website", "--skip-copy-extras", "--clean"]
    for revision in range(3):
        (module / "module.md").write_text(f"# Systems\n\nRevision {revision}.")
        assert main(args) == 0
        target = published / "lecture-content_01_systems-module.md"
        assert target.read_bytes() == (module / "module.md").read_bytes()
        assert {path: path.read_bytes() for path in protected} == protected
        assert set(published.glob("*.md")) == {foreign, guide, target}


def test_cli_relative_repo_root_generates_publishes_and_copies_module_extras(tmp_path):
    """Relative roots remain absolute through cleanup, publication and extras."""
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nRelative-root publication.")
    (module / "dashboard.html").write_text("<html>Module dashboard</html>")
    script = Path(__file__).resolve().parents[1] / "scripts/publish_all.py"
    result = subprocess.run(
        [sys.executable, str(script), "--repo-root", tmp_path.name,
         "--course", "ai-philosophy", "--formats", "md", "--no-website"],
        cwd=tmp_path.parent, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    published = tmp_path / "published/ai-philosophy/01_systems"
    assert (published / "01_systems-module.md").read_bytes() == (module / "module.md").read_bytes()
    assert (published / "dashboard.html").read_bytes() == (module / "dashboard.html").read_bytes()
