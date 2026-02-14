"""Logging style constants and utilities for visually enhanced pipeline output.

Provides emoji mappings and formatting helpers for consistent, readable logging
across the publish pipeline.
"""

# Format type emoji
FORMAT_EMOJI = {
    "pdf": "📄",
    "docx": "📝",
    "mp3": "🔊",
    "html": "🌐",
    "txt": "📋",
    "md": "📑",
}

# Content type emoji
CONTENT_EMOJI = {
    "module": "📚",
    "syllabus": "📅",
    "lab": "🧪",
    "test": "📝",
    "practice_test": "📝",
    "slide": "🎯",
    "dashboard": "📊",
    "website": "🌐",
}

# Status emoji
STATUS_EMOJI = {
    "success": "✅",
    "warning": "⚠️",
    "error": "❌",
    "processing": "🔄",
    "cleaning": "🧹",
    "validating": "🔍",
    "publishing": "📦",
    "copying": "📋",
    "flattening": "📁",
    "pushing": "🚀",
}

# Step emoji for pipeline stages
STEP_EMOJI = {
    1: "🧹",    # Clean
    1.5: "🧹",  # Clean source
    2: "⚙️",    # Generate
    3: "📦",    # Publish
    4: "📋",    # Copy labs
    4.5: "🎯",  # Copy slides
    5: "📁",    # Flatten
    5.5: "📁",  # Reorganize
    6: "🔍",    # Validate
}


def format_summary(counts: dict, show_zero: bool = False) -> str:
    """Format output counts as a compact emoji-annotated string.
    
    Args:
        counts: Dict mapping format name to count (e.g., {"pdf": 2, "docx": 2})
        show_zero: If False, omit formats with zero count
        
    Returns:
        Compact string like "📄 2  📝 2  📑 2"
    """
    parts = []
    # Order: pdf, docx, md, html, mp3, txt
    format_order = ["pdf", "docx", "md", "html", "mp3", "txt"]
    
    for fmt in format_order:
        count = counts.get(fmt, 0)
        if count > 0 or show_zero:
            emoji = FORMAT_EMOJI.get(fmt, "📄")
            parts.append(f"{emoji} {count}")
    
    return "  ".join(parts) if parts else "—"


def format_module_result(module_name: str, duration: float, counts: dict) -> str:
    """Format a module processing result as a compact one-liner.
    
    Args:
        module_name: Name of the module (e.g., "module-01-study-of-life")
        duration: Processing time in seconds
        counts: Dict mapping format to count
        
    Returns:
        Formatted string like "✅ module-01-study-of-life (0.44s) → 📄 2  📝 2  📑 2"
    """
    summary = format_summary(counts)
    return f"✅ {module_name} ({duration:.2f}s) → {summary}"


def section_header(title: str, emoji: str = "═", width: int = 60) -> str:
    """Create a visually distinct section header.
    
    Args:
        title: Header text
        emoji: Optional leading emoji for the title
        width: Total width of the separator line
        
    Returns:
        Multi-line header string
    """
    separator = "═" * width
    return f"\n{separator}\n{emoji} {title}\n{separator}"


def step_header(step_num: float, title: str) -> str:
    """Create a pipeline step header with appropriate emoji.
    
    Args:
        step_num: Step number (e.g., 1, 1.5, 2)
        title: Step description
        
    Returns:
        Formatted step header like "🧹 STEP 1: Cleaning PUBLISHED directory"
    """
    emoji = STEP_EMOJI.get(step_num, "▶️")
    if step_num == int(step_num):
        return f"\n{emoji} STEP {int(step_num)}: {title}"
    else:
        return f"\n{emoji} STEP {step_num}: {title}"


def validation_status(valid: bool, context: str = "") -> str:
    """Format a validation status with appropriate emoji.
    
    Args:
        valid: Whether validation passed
        context: Additional context (e.g., "17/17 modules")
        
    Returns:
        Formatted status like "✅ 17/17 modules valid"
    """
    emoji = STATUS_EMOJI["success"] if valid else STATUS_EMOJI["error"]
    return f"{emoji} {context}" if context else emoji
