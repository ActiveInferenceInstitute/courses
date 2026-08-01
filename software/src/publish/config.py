"""Configuration for the publish module."""

# Root directory name for published content (relative to repo root)
PUBLISH_ROOT_NAME = "published"

# Configuration for specific courses.
# Key: Course directory name OR COURSE_REGISTRY ID.
# Value: Dict with publish-time options.
#   - module_source_dir:   subdirectory inside each module dir that contains rendered output
#   - syllabus_source_dir: subdirectory inside the syllabus dir that contains rendered output
#   - include_syllabus:    whether to publish the syllabus section
#   - copy_dashboards:     whether to copy dashboard/HTML artifacts alongside content
#   - additional_module_dirs: extra subdirs per module to copy verbatim (e.g. slides)
COURSE_CONFIGS = {
    # -------------------------------------------------------------------------
    # Legacy biology courses (backward-compat — use course/module-* glob)
    # -------------------------------------------------------------------------
    "biol-1": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
    },
    "biol-8": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
    },
    # -------------------------------------------------------------------------
    # Active Inference Institute — core consolidated course
    # -------------------------------------------------------------------------
    "active-inference": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    # -------------------------------------------------------------------------
    # Active Inference — legacy individual sub-course entries (Deprecated)
    # -------------------------------------------------------------------------
    "ai-philosophy": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-cognitive-science": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-math": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-computer-science": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    # -------------------------------------------------------------------------
    # Level-adapted courses
    # -------------------------------------------------------------------------
    "ai-es": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-family": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-ms": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-hs": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-101": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-401": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    # -------------------------------------------------------------------------
    # Domain courses
    # -------------------------------------------------------------------------
    "ai-embodied": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-organizations": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-robotics": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-crochet": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-inventions": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-metallurgy": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    "ai-comedy": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": True,
        "copy_dashboards": True,
    },
    # -------------------------------------------------------------------------
    # YouTube transcript archive
    # -------------------------------------------------------------------------
    "youtube": {
        "module_source_dir": "output",
        "syllabus_source_dir": "output",
        "include_syllabus": False,
        "copy_dashboards": False,
    },
}

# Default configuration for courses not listed above.
DEFAULT_CONFIG = {
    "module_source_dir": "output",
    "syllabus_source_dir": "output",
    "include_syllabus": True,
}

# Subdirectories to exclude during copy
EXCLUDE_PATTERNS = [
    ".DS_Store",
    "Thumbs.db",
    "__pycache__",
    ".git",
]
