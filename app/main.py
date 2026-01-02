import streamlit as st
from ui.upload import upload_section
from ui.summary import summary_section
from ui.chat import chat_section

st.set_page_config(page_title="MindMeetingAI", layout="wide")
st.title("MindMeetingAI – Free & Local AI Meeting Assistant")

tab1, tab2 = st.tabs(["📄 Meeting Summary", "💬 Meeting QA Bot"])

with tab1:
    upload_section()
    summary_section()

with tab2:
    chat_section()


