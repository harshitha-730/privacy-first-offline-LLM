# 📁 Local Document Intelligent RAG Engine

A privacy-focused, 100% offline Retrieval-Augmented Generation (RAG) assistant that allows users to securely chat with sensitive PDF documents (such as financial records, medical documents, or admit cards). Built using Python, LangChain, and Gradio, running entirely on local consumer hardware without requiring an internet connection.

---

## 🚀 Core Features & Architecture
* **100% Data Privacy:** Zero data leaves your local machine. Completely immune to external data logging.
* **Local Semantic Search:** Implements local text chunking via `RecursiveCharacterTextSplitter` and converts them into mathematical vectors using HuggingFace's `all-MiniLM-L6-v2` model.
* **In-Memory Vector Store:** Leverages **ChromaDB** for lightning-fast local document vector indexing.
* **Optimized Local Execution:** Fine-tuned to run smoothly on standard consumer processors (tested on AMD Ryzen 5 series CPU) utilizing Meta's quantized `llama3.2:3b` model via Ollama.
* **Real-time Streaming Interface:** Features a responsive dual-panel web interface built with **Gradio** that streams the LLM's response token-by-token.

---

## 🛠️ System Architecture Diagram
The layout below illustrates how data streams locally through the application without touching the cloud:

1. **Document Ingestion:** PDF uploaded ➡️ Parsed via `PyPDFLoader` ➡️ Split into overlapping text chunks.
2. **Vectorization:** Text chunks converted to embeddings using `all-MiniLM-L6-v2` ➡️ Cached into `ChromaDB`.
3. **Retrieval & Inference:** User question queries ChromaDB ➡️ Top 3 relevant context blocks pulled ➡️ Context + Question sent to `llama3.2:3b` ➡️ Streamed response back to UI.

---

## ⚙️ Tech Stack
* **LLM Ingestion Engine:** Ollama (`llama3.2:3b`)
* **Embedding Model:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
* **Orchestration Framework:** LangChain (`langchain-ollama`, `langchain-community`)
* **Vector Database:** ChromaDB
* **UI Presentation:** Gradio

---

## 📋 Installation & Setup

### Prerequisites
1. Install [Ollama](https://ollama.com/).
2. Pull the optimized chat model in your terminal:
   ```bash
   ollama pull llama3.2:3b
