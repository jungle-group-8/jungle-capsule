from flask import Flask,render_template,request,jsonify
from bson import ObjectId
from pymongo import MongoClient
import os

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("capsule/main.html")

@app.route("/create")
def create_choice():
    return render_template("capsule/create-choice.html")

@app.route("/create-capsule")
def create_capsule():
    return render_template("capsule/create-capsule.html")

@app.route("/capsule-storage")
def capsule_storage():
    return render_template("capsule/storage.html")

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/sign-up")
def sign_up():
    return render_template("auth/signup.html")

try:
    client.admin.command("ping")
    print("MongoDB 연결 성공")
except Exception as e:
    print("MongoDB 연결 실패")
    print(e)


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)