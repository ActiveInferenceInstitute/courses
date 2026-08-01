"""Utility functions for text-to-speech generation."""

import re
from pathlib import Path
from typing import Optional


def read_text_file(file_path: Path) -> str:
    """Read text file content.

    Args:
        file_path: Path to text file

    Returns:
        File content as string

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Text file not found: {file_path}")

    return file_path.read_text(encoding="utf-8")


def extract_text_from_markdown(markdown_text: str) -> str:
    """Extract plain text from Markdown content.

    Args:
        markdown_text: Markdown content

    Returns:
        Plain text content
    """
    # Remove markdown syntax
    # Remove headers
    text = re.sub(r"^#+\s+", "", markdown_text, flags=re.MULTILINE)
    # Remove links but keep text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove images
    text = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", "", text)
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Remove bold/italic markers
    text = re.sub(r"\*\*([^\*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^\*]+)\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    # Remove horizontal rules
    text = re.sub(r"^---+\s*$", "", text, flags=re.MULTILINE)
    # Remove list markers
    text = re.sub(r"^[\*\-\+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
    # Clean up extra whitespace
    text = re.sub(r"\n\s*\n\s*\n", "\n\n", text)
    text = text.strip()

    return text


def text_to_speech_audio(
    text: str,
    output_path: Path,
    lang: str = "en",
    slow: bool = False,
) -> None:
    """Generate speech audio from text using gTTS (cross-platform).

    Uses the real ``gTTS`` library (per the documented dependency) so ``lang``
    and ``slow`` are honored and output works on any platform, not just macOS.

    Args:
        text: Text content to convert
        output_path: Path for output audio file
        lang: Language code (default: "en")
        slow: Whether to speak slowly (default: False)

    Raises:
        OSError: If audio generation fails
    """
    from gtts import gTTS

    try:
        tts = gTTS(text=text, lang=lang or "en", slow=slow)
        tts.save(str(output_path))
    except Exception as e:
        raise OSError(f"TTS generation failed: {e}") from e


def ensure_output_directory(output_path: Path) -> None:
    """Ensure output directory exists.

    Args:
        output_path: Path to output file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)


def get_output_path(input_path: Path, output_dir: Optional[Path] = None) -> Path:
    """Get output audio path from input text path.

    Args:
        input_path: Path to input text file
        output_dir: Optional output directory (if None, uses input directory)

    Returns:
        Path to output audio file
    """
    if output_dir is None:
        output_dir = input_path.parent

    output_filename = input_path.stem + ".mp3"
    return output_dir / output_filename
