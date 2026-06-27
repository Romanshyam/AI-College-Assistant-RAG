from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    """
    Split extracted text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []
    for document in documents:
        document_chunks = splitter.split_text(
            document["text"]
        )
        for chunk in document_chunks:
            chunks.append(
                {
                    "text": chunk,
                    "source": document["source"],
                    "page": document["page"]
                })
    return chunks

