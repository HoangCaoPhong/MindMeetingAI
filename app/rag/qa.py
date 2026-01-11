import ollama
from rag.vector_store import search


SYSTEM_PROMPT = """
Bạn là trợ lý AI chuyên trả lời câu hỏi dựa trên nội dung cuộc họp.

Quy tắc:
- Chỉ sử dụng thông tin trong transcript được cung cấp
- Không suy đoán
- Trả lời bằng tiếng Việt
- Nếu không có thông tin, trả lời: "Không tìm thấy thông tin trong cuộc họp"
"""


def answer_question(question: str) -> str:
    # ===== STEP 1: Retrieve =====
    docs = search(question, k=3)

    if not docs:
        return "❌ Không tìm thấy thông tin trong cuộc họp."

    context = "\n\n".join(docs)

    # ===== STEP 2: Prompt =====
    prompt = f"""
Transcript cuộc họp:
-------------------
{context}

Câu hỏi:
{question}

Trả lời ngắn gọn, đúng trọng tâm.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()
