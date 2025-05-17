from agents.base_agent import BaseAgent

DRAFT_PROMPT = ("Write a detailed story following this outline:\n{outline}\n\n"
                "Story Draft:\n")
REVISE_PROMPT = ("Here is a story draft and some feedback.\nOutline:\n{outline}\n"
                 "Current Draft:\n{draft}\n\nFeedback:\n{feedback}\n\n"
                 "Revise the draft incorporating the feedback while maintaining the story's style and coherence. Provide the full revised story.")
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
