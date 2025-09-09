from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document

def load_file():
    loader = PyPDFLoader(r"C:\Users\Rajmohan\Desktop\POC-PDF-Summarizer\data\stats.pdf")
    data = loader.load()

            
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap  = 100,
    )

    # Prepare documents and embeddings
    all_chunks = []
    for page in data:
        chunks = text_splitter.split_text(page.page_content)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "page": page.metadata.get("page", 0),
                "chunk_index": i
            })

    # Convert your chunks into Document objects
    docs_for_qdrant = [
    Document(
        page_content=chunk["text"],
        metadata={
            "page": chunk["page"],
            "chunk_index": chunk["chunk_index"]
            }
         )
    for chunk in all_chunks
    ]
    return docs_for_qdrant

#docs_for_qdrant = load_file()
#print(docs_for_qdrant)