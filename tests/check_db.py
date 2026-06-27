from src.vector_store import create_vector_store, get_collection

client = create_vector_store()

collection = get_collection(client)

print("=" * 40)
print("Total Chunks:", collection.count())
print("=" * 40)