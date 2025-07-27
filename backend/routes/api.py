# File: backend/routes/api.py
# ----------------------------
from flask import Flask, request, jsonify
from services.db_service import save_memory
from services.stt_service import transcribe_audio

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    text = transcribe_audio(file)
    save_memory(photo_url="url_from_storage", description=text, tags=["ai", "voice"])
    return jsonify({"status": "saved", "description": text})
