import ollama
from rag.vector_store import search

def answer_question(question: str) -> str:
    docs = search(question)

    if not docs["documents"]:
        return "Không tìm thấy thông tin liên quan."

    context = docs["documents"][0][0]

    prompt = f"""
    Dựa trên nội dung cuộc họp sau:
    ----------------
    {context}

    Trả lời câu hỏi:
    {question}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
