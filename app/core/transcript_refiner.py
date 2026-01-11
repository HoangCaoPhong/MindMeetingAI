from ollama import chat

SYSTEM_PROMPT = """
You are an assistant that cleans and refines Vietnamese meeting transcripts.

Tasks:
- Fix spelling and punctuation
- Restore proper sentence boundaries
- Keep original meaning
- DO NOT summarize
- DO NOT add new information
- Output clean Vietnamese text only
"""

def refine_transcript(raw_text: str) -> str:
    response = chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": raw_text}
        ]
    )
    return response.message.content.strip()
