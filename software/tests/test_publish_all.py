"""Run the complete local Markdown pipeline against isolated authored files."""
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
