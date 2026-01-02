import ollama

res = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Tóm tắt 1 câu về một cuộc họp dự án bị trễ deadline."}
    ]
)

print(res["message"]["content"])
