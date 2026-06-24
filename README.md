# 📁 SecureSphere AI: Privacy-First Intelligent Chatbot & Document Retriever

SecureSphere AI is an advanced, privacy-focused conversational chatbot and semantic search retriever that transforms your sensitive local PDF files (financial records, legal papers, or personal data) into an interactive, local knowledge base. Built using Python, LangChain, and Gradio, this system is engineered to run completely offline on standard consumer hardware—giving you absolute data sovereignty with zero data leaving your machine.

> 🚀 **Deployment Note:** The live demo link provided in the "About" website section runs on a secure cloud server for instant demonstration purposes. To experience the 100% offline version with absolute data privacy, you can easily follow the installation steps below to deploy the exact same local conversational engine directly onto your own machine.

---

## 🚀 Core Capabilities & Architecture
* **Intelligent Chatbot & Retriever:** Functions as both a smart search engine (locating precise information within hundreds of pages) and a conversational AI assistant that summarizes, explains, and cross-references your documents.
* **100% Data Privacy:** Zero data leaves your local machine. Completely immune to external data logging, corporate AI training usage, or cloud leaks.
* **Local Semantic Search:** Implements local text chunking via `RecursiveCharacterTextSplitter` and converts them into mathematical vectors using HuggingFace's `all-MiniLM-L6-v2` model.
* **In-Memory Vector Store:** Leverages **ChromaDB** for lightning-fast document vector indexing and contextual keyword extraction.
* **Optimized Local Execution:** Fine-tuned to run smoothly on standard consumer processors (tested on AMD Ryzen 5 series CPU) utilizing Meta's quantized `llama3.2:3b` model via Ollama.
* **Real-time Streaming Interface:** Features a responsive dual-panel web interface built with **Gradio** that streams the AI's response token-by-token.

---

## 🛠️ System Architecture Diagram
The layout below illustrates how data streams locally through the application without touching the cloud:



1. **Knowledge Ingestion:** PDF uploaded ➡️ Parsed via `PyPDFLoader` ➡️ Split into overlapping text chunks.
2. **Vectorization & Indexing:** Text chunks converted to deep-learning embeddings using `all-MiniLM-L6-v2` ➡️ Cached securely into `ChromaDB`.
3. **Retrieval-Augmented Chat:** User types a question ➡️ ChromaDB retrieves the top 3 most relevant context blocks ➡️ Context + Question are fused into a prompt ➡️ Local LLM processes it and streams contextual answers back to the UI.

---

## ⚙️ Tech Stack
* **LLM Engine:** Ollama (`llama3.2:3b`) / Groq Cloud Client (Used for the live cloud demo)
* **Embedding Model:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
* **Orchestration Framework:** LangChain (`langchain-huggingface`, `langchain-community`)
* **Vector Database:** ChromaDB
* **UI Presentation:** Gradio

---

## 📋 Installation & Setup (Local Offline Mode)

### Prerequisites
1. Download and install [Ollama](https://ollama.com/).
2. Pull the optimized chat model in your terminal:
   ```bash
   ollama pull llama3.2:3b
