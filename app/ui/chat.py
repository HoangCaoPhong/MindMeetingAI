import streamlit as st
from rag.qa import answer_question

def chat_section():
    if "transcript" not in st.session_state:
        st.info("Vui lòng upload cuộc họp trước.")
        return

    q = st.text_input("Hỏi về cuộc họp:")
    if q:
        ans = answer_question(q)
        st.write(ans)
