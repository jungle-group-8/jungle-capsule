from pymongo import MongoClient
import os

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]

try:
    client.admin.command("ping")
    print("MongoDB 연결 성공")
except Exception as e:
    print("MongoDB 연결 실패")
    print(e)
