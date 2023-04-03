from bson.objectid import ObjectId
from backend.app.utils.database import mongo

class User:
    def __init__(self, data):
        self.id = str(data["_id"]) if "_id" in data else None
        self.email = data["email"]
        self.hashed_password = data["hashed_password"]
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data)

    @staticmethod
    def get_all_users():
        return mongo.db.users.find()

    @staticmethod
    def get_user_by_id(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def create_user(user_data):
        return mongo.db.users.insert_one(user_data)

    @staticmethod
    def update_user(user_id, update_data):
        return mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})

    @staticmethod
    def delete_user(user_id):
        return mongo.db.users.delete_one({"_id": ObjectId(user_id)})
