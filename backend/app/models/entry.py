# backend/app/models/entry.py
from bson.objectid import ObjectId
from backend.app.utils.database import mongo

class DreamEntry:
    def __init__(self, data):
        self.id = str(data["_id"]) if "_id" in data else None
        self.user_id = data["user_id"]
        self.title = data["title"]
        self.content = data["content"]
        self.date = data.get("date")

    @classmethod
    def get_entries_by_user_id(cls, user_id):
        entries = mongo.db.entries.find({"user_id": user_id})
        return [cls(entry) for entry in entries]

    @classmethod
    def get_entry_by_id(cls, entry_id):
        entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
        return cls(entry) if entry else None

    @classmethod
    def create_entry(cls, entry_data):
        return mongo.db.entries.insert_one(entry_data)

    @classmethod
    def update_entry(cls, entry_id, entry_data):
        return mongo.db.entries.update_one({"_id": ObjectId(entry_id)}, {"$set": entry_data})

    @classmethod
    def delete_entry(cls, entry_id):
        return mongo.db.entries.delete_one({"_id": ObjectId(entry_id)})

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "date": self.date,
        }
