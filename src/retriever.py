from src.vector_store import (
    create_vector_store,
    get_collection
)

from src.embeddings import create_embedding_model


def retrieve_documents(query, top_k=8):
    """
    Retrieve the most relevant document chunks.
    """

    # Load embedding model
    model = create_embedding_model()

    # Convert query into embedding
    query_embedding = model.encode(query).tolist()

    # Connect to ChromaDB
    client = create_vector_store()

    collection = get_collection(client)

    # Search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "documents": results["documents"][0],
        "sources": results["metadatas"][0]
    }