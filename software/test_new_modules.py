
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path.cwd() / "software"))

from src.llm import OllamaClient
from src.llm.utils import estimate_tokens, split_text_into_chunks

def test_llm_utils():
    print("Testing LLM Utils...")
    text = "Hello world. " * 100
    tokens = estimate_tokens(text)
    print(f"Estimated tokens: {tokens}")
    
    chunks = list(split_text_into_chunks(text, max_tokens=20))
    print(f"Split into {len(chunks)} chunks")
    assert len(chunks) > 1
    print("LLM Utils Check Passed")

def test_translation_import():
    print("Testing Translation Import...")
    from src.translation import translate_text
    print("Translation Import Passed")

if __name__ == "__main__":
    test_llm_utils()
    test_translation_import()
