"""
Wrapper for Anthropic Claude API calls.
"""
import os

class AnthropicProvider:
    """
    Provider for Anthropic's Claude model.
    Handles API calls to Anthropic's language models.
    """
    
    def __init__(self, model_name="claude-3-7-sonnet-20250219"):
        """
        Initialize the Anthropic provider.
        
        Args:
            model_name (str): The model to use (default: claude-3-7-sonnet-20250219)
        """
        self.model_name = model_name
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set.")
        
        # Import here to avoid requiring the package if not using this provider
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
            # Validate that we're using a supported model
            if not self.model_name.startswith("claude-"):
                print(f"Warning: {self.model_name} may not be a valid Claude model name.")
        except ImportError:
            raise ImportError(
                "Anthropic package is not installed. "
                "Please install it using 'pip install anthropic'."
            )
    
    def generate_text(self, system_prompt, user_prompt, temperature=0.3, max_tokens=25000):
        """
        Generate text using the Anthropic API.
        
        Args:
            system_prompt (str): The system prompt to guide the model's behavior
            user_prompt (str): The user prompt/question
            temperature (float): Controls randomness (0 to 1)
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            str: The generated text response
        """
        try:
            response = self.client.messages.create(
                model=self.model_name,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.content[0].text
        except Exception as e:
            # Log the error and return an error message
            print(f"Error generating text with Anthropic: {e}")
            return f"Error generating text: {str(e)}"
