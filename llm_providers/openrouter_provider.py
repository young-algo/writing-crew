"""
Wrapper for OpenRouter API calls.
"""
import os

class OpenRouterProvider:
    """
    Provider for OpenRouter API.
    Handles API calls to various language models through OpenRouter.
    """
    
    def __init__(self, model_name="openai/gpt-4o"):
        """
        Initialize the OpenRouter provider.
        
        Args:
            model_name (str): The model to use (default: openai/gpt-4o)
        """
        self.model_name = model_name
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set.")
        
        # Site information for OpenRouter rankings
        self.site_url = os.getenv("SITE_URL", "")
        self.site_name = os.getenv("SITE_NAME", "")
        
        # Import here to avoid requiring the package if not using this provider
        try:
            from openai import OpenAI
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=self.api_key
            )
        except ImportError:
            raise ImportError(
                "OpenAI package is not installed. "
                "Please install it using 'pip install openai'."
            )
    
    def generate_text(self, system_prompt, user_prompt, temperature=0.5, max_tokens=250000):
        """
        Generate text using the OpenRouter API.
        
        Args:
            system_prompt (str): The system prompt to guide the model's behavior
            user_prompt (str): The user prompt/question
            temperature (float): Controls randomness (0 to 1)
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            str: The generated text response
        """
        try:
            # Setup extra headers if site information is available
            extra_headers = {}
            if self.site_url:
                extra_headers["HTTP-Referer"] = self.site_url
            if self.site_name:
                extra_headers["X-Title"] = self.site_name
            
            response = self.client.chat.completions.create(
                extra_headers=extra_headers,
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
            print(f"Error generating text with OpenRouter: {e}")
            return f"Error generating text: {str(e)}"
