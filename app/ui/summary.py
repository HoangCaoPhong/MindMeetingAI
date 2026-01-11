import streamlit as st
from core.summarizer import multi_layer_summary

from rag.chunking import chunk_text
from rag.vector_store import add_transcript


def summary_section():
    if "editable_transcript" not in st.session_state:
        st.info("Vui lòng upload audio trước.")
        return

    if st.button("🧠 Generate Meeting Summary"):
        with st.spinner("AI đang phân tích cuộc họp..."):

            transcript = st.session_state.editable_transcript

            # ✅ 1. UPDATE QA BOT (RAG)
            chunks = chunk_text(transcript)
            add_transcript(chunks)

            # ✅ 2. GENERATE SUMMARY
            summary = multi_layer_summary(transcript)
            st.session_state.summary = summary

        st.success("✅ Summary tạo xong & QA Bot đã được cập nhật")

    if "summary" in st.session_state:
        st.markdown("## 📄 Meeting Summary")
        st.markdown(st.session_state.summary)
