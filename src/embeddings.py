from sentence_transformers import SentenceTransformer


def create_embedding_model():
    """
    Load the Hugging Face embedding model.
    """

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    return model


def create_embeddings(model, chunks):
    """
    Convert document chunks into embeddings.
    """

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings