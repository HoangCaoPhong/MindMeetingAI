def clean_text(text: str) -> str:
    text = text.replace("ờ", "").replace("à", "")
    return text.strip()




