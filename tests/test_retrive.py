from src.retriever import retrieve_documents

query = "What is an intelligent agent?"

docs = retrieve_documents(query)

print("=" * 50)

for i, doc in enumerate(docs):
    print(f"\nDocument {i+1}")
    print("-" * 40)
    print(doc[:500])