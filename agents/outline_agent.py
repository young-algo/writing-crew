from agents.base_agent import BaseAgent
from prompt_loader import load_prompt


OUTLINE_PROMPT = load_prompt("outline_prompt.txt")
class OutlineAgent(BaseAgent):
    def __init__(self, llm_provider):
        super().__init__("OutlineAgent", llm_provider, OUTLINE_PROMPT)
    def generate_outline(self, concept: str) -> str:
        return self.run(concept=concept)
