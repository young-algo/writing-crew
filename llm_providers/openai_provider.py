"""
Wrapper for OpenAI GPT-4 API calls.
"""
import os

class OpenAIProvider:
    """
    Provider for OpenAI's GPT-4 model.
    Handles API calls to OpenAI's language models.
    """
    
    def __init__(self, model_name="gpt-4o"):
        """
        Initialize the OpenAI provider.
        
        Args:
            model_name (str): The model to use (default: gpt-4o)
        """
        self.model_name = model_name
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        
        # Import here to avoid requiring the package if not using this provider
        try:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError(
                "OpenAI package is not installed. "
                "Please install it using 'pip install openai'."
            )
    
    def generate_text(self, system_prompt, user_prompt, temperature=0.7, max_tokens=25000):
        """
        Generate text using the OpenAI API.
        
        Args:
            system_prompt (str): The system prompt to guide the model's behavior
            user_prompt (str): The user prompt/question
            temperature (float): Controls randomness (0 to 1)
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            str: The generated text response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
        except Exception as e:
            # Log the error and return an error message
            print(f"Error generating text with OpenAI: {e}")
            return f"Error generating text: {str(e)}"
