import gradio as gr
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# 1. Initialize local LLM (Ollama) and local Embeddings (HuggingFace)
llm = OllamaLLM(model="llama3.2:3b")

# This runs 100% locally on your Python environment, bypassing Ollama for embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Global reference to hold our active database index
vector_store = None

def process_pdf(file_path):
    global vector_store
    if file_path is None:
        return "⚠️ Please select a valid PDF file first."
    
    try:
        # Load and parse text layout from the document
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        # Breakdown raw text into overlapping semantic blocks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=60)
        chunks = text_splitter.split_documents(documents)
        
        # Generate mathematical vector embeddings locally and save to Chroma
        vector_store = Chroma.from_documents(chunks, embeddings)
        return f"✅ Database built successfully! Processed {len(chunks)} structural document chunks."
    except Exception as e:
        return f"❌ Critical error parsing document: {str(e)}"

def predict(message, history):
    global vector_store
    
    if vector_store is not None:
        # Search for top 3 matching information blocks
        docs = vector_store.similarity_search(message, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        prompt = f"""You are an advanced offline document analysis assistant. Answer the user prompt using only the verified facts provided in the context below. If the answer cannot be found in the context, explicitly state that you don't know based on the provided material. Do not extrapolate.

Context:
{context}

Question: {message}
Answer:"""
    else:
        prompt = message

    # Stream out chunks to the Gradio web component
    response = ""
    for chunk in llm.stream(prompt):
        response += chunk
        yield response

# 2. Design the Custom Blocks-based Web Interface Layout
with gr.Blocks(title="Local Document RAG Engine") as demo:
    gr.Markdown("# 📁 Local Document Intelligent RAG Engine")
    gr.Markdown("Analyze secure documents completely offline. Zero internet connections required, 100% data privacy.")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🛠️ Data Loading Control")
            file_input = gr.File(label="Target PDF Document", file_types=[".pdf"])
            upload_button = gr.Button("Build Local Index Vector Store", variant="primary")
            status_output = gr.Textbox(label="System Status Logs", value="System idling. Awaiting document vector ingestion...", interactive=False)
            
        with gr.Column(scale=2):
            gr.Markdown("### 💬 Semantic Chat Assistant")
            chat_interface = gr.ChatInterface(fn=predict)
            
    upload_button.click(fn=process_pdf, inputs=file_input, outputs=status_output)

if __name__ == "__main__":
    demo.launch()