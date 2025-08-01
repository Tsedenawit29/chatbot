import google.generativeai as genai

# Instantiate Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def generate_reply(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()
