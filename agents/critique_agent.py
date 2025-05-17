from agents.base_agent import BaseAgent

CRITIQUE_PROMPT = ("You are a story critic. You will be given a story draft and its outline. "
                   "Provide a constructive critique of the draft. Identify any issues with plot, characters, consistency, and style. "
                   "Also mention what is done well. Be clear and concise in your feedback.\n\n"
                   "Outline:\n{outline}\n\nDraft:\n{draft}\n\nCritique:")

class CritiqueAgent(BaseAgent):
    def __init__(self, llm_provider):
        super().__init__("CritiqueAgent", llm_provider, CRITIQUE_PROMPT)
    def critique_draft(self, outline: str, draft: str) -> str:
        return self.run(outline=outline, draft=draft)
