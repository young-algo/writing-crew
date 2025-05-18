# Writing Crew

A collaborative AI writing system that leverages multiple LLM agents to generate high-quality content.

## Overview

Writing Crew orchestrates multiple AI agents, each powered by a different Large Language Model (LLM), to create well-structured, thoroughly-reviewed content. The system follows a multi-stage process:

1. **Outline Generation** (Google Gemini): Creates a well-structured content outline
2. **Draft Creation** (OpenAI GPT-4): Generates a comprehensive draft based on the outline
3. **Critique & Feedback** (Anthropic Claude): Provides detailed critique and suggestions for improvement
4. **Iterative Refinement**: The system can iteratively improve content through multiple draft/critique cycles

## Project Structure

```
writing-crew/
├── agents/
│   ├── base_agent.py         # Base class for agents (common interface)
│   ├── outline_agent.py      # OutlineAgent class (Gemini)
│   ├── draft_agent.py        # DraftAgent class (GPT-4)
│   ├── critique_agent.py     # CritiqueAgent class (Claude)
├── llm_providers/
│   ├── openai_provider.py    # Wrapper for OpenAI API calls
│   ├── anthropic_provider.py # Wrapper for Anthropic Claude API
│   ├── google_provider.py    # Wrapper for Google Gemini API
│   ├── openrouter_provider.py  # Wrapper for OpenRouter API calls
├── orchestrator.py           # The coordination logic (bringing agents together)
├── config.py                 # Configuration (API keys, model names, etc.)
├── test_all_providers.py     # Script to test all LLM providers
├── test_custom_agent.py      # Script to test a custom agent with OpenRouter
└── README.md                 # This documentation file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/writing-crew.git
   cd writing-crew
   ```

2. Install dependencies using UV:
   First, ensure you have UV installed. If not, you can install it via pip:
   ```bash
   pip install uv
   ```
   Then, create a virtual environment and install dependencies:
   ```bash
   uv venv
   uv pip sync pyproject.toml 
   # or uv pip sync uv.lock if you prefer to use the lock file
   ```
   Activate the virtual environment (the command might vary based on your shell):
   ```bash
   source .venv/bin/activate 
   ```

3. Set up your API keys as environment variables:
   Create a `.env` file in the project root or set environment variables directly.
   Example `.env` file:
   ```
   OPENAI_API_KEY="your_openai_api_key"
   ANTHROPIC_API_KEY="your_anthropic_api_key"
   GOOGLE_API_KEY="your_google_api_key"
   OPENROUTER_API_KEY="your_openrouter_api_key"
   # Optional for OpenRouter provider rankings:
   # SITE_URL="your_site_url" 
   # SITE_NAME="your_site_name"
   ```
   The application uses `python-dotenv` to load these variables.

## Configuration

Edit `config.py` to customize:
- LLM models used by each agent
- Maximum iterations for content refinement
- Content types and audience examples

You can modify the instructions each agent uses by editing the text files in the
`prompts/` directory.
The example story concept used by the orchestrator is stored in `concepts/example_story.txt`.

## Usage

The primary way to use Writing Crew is by running the `orchestrator.py` script. This script coordinates the different LLM agents to generate a story based on a given concept.

### Running from the Command Line

You can run the orchestrator directly from your terminal:

```bash
python orchestrator.py
```

This will use the example story concept loaded from `concepts/example_story.txt`:
```python
# Inside orchestrator.py
if __name__ == "__main__":
    # Load the example story concept from the concepts directory
    story_concept = load_concept("example_story.txt")
    final_story = run_story_generation(story_concept)
    print("Final Story:\n", final_story)
```
The script will then print the final generated story to the console. You can modify the text in `concepts/example_story.txt` to generate different stories.

### Importing and Using in Your Own Scripts

Alternatively, you can import the `run_story_generation` function into your own Python scripts:

```python
from orchestrator import run_story_generation
import config # Ensure config.py is set up with your API keys and model preferences

# Define your story concept
my_concept = "A futuristic detective investigating a crime in a city run by sentient AI."

# Generate the story
final_story_output = run_story_generation(my_concept)

# Print or process the final story
print("Generated Story:\n", final_story_output)
```

**How it Works:**

The `run_story_generation` function in `orchestrator.py`:
1. Initializes the necessary LLM providers (Google for outline, OpenRouter for draft, Anthropic for critique by default, configurable in `orchestrator.py` and `config.py`).
2. Creates instances of the `OutlineAgent`, `DraftAgent`, and `CritiqueAgent`.
3. **Outline Generation**: The `OutlineAgent` generates an initial story outline based on your concept.
4. **Draft Creation**: The `DraftAgent` writes the first draft of the story using the generated outline.
5. **Iterative Refinement**:
   - The `CritiqueAgent` reviews the draft and provides feedback.
   - The `DraftAgent` revises the draft based on this feedback.
   - This critique and revision cycle repeats for a number of iterations defined by `MAX_ITERATIONS` in `config.py`.
6. The final revised draft is returned.

Make sure your API keys are correctly set up in `config.py` (or as environment variables if `config.py` loads them that way) before running the orchestrator.

## Testing

The project includes several test scripts to verify the functionality of the LLM providers and agent integrations:

- **`test_all_providers.py`**: This script tests all configured LLM providers (OpenAI, Anthropic, Google, OpenRouter) by using them with the `OutlineAgent`. It helps ensure that each provider is correctly set up and can communicate with its respective API.
  ```bash
  python test_all_providers.py
  ```
  *(Note: Requires API keys for all tested providers to be set in your environment.)*

- **`test_custom_agent.py`**: This script demonstrates how to create a new custom agent (a `SummaryAgent` in this example) and use it with the `OpenRouterProvider`. It serves as an example of the flexibility of the agent and provider architecture.
  ```bash
  python test_custom_agent.py
  ```
  *(Note: Requires `OPENROUTER_API_KEY` to be set.)*

Before running these tests, ensure you have installed the necessary dependencies using UV as described in the "Installation" section and have the required API keys set.

## License

[MIT License](LICENSE)

