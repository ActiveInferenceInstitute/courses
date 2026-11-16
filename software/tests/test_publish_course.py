"""Publication CLI failure propagation through real filesystem inputs."""
from scripts.generate_all_outputs import main as generate
from scripts.publish_course import main


def test_missing_selected_output_fails_without_partial_publication(tmp_path):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nSource.")
    args = ["--repo-root", str(tmp_path), "--course", "ai-philosophy",
            "--formats", "md", "--no-website"]
    assert main(args) == 1
    assert not (tmp_path / "published").exists()
    assert generate(args) == 0
    assert main(args) == 0
    destination = tmp_path / "published/ai-philosophy/01_systems/lecture-content/01_systems-module.md"
    assert destination.read_bytes() == (module / "module.md").read_bytes()


def test_copy_destination_failure_returns_nonzero(tmp_path):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nSource.")
    args = ["--repo-root", str(tmp_path), "--course", "ai-philosophy",
            "--formats", "md", "--no-website"]
    assert generate(args) == 0
    (tmp_path / "published").write_text("blocking file")
    assert main(args) == 1
    assert (tmp_path / "published").read_text() == "blocking file"
