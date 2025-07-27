# app/routes/router.py
def show_page():
    import streamlit as st
    from app.components.memory_view import display_memories
    from app.components.upload_memory import upload_memory

    menu = ["Home", "Upload Memory"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        display_memories()
    elif choice == "Upload Memory":
        upload_memory()
