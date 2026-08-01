"""Tests for course_generator content rendering."""

import pytest
from src.course_generator.schema import (
    ModuleConfig, CourseConfig, CurriculumConfig, MODULE_TOPICS,
)
from src.course_generator.content import (
    render_module_md, render_questions_md, render_quiz_md,
    render_lab_md, render_readme_md, render_agents_md,
    render_dashboard_html, render_course_readme, render_course_agents,
    render_course_syllabus, render_root_readme, render_root_overview,
    render_root_agents, render_audit_script,
    render_resource_glossary, render_resource_notation,
    render_resource_references, render_resource_cross_course_map,
    render_resource_faq, render_resource_readme, render_resource_agents,
    render_resource_learning_pathways,
)


@pytest.fixture
def sample_curriculum():
    """Build a minimal curriculum for testing content renders."""
    courses = []
    for c in range(1, 5):
        modules = [
            ModuleConfig(
                number=i, topic=t, subtitle=f"Test {t.title()}",
                key_concepts=[f"{t}_concept_1", f"{t}_concept_2"],
                learning_goals=[f"Learn {t}", f"Apply {t}"],
            )
            for i, t in enumerate(MODULE_TOPICS, 1)
        ]
        courses.append(CourseConfig(
            number=c, dir_name=f"{c:02d}_test", title=f"Test Course {c}",
            perspective="Testing", lab_type="Test Lab", modules=modules,
        ))
    return CurriculumConfig(
        id="test_content", title="Test Content Curriculum",
        audience="Test audience", tone="Testing tone. Clear.", courses=courses,
    )


class TestModuleLevelContent:
    """Tests for module-level file rendering."""

    def test_module_md_has_title(self, sample_curriculum):
        """Test module.md contains the module title."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_module_md(m, c, sample_curriculum)
        assert f"# Module 01: {m.topic.title()}" in result

    def test_module_md_has_concepts(self, sample_curriculum):
        """Test module.md contains key concepts."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_module_md(m, c, sample_curriculum)
        for concept in m.key_concepts:
            assert concept in result

    def test_questions_has_questions(self, sample_curriculum):
        """Test questions.md contains numbered questions."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_questions_md(m, c, sample_curriculum)
        assert "### Question 1" in result

    def test_quiz_has_mc(self, sample_curriculum):
        """Test practice_quiz.md has multiple choice section."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_quiz_md(m, c, sample_curriculum)
        assert "Part A: Multiple Choice" in result
        assert "Part B: Short Answer" in result

    def test_lab_has_instructions(self, sample_curriculum):
        """Test lab.md has instructions and reflection."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_lab_md(m, c, sample_curriculum)
        assert "Part 1: Exploration" in result
        assert "Reflection" in result

    def test_readme_has_navigation(self, sample_curriculum):
        """Test README.md has Quick Navigation links."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_readme_md(m, c, sample_curriculum)
        assert "Quick Navigation" in result
        assert "Course Home" in result

    def test_agents_has_conventions(self, sample_curriculum):
        """Test AGENTS.md has conventions section."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_agents_md(m, c, sample_curriculum)
        assert "Conventions" in result
        assert c.perspective in result

    def test_dashboard_is_valid_html(self, sample_curriculum):
        """Test dashboard.html starts with DOCTYPE."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        result = render_dashboard_html(m, c, sample_curriculum)
        assert result.startswith("<!DOCTYPE html>")
        assert "</html>" in result

    def test_no_placeholders_in_module_files(self, sample_curriculum):
        """Test all module renders contain no placeholders."""
        c = sample_curriculum.courses[0]
        m = c.modules[0]
        renders = [
            render_module_md(m, c, sample_curriculum),
            render_questions_md(m, c, sample_curriculum),
            render_quiz_md(m, c, sample_curriculum),
            render_lab_md(m, c, sample_curriculum),
            render_readme_md(m, c, sample_curriculum),
            render_agents_md(m, c, sample_curriculum),
        ]
        for rendered in renders:
            assert "[TODO]" not in rendered
            assert "[PLACEHOLDER]" not in rendered


