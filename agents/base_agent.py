# base_agent.py
class BaseAgent:
    def __init__(self, name: str, llm_provider, prompt_template: str):
        self.name = name
        self.llm = llm_provider  # e.g., an instance of OpenAIProvider or similar
        self.prompt_template = prompt_template

    def run(self, **kwargs) -> str:
        """Fill the prompt template with context and get LLM output."""
        prompt = self.prompt_template.format(**kwargs)
        system_prompt = f"You are {self.name}. Follow these instructions carefully."
        result = self.llm.generate_text(system_prompt, prompt)
        print(f"[{self.name}] Output:\n{result}\n")  # simple logging
        return result
