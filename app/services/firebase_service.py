# app/services/firebase_service.py
import firebase_admin
from firebase_admin import credentials, storage, firestore
import uuid

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("backend/firebase_config.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'your-bucket.appspot.com'
        })

def upload_memory_to_firebase(image_file, caption):
    db = firestore.client()
    bucket = storage.bucket()
    blob = bucket.blob(f"memories/{uuid.uuid4()}.jpg")
    blob.upload_from_file(image_file, content_type='image/jpeg')
    blob.make_public()

    db.collection("memories").add({
        "image_url": blob.public_url,
        "caption": caption
    })

def fetch_memories():
    db = firestore.client()
    docs = db.collection("memories").stream()
    return [{"image_url": doc.to_dict()["image_url"], "caption": doc.to_dict()["caption"]} for doc in docs]
