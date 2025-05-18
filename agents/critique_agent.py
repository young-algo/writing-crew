from agents.base_agent import BaseAgent
from prompt_loader import load_prompt


CRITIQUE_PROMPT = load_prompt("critique_prompt.txt")

class CritiqueAgent(BaseAgent):
    def __init__(self, llm_provider):
        super().__init__("CritiqueAgent", llm_provider, CRITIQUE_PROMPT)
    def critique_draft(self, outline: str, draft: str) -> str:
        return self.run(outline=outline, draft=draft)
