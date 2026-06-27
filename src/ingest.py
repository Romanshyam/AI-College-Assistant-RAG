"""
ingest.py

This module is responsible for:

1. Reading PDF files
2. Extracting text
3. Splitting text into chunks

This is the first step of the RAG pipeline.
"""

from pathlib import Path

from src.chunking import split_documents

from pypdf import PdfReader

DATA_FOLDER = "data"

def load_pdfs(data_folder= DATA_FOLDER):
    """
    Reads all PDF files inside the data folder.

    Parameters:
        data_folder (str): Path to folder containing PDFs

    Returns:
        list: List of extracted text from each PDF
    """

    documents = []

    pdf_files = Path(data_folder).glob("*.pdf")

    for pdf_file in pdf_files:

        print(f"Reading: {pdf_file.name}")

        reader = PdfReader(pdf_file)

        text = ""

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                documents.append(
                    {
                        "text": page_text,
                        "source": pdf_file.name,
                        "page": page_number
                        }
             )

    return documents

def load_and_split_documents():
    """
    Complete ingestion pipeline.
    """

    documents = load_pdfs()

    chunks = split_documents(documents)

    return chunks




