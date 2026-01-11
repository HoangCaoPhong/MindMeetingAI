import streamlit as st
from rag.qa import answer_question


def chat_section():
    st.subheader("💬 Meeting QA Bot")
    st.caption("Đặt câu hỏi dựa trên nội dung cuộc họp đã xử lý")

    # ===== Guard =====
    if "editable_transcript" not in st.session_state:
        st.info("📌 Vui lòng upload và xử lý cuộc họp trước.")
        return

    # ===== Init chat history =====
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ===== Input =====
    user_question = st.text_input(
        "Nhập câu hỏi về cuộc họp:",
        placeholder="Ví dụ: Deadline của dự án là khi nào?"
    )

    if user_question:
        with st.spinner("🤖 AI đang suy nghĩ..."):
            answer = answer_question(user_question)

        st.session_state.chat_history.append(
            ("🧑‍💼 Bạn", user_question)
        )
        st.session_state.chat_history.append(
            ("🤖 AI", answer)
        )

    st.divider()

    # ===== Render chat =====
    for role, msg in st.session_state.chat_history:
        st.markdown(f"**{role}:** {msg}")
