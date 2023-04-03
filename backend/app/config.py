import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/dream_journal")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "secret_key")
