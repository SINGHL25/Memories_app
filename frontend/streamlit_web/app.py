# File: frontend/streamlit_app.py
# --------------------------------
import streamlit as st
from backend.services.stt_service import transcribe_audio
from backend.services.db_service import save_memory

st.title("🧠 Memory Collector")

file = st.file_uploader("Upload Audio Note", type=["mp3", "wav"])
if file:
    with open("temp.mp3", "wb") as f:
        f.write(file.read())
    text = transcribe_audio("temp.mp3")
    st.success(f"Transcribed: {text}")
    if st.button("Save to DB"):
        save_memory("dummy_url.jpg", text, ["ai", "memory"])
        st.success("Saved!")
