import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import DATA_DIR


def load_documents():
    documents = []

    if not os.path.exists(DATA_DIR):
        print(f"Data folder not found: {DATA_DIR}")
        return documents

    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)

        # Load PDF files
        if filename.lower().endswith(".pdf"):
            # Skip empty PDF files
            if os.path.getsize(path) == 0:
                print(f"Skipped empty PDF: {filename}")
                continue

            try:
                loader = PyPDFLoader(path)
                docs = loader.load()
                documents.extend(docs)

                print(f"Loaded PDF: {filename}")

            except Exception as e:
                print(f"Error loading {filename}: {e}")

        # Load TXT files
        elif filename.lower().endswith(".txt"):
            try:
                loader = TextLoader(path, encoding="utf-8")
                docs = loader.load()
                documents.extend(docs)

                print(f"Loaded TXT: {filename}")

            except Exception as e:
                print(f"Error loading {filename}: {e}")

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)


if __name__ == "__main__":
    docs = load_documents()
    chunks = split_documents(docs)

    print(f"Documents loaded: {len(docs)}")
    print(f"Chunks created: {len(chunks)}")