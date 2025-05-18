# orchestrator.py
from agents.outline_agent import OutlineAgent
from agents.draft_agent import DraftAgent
from agents.critique_agent import CritiqueAgent
from llm_providers.google_provider import GoogleProvider
from llm_providers.openai_provider import OpenAIProvider
from llm_providers.anthropic_provider import AnthropicProvider
from llm_providers.openrouter_provider import OpenRouterProvider
import config
import os

def run_story_generation(concept: str):
    # Set environment variables for API keys
    os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY
    os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
    os.environ["ANTHROPIC_API_KEY"] = config.ANTHROPIC_API_KEY
    os.environ["OPENROUTER_API_KEY"] = config.OPENROUTER_API_KEY

    # Initialize LLM provider instances
    outline_llm = GoogleProvider(model_name=config.GOOGLE_MODEL)
    # draft_llm = OpenAIProvider(model_name=config.OPENAI_MODEL)
    draft_llm = OpenRouterProvider(model_name=config.OPENROUTER_MODEL)
    critique_llm = AnthropicProvider(model_name=config.ANTHROPIC_MODEL)
    # Create agent instances
    outline_agent = OutlineAgent(outline_llm)
    draft_agent   = DraftAgent(draft_llm)
    critique_agent = CritiqueAgent(critique_llm)
    # 1. Generate outline
    outline = outline_agent.generate_outline(concept)
    # 2. Generate first draft
    draft = draft_agent.write_draft(outline)
    # 3. Iterative critique and revision
    for i in range(config.MAX_ITERATIONS):
        feedback = critique_agent.critique_draft(outline, draft)
        print(f"Iteration {i+1} Feedback:\n{feedback}\n")
        # (Optional) check if feedback indicates no changes needed, then break
        draft = draft_agent.revise_draft(outline, draft, feedback)
        print(f"Iteration {i+1} Revised Draft:\n{draft[:200]}... \n")  # log first part
    # Final output
    return draft

if __name__ == "__main__":
    story_concept = "Charlie Laube, an adorable four-year old all-brown lagotto romagnolo that thinks in English but can't speak to humans" \
    "is charged with murder of several stuffed animal dinosaurs" \
    "and her owners (Kevin and Simone) are called to trial as character witnesses. " \
    "Kevin is also very funny" \
    "Charlie is ultimately acquitted of her _crimes_."  # example concept
    final_story = run_story_generation(story_concept)
    print("Final Story:\n", final_story)
