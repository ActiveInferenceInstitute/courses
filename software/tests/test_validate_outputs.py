"""Validate the same admitted source manifest as the generator."""
import json

from scripts.generate_all_outputs import main as generate
from scripts.validate_outputs import main


def test_current_registry_selection_and_all_required_formats(tmp_path, capsys):
    module = tmp_path / "course_development/active_inference/01_philosophy/01_systems"
    module.mkdir(parents=True)
    (module / "module.md").write_text("# Systems\n\nSource.")
    args = ["--repo-root", str(tmp_path), "--course", "ai-philosophy",
            "--formats", "md,txt", "--no-website"]
    assert generate(args) == 0
    capsys.readouterr()
    assert main([*args, "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload[0]["valid"] is True
    (module / "output/lecture-content/01_systems-module.md").unlink()
    assert main([*args, "--json"]) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload[0]["valid"] is False
    assert any("01_systems-module.md" in issue for issue in payload[0]["issues"])


def test_empty_or_invalid_selection_is_not_success(tmp_path, capsys):
    (tmp_path / "course_development/active_inference/01_philosophy").mkdir(parents=True)
    for extra in ([], ["--formats", "unknown"], ["--max-module", "ai-philosophy:0"]):
        assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy", "--json", *extra]) == 1
        assert json.loads(capsys.readouterr().out)[0]["valid"] is False
