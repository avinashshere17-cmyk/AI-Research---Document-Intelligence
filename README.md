#  AI Research & Document Intelligence

An AI-powered research assistant that lets users upload research papers in PDF format, ask questions about the documents, and receive concise answers with source-page references.

##  Project Overview

This project combines PDF processing, NLP, semantic embeddings, FAISS vector search, Retrieval-Augmented Generation (RAG), and Google Gemini to make research documents easier to understand.

# Workflow

```text
PDF Upload
   ↓
PDF Text Extraction
   ↓
Text Cleaning
   ↓
Text Chunking
   ↓
Sentence Transformer Embeddings
   ↓
FAISS Vector Search
   ↓
User Question
   ↓
Question Embedding
   ↓
Relevant Chunks
   ↓
Google Gemini
   ↓
Answer + Sources
```

##  Features

-  Upload multiple research PDFs
-  Text cleaning
-  Text chunking
-  Sentence Transformer embeddings
-  FAISS semantic similarity search
-  Google Gemini question answering
-  Source/page references
-  Chat history
-  Recommended questions
-  Document and chunk statistics
-  Downloadable research report
-  Reset uploaded documents
-  Streamlit web interface

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| FAISS | Vector similarity search |
| Google Gemini | Large Language Model |
| python-dotenv | Local environment variables |
| Git & GitHub | Version control |

##  Project Structure

```text
AI Research Assistent/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── AI Research Synopsis.pdf
│   └── AI Research Document Intelligence Complete Project Guide.pdf
│
├── data/
│   └── papers/
│       └── research.pdf
│
└── src/
    ├── pdf_processor.py
    ├── text_cleaner.py
    ├── chunker.py
    ├── embedder.py
    ├── vector_store.py
    ├── retriever.py
    └── llm.py
```

> Research PDFs uploaded by users are excluded from GitHub through `.gitignore`.

##  Main Components

### PDF Processor
Extracts text from PDF files page by page using PyMuPDF.

### Text Cleaner
Cleans extracted text before processing.

### Chunker
Splits long document text into smaller searchable chunks.

### Embedder
Uses Sentence Transformers to convert text into numerical vectors.

### FAISS Vector Store
Stores embeddings and performs similarity search.

### Retriever
Finds document chunks relevant to the user's question.

### Gemini LLM
Uses the retrieved document context to generate an answer.

### Streamlit App
Provides the interface for PDF upload, processing, questions, answers, sources, chat history, and report download.

##  Example

User uploads:

```text
research.pdf
```

User asks:

```text
What is the main objective of this research paper?
```

The system retrieves the most relevant document chunks and sends them to Gemini to generate an answer with source information.

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/avinashshere17-cmyk/AI-Research---Document-Intelligence.git
cd AI-Research---Document-Intelligence
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

##  Gemini API Key

Create a `.env` file in the project root for local development:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Never publish your real API key.

The `.gitignore` file excludes `.env`.

### Streamlit Cloud

Add the key in the app's **Secrets** settings:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

##  Run Locally

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

##  Deployment

The project can be deployed with Streamlit Community Cloud.

Configuration:

```text
Repository:
avinashshere17-cmyk/AI-Research---Document-Intelligence

Branch:
main

Main file:
app.py
```

After deployment, add `GEMINI_API_KEY` to Streamlit Secrets.

##  Testing

The RAG pipeline was tested through:

```text
PDF Extraction
      ↓
Text Cleaning
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS Index
      ↓
Similarity Retrieval
      ↓
Gemini
      ↓
Answer + Sources
```

The backend successfully generated chunks, embeddings, a FAISS index, and answers with source-page information.

##  Objectives

- Build an AI-powered research document assistant
- Reduce time spent understanding research papers
- Enable natural-language document questioning
- Use semantic search for relevant information
- Generate answers from retrieved document context
- Provide source information for transparency

##  Advantages

- Saves time when reading long documents
- Simple user interface
- Supports multiple PDFs
- Uses semantic search
- Provides source-page information
- Useful for students and researchers

##  Limitations

- Answer quality depends on the uploaded document and retrieved context
- Scanned/image-only PDFs may need OCR
- Gemini API limits can affect usage
- Very large documents may require optimized retrieval
- Internet access is required for Gemini API calls

##  Future Scope

- Hybrid keyword + semantic search
- Reranking retrieved chunks
- Citation verification
- Research gap analysis
- Automatic paper summarization
- Literature review generation
- Research report generation
- OCR for scanned PDFs
- Persistent vector database
- User authentication
- Cloud storage integration

##  Documentation

Detailed documentation is available in the `docs/` folder:

- **AI Research Synopsis** — project overview, objectives, methodology, workflow, technology stack, advantages, limitations, and future scope.
- **Complete Project Guide** — detailed file-by-file explanation, setup, implementation, workflow, and deployment.

##  Author/ created by :-

Avinash shere  
BSc Data Science

This project was developed as an academic and portfolio project in AI and Data Science.

##  Repository

https://github.com/avinashshere17-cmyk/AI-Research---Document-Intelligence

# Live Demo

Try the application online:

[AI Research & Document Intelligence]
(https:ai-research---document-intelligence-3atwisujfpiw6edpqz7z6c.streamlit.app/)

 Upload your research PDF, ask questions, and get AI-generated answers with source pages.
## License

This project is intended for educational, academic, and portfolio purposes.