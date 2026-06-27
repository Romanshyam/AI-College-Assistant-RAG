from src.ingest import load_pdfs, split_documents

from src.embeddings import (
    create_embedding_model,
    create_embeddings
)

from src.vector_store import (
    create_vector_store,
    get_collection,
    add_documents
)

# -------------------------------------
# Step 1: Load PDFs
# -------------------------------------
print("=" * 50)
print("Loading PDFs...")
print("=" * 50)

documents = load_pdfs("data")

print(f"Total Documents : {len(documents)}")

# -------------------------------------
# Step 2: Split into chunks
# -------------------------------------
chunks = split_documents(documents)

print(f"Total Chunks    : {len(chunks)}")

# -------------------------------------
# Step 3: Create Embeddings
# -------------------------------------
print("=" * 50)
print("Creating Embeddings...")
print("=" * 50)

model = create_embedding_model()

embeddings = create_embeddings(model, chunks)

# -------------------------------------
# Step 4: Connect to ChromaDB
# -------------------------------------
client = create_vector_store()

# Delete old collection (if exists)
try:
    client.delete_collection("college_documents")
    print("Old collection deleted.")
except Exception:
    print("No existing collection found.")

# -------------------------------------
# Step 5: Create Collection
# -------------------------------------
collection = get_collection(client)

# -------------------------------------
# Step 6: Store Chunks
# -------------------------------------
add_documents(
    collection,
    chunks,
    embeddings
)

print("=" * 50)
print("Vector Database Created Successfully!")
print(f"Total Chunks in Database : {collection.count()}")
print("=" * 50)