"""Tests for the publish module."""

from pathlib import Path
import pytest
from src.publish.main import publish_course
from src.publish import config

class TestPublishCourse:
    
    def test_publish_biol1_structure(self, temp_dir):
        """Test publishing BIOL-1 structure (uses for_upload)."""
        # Setup mock course
        course_dir = temp_dir / "biol-1"
        course_dir.mkdir()
        
        # Setup module with output
        mod1 = course_dir / "course" / "module-1"
        mod1.mkdir(parents=True)
        (mod1 / "output").mkdir()
        (mod1 / "output" / "test.pdf").write_text("content")
        
        # Setup syllabus with output
        syl = course_dir / "syllabus"
        syl.mkdir()
        (syl / "output").mkdir()
        (syl / "output" / "syllabus.pdf").write_text("syllabus")
        
        # Publish
        publish_root = temp_dir / "PUBLISHED"
        results = publish_course(str(course_dir), str(publish_root))
        
        assert results["course"] == "biol-1"
        assert results["modules_published"] == 1
        assert results["syllabus_files"] == 1
        
        # Verify structure
        assert (publish_root / "biol-1" / "module-1" / "test.pdf").exists()
        assert (publish_root / "biol-1" / "syllabus" / "syllabus.pdf").exists()

    def test_publish_biol8_structure(self, temp_dir):
        """Test publishing BIOL-8 structure (uses output)."""
        # Setup mock course
        course_dir = temp_dir / "biol-8"
        course_dir.mkdir()
        
        # Setup module with output
        mod1 = course_dir / "course" / "module-1"
        mod1.mkdir(parents=True)
        (mod1 / "output").mkdir()
        (mod1 / "output" / "gen.pdf").write_text("content")
        
        # Publish
        publish_root = temp_dir / "PUBLISHED"
        results = publish_course(str(course_dir), str(publish_root))
        
        assert results["course"] == "biol-8"
        assert results["modules_published"] == 1
        
        # Verify structure
        assert (publish_root / "biol-8" / "module-1" / "gen.pdf").exists()
        
    def test_clean_directory(self, temp_dir):
        """Test that destination is cleaned before publishing."""
        course_dir = temp_dir / "biol-1"
        course_dir.mkdir()
        mod1 = course_dir / "course" / "module-1" / "output"
        mod1.mkdir(parents=True)
        (mod1 / "new.pdf").write_text("new")
        
        publish_root = temp_dir / "PUBLISHED"
        dest_mod = publish_root / "biol-1" / "module-1"
        dest_mod.mkdir(parents=True)
        (dest_mod / "old.pdf").write_text("old")
        
        publish_course(str(course_dir), str(publish_root))
        
        assert (dest_mod / "new.pdf").exists()
        assert not (dest_mod / "old.pdf").exists()
