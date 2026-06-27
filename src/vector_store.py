import chromadb


def create_vector_store():
    """
    Create or connect to the ChromaDB database.
    """

    client = chromadb.PersistentClient(
        path="vector_db"
    )

    return client


def get_collection(client):
    """
    Create or get the collection.
    """

    collection = client.get_or_create_collection(
        name="college_documents"
    )

    return collection


def add_documents(collection, chunks, embeddings):
    """
    Store chunks, embeddings and metadata.
    """

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        {
            "source": chunk["source"],
            "page":chunk["page"]
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks successfully!")