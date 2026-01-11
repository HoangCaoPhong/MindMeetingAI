import streamlit as st
from core.asr import transcribe_audio
from core.preprocess import clean_text
from core.transcript_refiner import refine_transcript


def upload_section():
    uploaded_file = st.file_uploader(
        "🎧 Upload audio cuộc họp",
        type=["mp3", "wav"]
    )

    if not uploaded_file:
        return

    audio_path = f"temp/{uploaded_file.name}"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    # ===============================
    # STEP 1: WHISPER STT
    # ===============================
    with st.spinner("🔊 Đang chuyển giọng nói thành văn bản..."):
        raw_text = transcribe_audio(audio_path)

    # ===============================
    # STEP 2: CLEAN + AI REFINE (TỰ ĐỘNG)
    # ===============================
    with st.spinner("Thuật toán đang làm sạch transcript..."):
        cleaned_text = clean_text(raw_text)
        refined_text = refine_transcript(cleaned_text)

    # ===============================
    # STEP 3: INIT EDITABLE STATE (TRƯỚC KHI RENDER)
    # ===============================
    if (
        "editable_transcript" not in st.session_state
        or st.session_state.get("last_refined_text") != refined_text
    ):
        st.session_state["editable_transcript"] = refined_text
        st.session_state["last_refined_text"] = refined_text

    # ===============================
    # STEP 4: EDITABLE TRANSCRIPT UI
    # ===============================
    st.subheader("📝 Transcript (có thể chỉnh sửa)")
    st.caption("AI đã tự động làm sạch. Bạn có thể chỉnh sửa lại nếu muốn.")

    st.text_area(
        "Nội dung transcript:",
        key="editable_transcript",
        height=300
    )

    # ===============================
    # STEP 5: LƯU TRANSCRIPT CHO SUMMARY
    # ===============================
    st.session_state["transcript"] = st.session_state["editable_transcript"]
