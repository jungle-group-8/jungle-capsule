import os
from dotenv import load_dotenv
import certifi
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

db = client["jungle-capsule"]




