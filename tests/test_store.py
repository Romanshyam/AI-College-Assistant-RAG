from src.ingest import load_pdfs
from src.chunking import split_documents
from src.embeddings import (
    create_embedding_model,
    create_embeddings
)
from src.vector_store import (
    create_vector_store,
    get_collection,
    add_documents
)

# Read PDFs
documents = load_pdfs("data")

# Split into chunks
chunks = split_documents(documents)

# Embedding model
model = create_embedding_model()

# Generate embeddings
embeddings = create_embeddings(model, chunks)

# Create ChromaDB
client = create_vector_store()

collection = get_collection(client)

# Store everything
add_documents(
    collection,
    chunks,
    embeddings
)