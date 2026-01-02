import streamlit as st
import os
from core.asr import transcribe_audio
from core.preprocess import clean_text
from rag.chunking import chunk_text
from rag.vector_store import add_transcript

def upload_section():
    audio = st.file_uploader(
        "Upload audio cuộc họp",
        type=["mp3", "wav"]
    )

    if audio is not None:
        # Lưu file tạm
        audio_path = os.path.join("temp", audio.name)
        os.makedirs("temp", exist_ok=True)

        with open(audio_path, "wb") as f:
            f.write(audio.read())

        with st.spinner("Đang chuyển giọng nói thành văn bản..."):
            transcript = transcribe_audio(audio_path)
            cleaned = clean_text(transcript)

            st.session_state["transcript"] = cleaned

            chunks = chunk_text(cleaned)
            add_transcript(chunks)

        st.success(f"Đã lưu {len(chunks)} đoạn vào Vector DB")

        st.subheader("Transcript")
        st.write(cleaned)
