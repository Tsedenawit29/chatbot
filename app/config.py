import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Loads .env

# Get API key and validate
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini API
genai.configure(api_key=api_key)
