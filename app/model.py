import google.generativeai as genai
import time
from app import config  # This will load the API key configuration

# Use Gemini 1.5 Flash model (different quota limits)
print("🔧 Initializing Gemini 1.5 Flash model...")
model = genai.GenerativeModel("gemini-1.5-flash")
print("✅ Model initialized successfully")

# Rate limiting
last_request_time = 0
MIN_REQUEST_INTERVAL = 2  # seconds between requests

def generate_reply(prompt: str) -> str:
    global last_request_time
    
    try:
        # Rate limiting
        current_time = time.time()
        time_since_last = current_time - last_request_time
        if time_since_last < MIN_REQUEST_INTERVAL:
            wait_time = MIN_REQUEST_INTERVAL - time_since_last
            print(f"⏳ Rate limiting: waiting {wait_time:.1f} seconds...")
            time.sleep(wait_time)
        
        print(f"🤖 Generating response for: {prompt[:50]}...")
        response = model.generate_content(prompt)
        result = response.text.strip()
        print(f"✅ Response generated successfully")
        
        last_request_time = time.time()
        return result
    except Exception as e:
        print(f"❌ API Error: {e}")
        if "429" in str(e) or "quota" in str(e).lower():
            return "Sorry, I've hit my daily limit. Please try again later or wait a few minutes between requests."
        return f"Sorry, I encountered an error: {str(e)}"
