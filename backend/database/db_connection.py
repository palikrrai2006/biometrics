from pymongo import MongoClient
from backend.config.settings import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

users_collection = db["users"]
logs_collection = db["access_logs"]
