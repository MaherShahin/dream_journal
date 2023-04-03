# backend/app/models/entry.py
from bson.objectid import ObjectId

class DreamEntry:
    def __init__(self, data):
        self.id = str(data["_id"]) if "_id" in data else None
        self.user_id = data["user_id"]
        self.title = data["title"]
        self.content = data["content"]
        self.date = data.get("date")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
