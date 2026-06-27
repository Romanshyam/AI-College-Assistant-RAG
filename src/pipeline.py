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


def rebuild_vector_database():
    """
    Rebuild the vector database using all PDFs in the data folder.
    """

    # Load documents
    documents = load_pdfs("data")

    # Split
    chunks = split_documents(documents)

    # Embeddings
    model = create_embedding_model()

    embeddings = create_embeddings(
        model,
        chunks
    )

    # ChromaDB
    client = create_vector_store()

    # Delete previous collection
    try:
        client.delete_collection(
            "college_documents"
        )
    except:
        pass

    collection = get_collection(client)

    add_documents(
        collection,
        chunks,
        embeddings
    )

    return len(documents), len(chunks)