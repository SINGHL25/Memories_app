# app/components/upload_memory.py
def upload_memory():
    import streamlit as st
    from app.services.firebase_service import upload_memory_to_firebase

    st.title("📤 Upload a New Memory")
    image = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
    caption = st.text_input("Enter a caption")

    if st.button("Upload"):
        if image and caption:
            upload_memory_to_firebase(image, caption)
            st.success("Memory uploaded!")
        else:
            st.warning("Please provide both image and caption.")

