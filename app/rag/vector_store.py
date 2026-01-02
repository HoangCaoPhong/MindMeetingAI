import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# Khởi tạo Chroma Client (local, persist)
client = chromadb.Client(
    Settings(
        persist_directory=".chroma",
        anonymized_telemetry=False
    )
)

# Collection cho meeting
collection = client.get_or_create_collection(
    name="meetings"
)

# Embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def add_transcript(chunks: list[str]):
    if not chunks:
        return

    embeddings = embedder.encode(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )


def search(query: str, k: int = 3):
    query_embedding = embedder.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    # Trả về list các đoạn liên quan nhất
    return results["documents"][0]
