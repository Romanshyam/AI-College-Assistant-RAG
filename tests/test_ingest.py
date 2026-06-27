from src.ingest import load_pdfs, split_documents

documents = load_pdfs("data")

chunks = split_documents(documents)

print("=" * 30)
print(f"Total Documents : {len(documents)}")
print(f"Total Chunks    : {len(chunks)}")
print("=" * 30)

print("\nFirst Chunk:\n")
print(chunks[0])