# PDF Summarizer with RAG Pipeline

A Python-based **Retrieval-Augmented Generation (RAG) pipeline** for summarizing PDFs using OpenAI embeddings and LLMs, with Qdrant as the vector store. This project allows you to query PDFs and get concise, structured answers based on retrieved content.

test
---

## Features

- Load PDF documents and split them into chunks for vectorization.
- Embed text chunks using **OpenAI embeddings** (`text-embedding-3-small`).
- Store and index vectors in **Qdrant** for fast semantic retrieval.
- Retrieve relevant chunks from Qdrant and generate answers using **OpenAI LLMs** (`gpt-3.5-turbo` or `gpt-4`).
- Fully **RAG-based pipeline** with source tracing.

---

## Directory Structure

```bash
PDF-Summarizer/
│
├─ data/ # Place PDF files here
│ └─ Stats.pdf
├─ main.py # Main RAG pipeline script
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation
```

---

## Environment Setup

1. **Clone the repository**

```bash
git clone https://github.com/Tejaswi-Boni/POCPDFSummarizer.git
```

2.  **Create a Python virtual environment**

# Using conda

```bash
conda create -n PDFSummarizer python=3.10 -y
conda activate PDFSummarizer
```

3.  **Install dependencies**

```bash
pip install -r requirements.txt
```

## RAG Pipeline Overview

The PDF Summarizer uses a **Retrieval-Augmented Generation (RAG) pipeline**. The process is as follows:

1. **Load PDF**  
   Read PDF pages using `PyPDFLoader`.

2. **Split into Chunks**  
   Use `RecursiveCharacterTextSplitter` to break text into manageable pieces.

3. **Embeddings**  
   Convert text chunks into vectors using `OpenAIEmbeddings`.

4. **Vector Store**  
   Store the vectors in **Qdrant** for semantic search and retrieval.

5. **Retrieval + Generation**  
   Retrieve the top-k relevant chunks and generate answers using `ChatOpenAI`.

6. **Answer + Sources**  
   Return a structured answer along with page and chunk references for traceability.
