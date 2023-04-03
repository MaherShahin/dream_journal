import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)
mongo = client.get_default_database()
