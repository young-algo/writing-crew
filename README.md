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
│   ├── openai_provider.py    # Wrapper for OpenAI GPT-4 API calls
│   ├── anthropic_provider.py # Wrapper for Anthropic Claude API
│   ├── google_provider.py    # Wrapper for Google Gemini API
├── orchestrator.py           # The coordination logic (bringing agents together)
├── config.py                 # Configuration (API keys, model names, etc.)
└── README.md                 # This documentation file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/writing-crew.git
   cd writing-crew
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys as environment variables:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   export GOOGLE_API_KEY=your_google_api_key
   ```

## Configuration

Edit `config.py` to customize:
- LLM models used by each agent
- Maximum iterations for content refinement
- Default prompts for each agent
- Content types and audience examples

## Usage Examples

### Basic Usage

```python
from orchestrator import Orchestrator

# Initialize the orchestrator
orchestrator = Orchestrator()

# Run the basic pipeline (one pass through all agents)
result = orchestrator.run_pipeline(
    topic="Artificial Intelligence Ethics",
    audience="general_readers",
    content_type="article",
    outline_prompt="Create a comprehensive outline for an article about AI ethics.",
    draft_prompt="Write a detailed draft based on the provided outline.",
    critique_prompt="Provide detailed feedback on this draft."
)

# Access the results
print("OUTLINE:")
print(result['outline'])
print("\nDRAFT:")
print(result['draft'])
print("\nCRITIQUE:")
print(result['critique'])
```

### Iterative Refinement

```python
# Run the iterative pipeline with multiple refinement cycles
result = orchestrator.run_iterative_pipeline(
    topic="Machine Learning for Beginners",
    audience="beginners",
    content_type="tutorial",
    outline_prompt="Create a beginner-friendly tutorial outline about machine learning.",
    draft_prompt="Write an approachable tutorial based on the outline.",
    critique_prompt="Identify areas where the tutorial could be clearer or more beginner-friendly.",
    revision_prompt="Revise the tutorial to be more accessible to beginners."
)

# Access the final draft
print("FINAL DRAFT:")
print(result['final_draft'])

# Or examine the entire iteration history
for i, iteration in enumerate(result['iterations']):
    print(f"ITERATION {i+1}:")
    print(f"Draft:\n{iteration['draft'][:500]}...\n")
    print(f"Critique:\n{iteration['critique'][:500]}...\n")
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
