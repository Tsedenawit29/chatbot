from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app import config  # This will load the API key configuration

# Configure embeddings with API key
embedding_function = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=config.api_key
)
vectorstore = Chroma(persist_directory="./chroma_chat_memory", embedding_function=embedding_function)

def store_chat_message(user_msg, bot_msg):
    try:
        combined = f"User: {user_msg}\nBot: {bot_msg}"
        vectorstore.add_texts([combined])
    except Exception as e:
        print(f"Error storing chat message: {e}")

def get_similar_history(query, k=3):
    try:
        docs = vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
    except Exception as e:
        print(f"Error retrieving similar history: {e}")
        return []
