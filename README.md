# 💬 Gemini Chatbot with Memory

A powerful conversational AI chatbot built with Google's Gemini AI, featuring persistent memory using ChromaDB and a beautiful Streamlit interface.

## ✨ Features

- 🤖 **AI-Powered Conversations**: Powered by Google's Gemini 1.5 Flash model
- 🧠 **Persistent Memory**: Remembers conversation history using ChromaDB
- 💬 **Multi-Session Support**: Create and switch between different chat sessions
- 🎨 **Beautiful UI**: Modern Streamlit interface with chat bubbles and timestamps
- 🔄 **Real-time Responses**: Instant AI responses with context awareness
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key
- Docker (optional)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd chatbot
```

### 2. Set Up Environment

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your API key from: https://makersuite.google.com/app/apikey

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

#### Option A: Local Development
```bash
streamlit run streamlit_app.py
```

#### Option B: Docker (Recommended)
```bash
docker compose up --build
```

The application will be available at: http://localhost:8501

## 🏗️ Project Structure

```
chatbot/
├── app/
│   ├── config.py          # API key configuration
│   ├── model.py           # Gemini AI model setup
│   ├── memory.py          # ChromaDB memory management
│   └── chat.py            # Chat logic and response generation
├── streamlit_app.py       # Main Streamlit application
├── main.py               # CLI version of the chatbot
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker configuration
├── Dockerfile           # Docker image setup
└── .env                 # Environment variables (create this)
```

## 🔧 Configuration

### Model Configuration

The chatbot uses `gemini-1.5-flash` for text generation and `models/embedding-001` for memory embeddings.

### Memory Storage

Chat history is stored in the `./chroma_chat_memory` directory and persists between sessions.

## 🐳 Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker compose up --build

# Run in background
docker compose up -d

# Stop the application
docker compose down
```

### Docker Configuration

- **Port**: 8501
- **Volume**: `./chroma_chat_memory` for persistent memory
- **Environment**: Loads from `.env` file

## 🧪 Testing

The chatbot is ready to use! Simply run the application and start chatting.

## 📦 Dependencies

### Core Dependencies
- `streamlit` - Web interface
- `google-generativeai` - Gemini AI integration
- `langchain-google-genai` - LangChain integration
- `langchain-chroma` - Vector database for memory
- `chromadb` - Embedding storage
- `python-dotenv` - Environment variable management

### UI Dependencies
- `streamlit-extras` - Enhanced UI components
- `tiktoken` - Token counting

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains the correct API key
   - Verify the API key is valid at Google AI Studio

2. **Model Not Found Error**
   - The chatbot uses `gemini-1.5-flash` which should be available with most API keys
   - Check your API key permissions

3. **Memory Issues**
   - Ensure the `./chroma_chat_memory` directory is writable
   - Clear the directory if memory becomes corrupted

4. **Docker Network Issues**
   - Try running locally first: `streamlit run streamlit_app.py`
   - Use a different network or VPN if Docker fails

### Network Timeout Solutions

If you experience network timeouts during installation:

```bash
# Install packages individually with longer timeouts
pip install streamlit==1.47.1 --timeout=600
pip install google-generativeai==0.8.5 --timeout=600
pip install python-dotenv==1.0.1 --timeout=600
pip install langchain-google-genai==2.1.8 --timeout=600
pip install langchain-chroma --timeout=600
pip install chromadb==0.6.3 --timeout=600
```

## 🎯 Usage

1. **Start a New Chat**: Click "➕ New Chat" in the sidebar
2. **Ask Questions**: Type your message in the chat input
3. **View History**: Previous chats appear in the sidebar
4. **Switch Sessions**: Click on any previous chat to continue

## 🔒 Security

- API keys are stored in `.env` file (not committed to git)
- Chat history is stored locally in `./chroma_chat_memory`
- No data is sent to external services except Google AI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Google Gemini AI for the language model
- Streamlit for the web framework
- LangChain for the AI framework
- ChromaDB for vector storage

---

**Made with ❤️ using Google Gemini AI**