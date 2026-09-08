import os

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from document_loader import load_documents, split_documents
from config import CHROMA_DIR, COLLECTION_NAME


def create_vector_database():
    documents = load_documents()

    if not documents:
        print("No documents found in data folder.")
        return None

    chunks = split_documents(documents)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME
    )

    print("Vector database created successfully.")
    print(f"Total chunks: {len(chunks)}")

    return vectorstore


def get_vector_database():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )


def search_documents(question, k=4):
    vectorstore = get_vector_database()
    return vectorstore.similarity_search(question, k=k)


if __name__ == "__main__":
    create_vector_database()