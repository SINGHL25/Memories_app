import whisper
from tempfile import NamedTemporaryFile

model = whisper.load_model("base")

def transcribe_audio(uploaded_file):
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        result = model.transcribe(tmp.name)
        return result["text"]

