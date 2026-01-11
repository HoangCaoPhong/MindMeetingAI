import streamlit as st
from core.asr import transcribe_audio
from core.preprocess import clean_text
from core.transcript_refiner import refine_transcript


def upload_section():
    uploaded_file = st.file_uploader(
        "Upload audio cuộc họp",
        type=["mp3", "wav"]
    )

    if uploaded_file:
        audio_path = f"temp/{uploaded_file.name}"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())

        # ===== STEP 1: Whisper STT =====
        if "raw_transcript" not in st.session_state:
            with st.spinner("🎙️ Đang chuyển giọng nói thành văn bản..."):
                st.session_state.raw_transcript = transcribe_audio(audio_path)

        # ===== STEP 2: AI clean =====
        if "clean_transcript" not in st.session_state:
            with st.spinner("🧹 Thuật toán đang làm sạch transcript..."):
                cleaned = clean_text(st.session_state.raw_transcript)
                st.session_state.clean_transcript = refine_transcript(cleaned)

        # ===== STEP 3: Editable transcript =====
        if "editable_transcript" not in st.session_state:
            st.session_state.editable_transcript = st.session_state.clean_transcript

        # ===== UI =====
        st.subheader("📝 Transcript (có thể chỉnh sửa)")
        st.caption("AI đã làm sạch. Bạn có thể chỉnh sửa lại nội dung nếu muốn.")

        edited_text = st.text_area(
            "Nội dung transcript:",
            value=st.session_state.editable_transcript,
            height=260
        )

        # luôn sync transcript sau khi sửa
        st.session_state.editable_transcript = edited_text
