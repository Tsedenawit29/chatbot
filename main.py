from app import config  # Loads environment and config
from app.chat import chatbot_response

def run_cli():
    print("💬 Gemini Chatbot with Chroma Memory (CLI mode). Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chatbot_response(user_input)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    run_cli()
