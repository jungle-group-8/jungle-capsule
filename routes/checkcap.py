from flask import Flask,render_template,request,jsonify
from bson import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_Capsule/<user_id>', methods =['GET'])
def check_Capsule(user_id):
    # user_id = session.get('uesr_id') #사용자 아이디

    # if not user_id:
    #     return redirect(url_for(long_page))
    
    capslues = list(db.item.find({'receiveId':user_id}))
    for c in capslues:
        c['_id'] = str(c['_id'])

    return render_template('index.html', capsules=capslues, now=datetime.now())