"""
Test script to create a custom agent using the OpenRouter provider.
This demonstrates that the OpenRouter provider can be used to create new agent types.
"""
import os
from dotenv import load_dotenv
from agents.base_agent import BaseAgent
from llm_providers.openrouter_provider import OpenRouterProvider

# Load environment variables from .env file
load_dotenv()

class SummaryAgent(BaseAgent):
    """
    A custom agent that summarizes content using the OpenRouter provider.
    This demonstrates creating a new agent type with the OpenRouter provider.
    """
    
    def __init__(self, llm_provider):
        """
        Initialize the SummaryAgent.
        
        Args:
            llm_provider: The LLM provider to use (e.g., OpenRouterProvider)
        """
        prompt_template = ("You are a professional summarizer. "
                          "Create a concise summary of the following text: \n\n{text}")
        super().__init__("SummaryAgent", llm_provider, prompt_template)
    
    def summarize(self, text: str) -> str:
        """
        Summarize the provided text.
        
        Args:
            text (str): The text to summarize
            
        Returns:
            str: The summarized text
        """
        return self.run(text=text)

def test_custom_agent_with_openrouter():
    """
    Test creating and using a custom agent with the OpenRouter provider.
    """
    print(f"\n{'='*40}\nTesting Custom Agent with OpenRouter\n{'='*40}")
    
    try:
        # Create OpenRouter provider
        provider = OpenRouterProvider(model_name="openai/gpt-4o")
        
        # Create a custom agent with this provider
        agent = SummaryAgent(provider)
        
        # Sample text to summarize
        sample_text = """
        Artificial intelligence (AI) is intelligence demonstrated by machines, 
        as opposed to natural intelligence displayed by animals including humans. 
        AI research has been defined as the field of study of intelligent agents, 
        which refers to any system that perceives its environment and takes actions 
        that maximize its chance of achieving its goals. The term "artificial intelligence" 
        had previously been used to describe machines that mimic and display human 
        cognitive skills that are associated with the human mind, such as learning 
        and problem-solving. This definition has since been rejected by major AI 
        researchers who now describe AI in terms of rationality and acting rationally, 
        which does not limit how intelligence can be articulated.
        """
        
        print("Generating summary of sample text...")
        summary = agent.summarize(sample_text)
        
        print(f"\nGenerated summary from custom agent:\n{summary}")
        print(f"\nCustom Agent with OpenRouter TEST SUCCESSFUL ✅")
        
        return True
    except Exception as e:
        print(f"\nCustom Agent with OpenRouter TEST FAILED ❌")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("TESTING CUSTOM AGENT WITH OPENROUTER PROVIDER")
    print("\nNote: This test requires the OPENROUTER_API_KEY environment variable to be set.")
    
    # Run the test
    test_custom_agent_with_openrouter()
