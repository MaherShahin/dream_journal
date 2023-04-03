# backend/app/models/user.py
from bson.objectid import ObjectId

class User:
    def __init__(self, data):
        self.id = str(data["_id"]) if "_id" in data else None
        self.email = data["email"]
        self.hashed_password = data["hashed_password"]
        self.first_name = data.get("first
