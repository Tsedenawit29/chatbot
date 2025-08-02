import google.generativeai as genai
from app import config  # This will load the API key configuration

# Use Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_reply(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"API Error: {e}")
        return f"Sorry, I encountered an error: {str(e)}"
