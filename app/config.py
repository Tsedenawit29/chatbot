import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Loads .env

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
