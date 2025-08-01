from langchain.vectorstores import Chroma
from langchain.embeddings import GoogleGenerativeAIEmbeddings

embedding_function = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma(persist_directory="./chroma_chat_memory", embedding_function=embedding_function)

def store_chat_message(user_msg, bot_msg):
    combined = f"User: {user_msg}\nBot: {bot_msg}"
    vectorstore.add_texts([combined])

def get_similar_history(query, k=3):
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
