# 🛠️ DevOps Chatbot — Hybrid RAG + Realtime Web Search (Groq + Tavily + FAISS)

A powerful DevOps assistant chatbot that answers technical queries using both **static PDF docs** (FAISS) and **real-time web search** (Tavily), built with **LangChain**, **RAG** **Groq's LLaMA3**, **FastAPI**, and **Streamlit**.

---

## 🚀 Features

✅ Real-time DevOps troubleshooting using **Tavily Search API**  
✅ Vector-based search using **FAISS** and DevOps PDFs  
✅ Answer generation using **Groq’s LLaMA3** model  
✅ FastAPI backend for flexible integration  
✅ Streamlit frontend for easy web-based UI  
✅ Dual mode hybrid retrieval (static + web)  
✅ Prompt template & memory support  
✅ Azure VM deployment-ready setup

---

## 📦 Tech Stack

- **LangChain**
- **Groq LLaMA3 (via API)**
- **FAISS**
- **Tavily API** (for real-time web search)
- **FastAPI** (Backend API)
- **Streamlit** (Frontend UI)
- **Python 3.11**
- **Azure VM (B2s)** (Ubuntu 22.04)

---

## 📁 Folder Structure

```bash
DevOps-Chatbot-Hybrid-RAG-Realtime/
├── app.py                     # LangChain logic
├── api.py                     # FastAPI routes
├── streamlit_ui.py            # Streamlit frontend
├── build_vectordb.py          # Converts PDFs to FAISS index
├── tools/
│   ├── tavily_search.py       # Web search tool (Tavily)
├── vectordb/
│   └── index.faiss            # FAISS vectorstore
├── data/
│   └── *.pdf                  # DevOps documentation
├── .env                       # API Keys
├── requirements.txt
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the root directory and add:

```ini
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 🧠 How It Works

1. User enters a DevOps-related query
2. LangChain hybrid retriever fetches:
   - Relevant chunks from FAISS vectorstore (static)
   - Top results from the web using Tavily (dynamic)
3. Combined context is passed to Groq’s LLaMA3 via prompt
4. Final response is shown via Streamlit UI or FastAPI response

---

## ⚙️ Setup Instructions

### 🔧 1. Clone & Install

```bash
git clone https://github.com/your-username/DevOps-Chatbot-Hybrid-RAG-Realtime.git
cd DevOps-Chatbot-Hybrid-RAG-Realtime
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 📚 2. Add DevOps PDFs

Place your DevOps PDF files inside the `data/` folder.

### 🧠 3. Build FAISS Vector DB

```bash
python build_vectordb.py
```

### 🚀 4. Run FastAPI Backend

```bash
uvicorn api:app --reload
```

### 🌐 5. Run Streamlit Frontend

In another terminal:

```bash
streamlit run streamlit_app.py
```

## 🔗 Related Links

- 🔗 Tavily: [https://github.com/tavily/Tavily-python](https://github.com/tavily/Tavily-python)
- 🔗 LangChain: [https://www.langchain.com](https://www.langchain.com)
- 🔗 Groq: [https://console.groq.com](https://console.groq.com)

---

## 👨‍💻 Author

**Saim Qureshi**  
Final Year BSCS Student – SMI University  
Vice President – Science Society | Passionate about LLMs, RAG, and DevOps Automation

---

## 🛡️ License

MIT License
