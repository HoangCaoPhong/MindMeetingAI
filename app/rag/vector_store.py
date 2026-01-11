import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

client = chromadb.Client(
    Settings(
        persist_directory=".chroma",
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(name="meetings")
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def clear_collection():
    """Xóa toàn bộ dữ liệu trong collection (safe)"""
    all_ids = collection.get()["ids"]
    if all_ids:
        collection.delete(ids=all_ids)


def add_transcript(chunks: list[str]):
    if not chunks:
        return

    # ✅ RESET DB ĐÚNG CÁCH
    clear_collection()

    embeddings = embedder.encode(chunks).tolist()
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def search(query: str, k: int = 3):
    query_embedding = embedder.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    return results["documents"][0] if results["documents"] else []
