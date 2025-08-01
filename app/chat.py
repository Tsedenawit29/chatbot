from app.memory import get_similar_history, store_chat_message
from app.model import generate_reply

def chatbot_response(user_input: str) -> str:
    context = "\n\n".join(get_similar_history(user_input))
    prompt = f"{context}\n\nUser: {user_input}\nBot:"
    bot_reply = generate_reply(prompt)
    store_chat_message(user_input, bot_reply)
    return bot_reply
