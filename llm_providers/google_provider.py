"""
Wrapper for Google Gemini API calls.
"""
import os

class GoogleProvider:
    """
    Provider for Google's Gemini model.
    Handles API calls to Google's language models.
    """
    
    def __init__(self, model_name="gemini-2.5-pro-preview-03-25"):
        """
        Initialize the Google provider.
        
        Args:
            model_name (str): The model to use (default: gemini-2.5-pro-preview-03-25)
        """
        self.model_name = model_name
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        
        # Import here to avoid requiring the package if not using this provider
        try:
            from google import genai
            from google.genai import types
            self.genai = genai
            self.types = types
            self.client = genai.Client(api_key=self.api_key)
        except ImportError:
            raise ImportError(
                "Google Generative AI package is not installed. "
                "Please install it using 'pip install google-genai'."
            )
    
    def generate_text(self, system_prompt, user_prompt, temperature=0.5, max_tokens=25000):
        """
        Generate text using the Google Gemini API.
        
        Args:
            system_prompt (str): The system prompt to guide the model's behavior
            user_prompt (str): The user prompt/question
            temperature (float): Controls randomness (0 to 1)
            max_tokens (int): Maximum number of tokens to generate
            
        Returns:
            str: The generated text response
        """
        try:
            # Use the updated API approach with client.models.generate_content
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[
                    self.types.Content(
                        role="model",
                        parts=[self.types.Part(text=system_prompt)]
                    ),
                    self.types.Content(
                        role="user",
                        parts=[self.types.Part(text=user_prompt)]
                    )
                ],
                config=self.types.GenerateContentConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    top_p=0.95,
                    top_k=40,
                )
            )
            
            return response.text
        except Exception as e:
            # Log the error and return an error message
            print(f"Error generating text with Google Gemini: {e}")
            return f"Error generating text: {str(e)}"
