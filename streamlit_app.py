import streamlit as st
from datetime import datetime
from app import config
from app.chat import chatbot_response
from streamlit_extras.stylable_container import stylable_container
from uuid import uuid4

# Initialize session state
if "sessions" not in st.session_state:
    st.session_state.sessions = {}  # {session_id: [(role, message, timestamp)]}
if "current_session" not in st.session_state:
    st.session_state.current_session = str(uuid4())

def start_new_chat():
    st.session_state.current_session = str(uuid4())

def add_to_chat(role, message):
    session_id = st.session_state.current_session
    timestamp = datetime.now().strftime("%H:%M")
    if session_id not in st.session_state.sessions:
        st.session_state.sessions[session_id] = []
    st.session_state.sessions[session_id].append((role, message, timestamp))

# Sidebar
with st.sidebar:
    st.title("📚 Chat History")
    st.button("➕ New Chat", on_click=start_new_chat)
    
    # Show list of past chats
    for session_id, messages in st.session_state.sessions.items():
        first_msg = messages[0][1] if messages else "Empty"
        label = first_msg[:30] + "..." if len(first_msg) > 30 else first_msg
        if st.button(f"💬 {label}", key=session_id):
            st.session_state.current_session = session_id

# Chat interface
st.title("💬 Gemini Chatbot")
user_input = st.chat_input("Ask something...")

if user_input:
    bot_reply = chatbot_response(user_input)
    add_to_chat("user", user_input)
    add_to_chat("bot", bot_reply)

# Display chat history
session_id = st.session_state.current_session
if session_id in st.session_state.sessions:
    # Show welcome message if chat is empty
    if not st.session_state.sessions[session_id]:
        with st.chat_message("bot", avatar="🤖"):
            st.markdown(
                "**👋 Welcome to Gemini Chatbot!**\n\n"
                "I'm your intelligent assistant powered by Google's Gemini. "
                "Ask me anything — from tech help to creative writing. 💡\n\n"
                "_What can I help you with today?_"
            )
    else:
        for i, (role, message, timestamp) in enumerate(st.session_state.sessions[session_id]):
            with st.chat_message(role, avatar="👤" if role == "user" else "🤖"):
                with stylable_container(
                    key=f"{role}_{timestamp}_{i}",
                    css_styles="opacity: 0.9; padding: 6px 10px; border-radius: 8px;"
                ):
                    st.markdown(
                        f"{message}  \n"
                        f"<span style='font-size:10px; color:gray;'>{timestamp}</span>",
                        unsafe_allow_html=True
                    )
