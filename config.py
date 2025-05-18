# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Model configurations
OPENAI_MODEL = "gpt-4o"                      
ANTHROPIC_MODEL = "claude-3-7-sonnet-20250219"  
GOOGLE_MODEL = "gemini-2.5-pro-preview-03-25"   
OPENROUTER_MODEL = "openai/o3" 
MAX_ITERATIONS = 2  
