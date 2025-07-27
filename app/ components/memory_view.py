# app/components/memory_view.py
def display_memories():
    import streamlit as st
    from app.services.firebase_service import fetch_memories

    st.title("📸 Your Memories")
    memories = fetch_memories()
    for memory in memories:
        st.image(memory['image_url'], caption=memory['caption'], width=400)

