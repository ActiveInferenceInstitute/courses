"""Real-file regressions for admitted generation and scoped cleanup."""

import pytest

from scripts.generate_all_outputs import main
from src.batch_processing.main import clear_all_outputs
from src.batch_processing.utils import get_courses_to_process, plan_generation


def snapshot(root):
    return {str(path.relative_to(root)): path.read_bytes()
            for path in root.rglob("*") if path.is_file()}


def modules(root):
    course = root / "course_development/active_inference"
    paths = [course / unit / module for unit in ("01_philosophy", "02_cognitive_science")
             for module in ("01_systems", "02_agents")]
    for path in paths:
        path.mkdir(parents=True)
        (path / "module.md").write_text(f"# {path.parent.name}\n\nAuthored explanation.\n")
        (path / "lab.md").write_text("# Lab\n\nAuthored protocol.\n")
        out = path / "output/lecture-content"
        out.mkdir(parents=True)
        for fmt in ("md", "pdf"):
            (out / f"{path.name}-module.{fmt}").write_text(f"old {path} {fmt}")
        (path / "output/README.md").write_text("authored guide")
        (path / "output/.keep").write_text("hidden custody")
    return course, paths


def test_numeric_ambiguity_rejected_before_cleanup(tmp_path, capsys):
    _, paths = modules(tmp_path)
    before = snapshot(tmp_path)
    assert main(["--repo-root", str(tmp_path), "--course", "active-inference",
                 "--module", "1", "--formats", "md", "--no-website"]) == 1
    assert snapshot(tmp_path) == before
    assert "Ambiguous module" in capsys.readouterr().err
    assert all((path / "output/README.md").read_text() == "authored guide" for path in paths)


def test_selected_generation_preserves_other_units_modules_formats_guides(tmp_path):
    _, paths = modules(tmp_path)
    before = snapshot(tmp_path)
    selected = paths[0]
    output = selected / "output/lecture-content/01_systems-module.md"
    output_directory_inode = output.parent.stat().st_ino
    assert main(["--repo-root", str(tmp_path), "--course", "active-inference",
                 "--unit", "01_philosophy", "--module", "1", "--formats", "md",
                 "--skip-labs", "--no-website"]) == 0
    after = snapshot(tmp_path)
    assert output.read_bytes() == (selected / "module.md").read_bytes()
    changed = {name for name in before.keys() | after.keys() if before.get(name) != after.get(name)}
    assert changed == {str(output.relative_to(tmp_path))}
    assert output.parent.stat().st_ino == output_directory_inode


@pytest.mark.parametrize("extra", [
    ["--formats", "md,unknown"], ["--module", "0"],
    ["--max-module", "active-inference:0"], ["--max-lab", "ai-math:1"],
])
def test_invalid_admission_never_mutates(tmp_path, extra):
    modules(tmp_path)
    before = snapshot(tmp_path)
    assert main(["--repo-root", str(tmp_path), "--course", "active-inference", *extra]) == 1
    assert snapshot(tmp_path) == before


def test_dry_run_is_nonmutating_and_unit_qualified(tmp_path, capsys):
    modules(tmp_path)
    before = snapshot(tmp_path)
    assert main(["--repo-root", str(tmp_path), "--course", "active-inference",
                 "--unit", "02_cognitive_science", "--module", "2",
                 "--formats", "md", "--skip-labs", "--no-website", "--dry-run"]) == 0
    assert snapshot(tmp_path) == before
    text = capsys.readouterr().out
    assert "02_cognitive_science/02_agents/output/lecture-content/02_agents-module.md" in text
    assert "01_philosophy" not in text
    assert "website" not in text


def test_lab_and_module_limits_clean_only_admitted_outputs(tmp_path):
    course, paths = modules(tmp_path)
    labs = course / "labs"
    for index in (1, 2):
        labs.mkdir(exist_ok=True)
        (labs / f"lab-{index}.md").write_text("# Lab\n\nProtocol.")
        for fmt in ("pdf", "html"):
            destination = labs / "output" / fmt / f"lab-{index}.{fmt}"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(f"old lab {index} {fmt}")
    plans = plan_generation(
        tmp_path, get_courses_to_process("active-inference"), ["pdf"],
        max_modules={"active-inference": 1}, max_labs={"active-inference": 1},
        generate_website=False,
    )
    result = clear_all_outputs(tmp_path, plans=plans)
    assert result["errors"] == []
    assert not (labs / "output/pdf/lab-1.pdf").exists()
    assert (labs / "output/pdf/lab-2.pdf").read_text() == "old lab 2 pdf"
    assert (labs / "output/html/lab-1.html").read_text() == "old lab 1 html"
    assert (paths[1] / "output/lecture-content/02_agents-module.pdf").exists()
    assert (paths[0] / "output/lecture-content/01_systems-module.md").exists()


def test_real_render_failure_is_nonzero_and_retains_peer_result(tmp_path):
    course = tmp_path / "course_development/active_inference/01_philosophy"
    for name in ("01_systems", "02_agents"):
        (course / name).mkdir(parents=True)
    (course / "01_systems/module.md").write_bytes(b"\xff")
    (course / "02_agents/module.md").write_text("# Agents\n\nWorking peer.")
    assert main(["--repo-root", str(tmp_path), "--course", "ai-philosophy",
                 "--formats", "txt", "--no-website"]) == 1
    assert "Working peer" in (course / "02_agents/output/lecture-content/02_agents-module.txt").read_text()
