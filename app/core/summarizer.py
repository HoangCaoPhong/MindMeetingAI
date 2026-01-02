import ollama

SUMMARY_PROMPT = """
Bạn là trợ lý AI chuyên phân tích cuộc họp.

Hãy tóm tắt cuộc họp theo cấu trúc sau (ghi rõ tiêu đề từng mục):

1. Executive Summary (2–3 câu)
2. Key Insights (bullet points)
3. Decisions Made
4. Risks / Issues
5. Action Items (Ai – Làm gì – Khi nào)

Nội dung cuộc họp:
----------------
{transcript}
"""

def multi_layer_summary(transcript: str) -> str:
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": SUMMARY_PROMPT.format(transcript=transcript)
            }
        ]
    )
    return response["message"]["content"]
