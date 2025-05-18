from agents.base_agent import BaseAgent
from prompt_loader import load_prompt


DRAFT_PROMPT = load_prompt("draft_prompt.txt")
REVISE_PROMPT = load_prompt("revise_prompt.txt")
class DraftAgent(BaseAgent):
    def __init__(self, llm_provider):
        super().__init__("DraftAgent", llm_provider, DRAFT_PROMPT)
    def write_draft(self, outline: str) -> str:
        # Use initial draft prompt
        self.prompt_template = DRAFT_PROMPT
        return self.run(outline=outline)
    def revise_draft(self, outline: str, draft: str, feedback: str) -> str:
        # Use revision prompt template
        self.prompt_template = REVISE_PROMPT
        return self.run(outline=outline, draft=draft, feedback=feedback)
