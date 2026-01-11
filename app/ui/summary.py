import streamlit as st
from core.summarizer import multi_layer_summary

def summary_section():
    if "transcript" not in st.session_state:
        st.info("Chưa có transcript.")
        return

    if st.button("Generate Meeting Summary"):
    
        with st.spinner("AI đang phân tích cuộc họp..."):
            summary = multi_layer_summary(st.session_state["transcript"])
            st.session_state["summary"] = summary

    if "summary" in st.session_state:
        st.markdown("### 📄 Meeting Summary")
        st.markdown(st.session_state["summary"])