class TestCourseLevelContent:
    """Tests for course-level file rendering."""

    def test_course_readme_has_modules(self, sample_curriculum):
        """Test course README lists all 8 modules."""
        c = sample_curriculum.courses[0]
        result = render_course_readme(c, sample_curriculum)
        for m in c.modules:
            assert m.topic.title() in result

    def test_course_agents_has_identity(self, sample_curriculum):
        """Test course AGENTS has identity section."""
        c = sample_curriculum.courses[0]
        result = render_course_agents(c, sample_curriculum)
        assert c.title in result
        assert c.perspective in result

    def test_course_syllabus_has_schedule(self, sample_curriculum):
        """Test syllabus has a schedule table."""
        c = sample_curriculum.courses[0]
        result = render_course_syllabus(c, sample_curriculum)
        assert "Week 1" in result
        assert "Week 8" in result


class TestRootLevelContent:
    """Tests for root-level file rendering."""

    def test_root_readme_has_courses(self, sample_curriculum):
        """Test root README lists all courses."""
        result = render_root_readme(sample_curriculum)
        for c in sample_curriculum.courses:
            assert c.title in result

    def test_root_overview_has_vision(self, sample_curriculum):
        """Test OVERVIEW.md has a Vision section."""
        result = render_root_overview(sample_curriculum)
        assert "Vision" in result

    def test_root_agents_has_rules(self, sample_curriculum):
        """Test AGENTS.md has critical rules."""
        result = render_root_agents(sample_curriculum)
        assert "Critical Rules" in result
        assert sample_curriculum.audience in result

    def test_audit_script_is_bash(self, sample_curriculum):
        """Test audit script starts with shebang."""
        result = render_audit_script(sample_curriculum)
        assert result.startswith("#!/usr/bin/env bash")

    def test_audit_script_shell_quotes_hostile_input(self):
        """Titles/dir_names with shell metacharacters must not break out."""
        from src.course_generator.schema import CourseConfig, CurriculumConfig, ModuleConfig

        modules = [
            ModuleConfig(
                number=i, topic=MODULE_TOPICS[i - 1],
                subtitle=f"Test {MODULE_TOPICS[i-1].title()}",
            )
            for i in range(1, 9)
        ]
        hostile = "$(rm -rf /)"
        title_hostile = "'; echo pwned; '"
        course = CourseConfig(
            number=1,
            dir_name=hostile,
            title=title_hostile,
            perspective="Testing",
            lab_type="Test Lab",
            modules=modules,
        )
        cur = CurriculumConfig(
            id="t", title="T", audience="a", tone="neutral",
            courses=[course] * 4,
        )
        script = render_audit_script(cur)
        # Hostile metacharacters must be safely single-quoted, not active.
        assert "check_course '$(" in script
        assert "$(rm -rf /)" in script
        # A single-quote in the value is escaped so it cannot break out.
        assert "\\''" in script or "'\\''" in script


class TestResourceContent:
    """Tests for resource file rendering."""

    def test_glossary_has_entries(self, sample_curriculum):
        """Test glossary has concept entries."""
        result = render_resource_glossary(sample_curriculum)
        assert "###" in result  # Term headings

    def test_notation_has_table(self, sample_curriculum):
        """Test notation table has a table."""
        result = render_resource_notation(sample_curriculum)
        assert "| Symbol |" in result

    def test_references_has_citations(self, sample_curriculum):
        """Test references has citations."""
        result = render_resource_references(sample_curriculum)
        assert "Friston" in result

    def test_cross_course_map_has_all_topics(self, sample_curriculum):
        """Test cross-course map contains all 8 topics."""
        result = render_resource_cross_course_map(sample_curriculum)
        for topic in MODULE_TOPICS:
            assert topic.title() in result

    def test_faq_has_qa(self, sample_curriculum):
        """Test FAQ has questions and answers."""
        result = render_resource_faq(sample_curriculum)
        assert "What is Active Inference?" in result

    def test_resource_readme_has_contents(self, sample_curriculum):
        """Test resource README has contents table."""
        result = render_resource_readme(sample_curriculum)
        assert "glossary.md" in result

    def test_resource_agents_has_rules(self, sample_curriculum):
        """Test resource AGENTS has maintenance rules."""
        result = render_resource_agents(sample_curriculum)
        assert "Maintenance Rules" in result

    def test_learning_pathways_has_paths(self, sample_curriculum):
        """Test learning pathways has pathway descriptions."""
        result = render_resource_learning_pathways(sample_curriculum)
        assert "Pathway 1" in result
