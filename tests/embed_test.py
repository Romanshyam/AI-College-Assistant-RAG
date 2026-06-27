from src.ingest import (
    load_pdfs,
    split_documents,
    create_embedding_model,
    create_embeddings
)

# Load PDFs
documents = load_pdfs("data")

# Split into chunks
chunks = split_documents(documents)

# Load embedding model
model = create_embedding_model()

# Generate embeddings
embeddings = create_embeddings(model, chunks)

print("=" * 50)
print("Total Chunks:", len(chunks))
print("Total Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))
print("=" * 50)
print("\nFirst Chunk:\n")
print(chunks[0])

print("\nFirst Embedding (First 10 Values):\n")
print(embeddings[0][:10])