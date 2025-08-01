# 💬 Gemini Chatbot

A smart, conversational chatbot powered by **Google Gemini Pro** with **semantic memory** using **Chroma vector store** and **LangChain**. Designed with a clean **Streamlit UI**, it supports multiple chat sessions, memory recall, and a professional welcome experience.

---

## 🚀 Features

* 🔎 **Semantic memory with ChromaDB**: Retrieves previous messages similar to your current question.
* 🧠 **Gemini Pro API**: Powered by Google’s latest language model.
* 💬 **Multi-session support**: Start new chats, view past ones in the sidebar.
* 🎨 **Streamlit UI**: Modern, responsive chat interface.
* 📝 **Welcome prompt**: Personalized message when starting a new conversation.

---

## 📁 Project Structure

```
├── app/
│   ├── chat.py           # Handles chatbot response logic
│   ├── memory.py         # Vectorstore-based memory storage/retrieval
│   └── config.py         # (optional) API key or settings management
├── chroma_chat_memory/   # Chroma's vector database directory
├── streamlit_app.py      # Main Streamlit UI
├── main.py               # Optional CLI interface
├── Dockerfile            # Docker container build instructions
├── docker-compose.yml    # Optional: used earlier with Redis
├── requirements.txt      # Python dependencies
└── README.md             # Project info
```

---

## ⚙️ Setup Instructions

### 1. 🔑 Configure API Key

Create a `.env` file and add your [Gemini API key](https://makersuite.google.com/app/apikey):

```
GOOGLE_API_KEY=your_api_key_here
```

Or export it in your environment:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

---

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure these are in your `requirements.txt`:

```txt
streamlit
langchain
langchain-community
google-generativeai
chromadb
streamlit-extras
```

---

### 3. 🧪 Run the App

```bash
streamlit run streamlit_app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🐳 Docker (Optional)

If you want to run in a container:

1. **Build the image**

```bash
docker build -t gemini-chatbot .
```

2. **Run the container**

```bash
docker run -p 8501:8501 --env-file .env gemini-chatbot
```

---

## 🛠 How It Works

* Each user message is embedded using **GoogleGenerativeAIEmbeddings**
* Stored in **Chroma vector store**
* When a user asks a new question:

  * Recent, similar messages are retrieved
  * Used as **context** for Gemini’s next response
* The result is a more memory-aware chatbot with better continuity


