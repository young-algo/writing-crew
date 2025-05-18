from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROMPT_DIR = BASE_DIR / "prompts"
CONCEPT_DIR = BASE_DIR / "concepts"


def load_prompt(filename: str) -> str:
    """Load a prompt template from the prompts directory."""
    path = PROMPT_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_concept(filename: str) -> str:
    """Load a story concept from the concepts directory."""
    path = CONCEPT_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()
