# app/main.py
import streamlit as st
from app.voice_to_text import transcribe_audio
from app.memory_search import search_memories
from app.firebase_service import fetch_memories

st.set_page_config(page_title="My Memories", layout="wide")

st.title("📸 My Memory Wall")

menu = st.sidebar.radio("Navigate", ["View Memories", "Add by Voice", "Search Memory"])

if menu == "View Memories":
    memories = fetch_memories()
    for memory in memories:
        st.image(memory["image_url"], width=300)
        st.write(f"📝 {memory['description']}")
        st.caption(f"📆 {memory['timestamp']}")

elif menu == "Add by Voice":
    audio_file = st.file_uploader("Upload your voice memory", type=["mp3", "wav"])
    if audio_file:
        text = transcribe_audio(audio_file)
        st.success(f"Transcribed Memory: {text}")

elif menu == "Search Memory":
    query = st.text_input("Search memories (keyword)")
    if query:
        result = search_memories(query)
        for res in result:
            st.image(res["image_url"], width=300)
            st.write(res["description"])
