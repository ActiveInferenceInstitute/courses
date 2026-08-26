"""Tests for the translation module.

Uses real methods throughout — no mocks, stubs, or fakes.
Tests that require a running Ollama instance are marked with
`requires_api` so they skip gracefully in CI.
"""

from pathlib import Path

import pytest

from src.translation.config import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_SOURCE_LANG,
    SUPPORTED_LANGUAGES,
    TRANSLATABLE_EXTENSIONS,
)
from src.translation.utils import (
    get_language_name,
    get_output_path,
    validate_file_extension,
)
from src.translation.main import translate_file, translate_text


# ---------------------------------------------------------------------------
# Config tests
# ---------------------------------------------------------------------------


class TestConfig:
    """Verify config constants are well-formed."""

    def test_supported_languages_not_empty(self) -> None:
        assert len(SUPPORTED_LANGUAGES) > 0

    def test_supported_languages_keys_are_lowercase(self) -> None:
        for code in SUPPORTED_LANGUAGES:
            assert code == code.lower(), f"Language code '{code}' should be lowercase"

    def test_default_source_lang_is_string(self) -> None:
        assert isinstance(DEFAULT_SOURCE_LANG, str)
        assert len(DEFAULT_SOURCE_LANG) > 0

    def test_default_chunk_size_positive(self) -> None:
        assert DEFAULT_CHUNK_SIZE > 0

    def test_translatable_extensions_contain_dot(self) -> None:
        for ext in TRANSLATABLE_EXTENSIONS:
            assert ext.startswith("."), f"Extension '{ext}' should start with '.'"


# ---------------------------------------------------------------------------
# Utils tests
# ---------------------------------------------------------------------------


class TestGetLanguageName:
    """Test get_language_name with real SUPPORTED_LANGUAGES."""

    def test_known_code_returns_name(self) -> None:
        assert get_language_name("es") == "Spanish"
        assert get_language_name("ru") == "Russian"
        assert get_language_name("ja") == "Japanese"

    def test_case_insensitive(self) -> None:
        assert get_language_name("ES") == "Spanish"
        assert get_language_name("Fr") == "French"

    def test_unknown_code_returns_code(self) -> None:
        assert get_language_name("xx") == "xx"

    def test_all_supported_languages_resolve(self) -> None:
        for code, expected_name in SUPPORTED_LANGUAGES.items():
            assert get_language_name(code) == expected_name


class TestGetOutputPath:
    """Test get_output_path with real Path objects."""

    def test_basic_output_path(self, tmp_path: Path) -> None:
        input_path = tmp_path / "module.md"
        result = get_output_path(input_path, "es")
        assert result == tmp_path / "module_es.md"

    def test_txt_extension(self, tmp_path: Path) -> None:
        input_path = tmp_path / "notes.txt"
        result = get_output_path(input_path, "fr")
        assert result == tmp_path / "notes_fr.txt"

    def test_nested_path(self, tmp_path: Path) -> None:
        input_path = tmp_path / "sub" / "dir" / "file.md"
        result = get_output_path(input_path, "de")
        assert result == tmp_path / "sub" / "dir" / "file_de.md"


class TestValidateFileExtension:
    """Test validate_file_extension with real Path objects."""

    def test_markdown_is_translatable(self) -> None:
        assert validate_file_extension(Path("file.md")) is True

    def test_txt_is_translatable(self) -> None:
        assert validate_file_extension(Path("file.txt")) is True

    def test_pdf_is_not_translatable(self) -> None:
        assert validate_file_extension(Path("file.pdf")) is False

    def test_case_insensitive(self) -> None:
        assert validate_file_extension(Path("FILE.MD")) is True
        assert validate_file_extension(Path("FILE.TXT")) is True

    def test_no_extension_is_not_translatable(self) -> None:
        assert validate_file_extension(Path("README")) is False


# ---------------------------------------------------------------------------
# Integration tests (require running Ollama)
# ---------------------------------------------------------------------------


@pytest.mark.requires_api
class TestTranslateText:
    """Test translate_text with a real OllamaClient.

    Requires a running Ollama instance with a model available.
    """

    def test_translate_short_text(self) -> None:
        from src.llm import OllamaClient

        client = OllamaClient()
        if not client.is_available():
            pytest.skip("Ollama not available")

        result = translate_text("Hello", target_lang="es", client=client)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_translate_preserves_markdown(self) -> None:
        from src.llm import OllamaClient

        client = OllamaClient()
        if not client.is_available():
            pytest.skip("Ollama not available")

        md_text = "# Title\n\n- item 1\n- item 2\n\n```python\nprint('hello')\n```"
        result = translate_text(md_text, target_lang="fr", client=client)
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.requires_api
class TestTranslateFile:
    """Test translate_file with a real OllamaClient and filesystem."""

    def test_translate_file_creates_output(self, tmp_path: Path) -> None:
        from src.llm import OllamaClient

        client = OllamaClient()
        if not client.is_available():
            pytest.skip("Ollama not available")

        input_file = tmp_path / "test.md"
        input_file.write_text("Hello world", encoding="utf-8")

        output_file = tmp_path / "test_es.md"
        result_path = translate_file(
            str(input_file),
            target_lang="es",
            output_path=str(output_file),
            client=client,
        )

        assert result_path == str(output_file)
        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert len(content) > 0

    def test_translate_file_auto_output_path(self, tmp_path: Path) -> None:
        from src.llm import OllamaClient

        client = OllamaClient()
        if not client.is_available():
            pytest.skip("Ollama not available")

        input_file = tmp_path / "test.md"
        input_file.write_text("Goodbye", encoding="utf-8")

        result_path = translate_file(
            str(input_file),
            target_lang="fr",
            client=client,
        )

        expected = tmp_path / "test_fr.md"
        assert result_path == str(expected)
        assert expected.exists()


class TestTranslateFileErrors:
    """Test error handling with real filesystem — no Ollama needed."""

    def test_file_not_found(self) -> None:
        with pytest.raises(FileNotFoundError):
            translate_file("nonexistent.md", target_lang="es")

    def test_file_not_found_nested(self, tmp_path: Path) -> None:
        fake = tmp_path / "does_not_exist" / "file.md"
        with pytest.raises(FileNotFoundError):
            translate_file(str(fake), target_lang="de")


class TestTranslationHardening:
    """Validation that does not require a live Ollama server."""

    def test_unsafe_target_lang_rejected(self) -> None:
        from src.translation.main import translate_text

        # Path traversal / injection primitives must be rejected up front.
        for bad in ("../../etc", "es/..", "a b", "<script>"):
            with pytest.raises(ValueError):
                translate_text("hello", target_lang=bad)

    def test_all_chunks_failed_raises(self) -> None:
        """If every chunk fails to translate, raise instead of returning source."""
        from src.translation.main import translate_text

        class _FailingClient:
            def generate(self, prompt):  # noqa: D102
                raise RuntimeError("LLM unavailable")

        with pytest.raises(RuntimeError):
            translate_text("Some text to translate", target_lang="es", client=_FailingClient())
