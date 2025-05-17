from agents.base_agent import BaseAgent

OUTLINE_PROMPT = ("You are a creative writing planner. Outline a story about \"{concept}\". "
                  "Include key plot points from introduction to conclusion, with bullet points.")
class OutlineAgent(BaseAgent):
    def __init__(self, llm_provider):
        super().__init__("OutlineAgent", llm_provider, OUTLINE_PROMPT)
    def generate_outline(self, concept: str) -> str:
        return self.run(concept=concept)
