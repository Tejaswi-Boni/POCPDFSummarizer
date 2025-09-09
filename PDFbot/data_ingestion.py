from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from PDFbot.helper import load_file
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",api_key=OPENAI_API_KEY)

def init_qdrant(embeddings, dim=1536):
    qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

       # Check if collection already exists
    existing_collections = [c.name for c in qdrant_client.get_collections().collections]
    if COLLECTION_NAME not in existing_collections:
        logging.info(f"Collection '{COLLECTION_NAME}' does not exist. Creating...")
        qdrant_client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
        )
    else:
        logging.info(f"Collection '{COLLECTION_NAME}' already exists. Skipping creation.")

    qdrant_store = Qdrant(
        client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embeddings=embeddings,
    )

    return qdrant_store

def ingestdata(status=None):
    qdrant_store = init_qdrant(embeddings)

    # Check if collection already has data
    qdrant_client = qdrant_store.client
    point_count = qdrant_client.count(collection_name=COLLECTION_NAME).count

    if point_count == 0:
        logging.info("Collection is empty. Inserting documents...")
        docs_for_qdrant = load_file()
        qdrant_store.add_documents(docs_for_qdrant)
        logging.info(f"Inserted {len(docs_for_qdrant)} documents into the collection.")
    else:
        logging.info(f"Collection already has {point_count} points. Skipping ingestion.")
    
    return qdrant_store


# if __name__ == "__main__":
#     # Ingest data (if collection is empty)
#     vstore = ingestdata()
#     # Perform a sample similarity search
#     query = "What is correlation in statistics?"
#     results = vstore.similarity_search(query)

#     print(f"\nTop results for query: '{query}'\n")
#     for res in results:
#         print(f"* {res.page_content[:200]}... [{res.metadata}]")