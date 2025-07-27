# app/main.py
import streamlit as st
from app.routes.router import show_page
from app.services.firebase_service import init_firebase

st.set_page_config(page_title="Memories Collector", layout="wide")
init_firebase()
show_page()
