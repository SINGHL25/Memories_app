# File: backend/services/db_service.py
# ------------------------------------
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["memories"]

def save_memory(photo_url, description, tags):
    db.memories.insert_one({"photo": photo_url, "desc": description, "tags": tags})

def search_memories(keyword):
    return list(db.memories.find({"$text": {"$search": keyword}}))
