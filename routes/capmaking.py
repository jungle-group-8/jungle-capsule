from flask import Flask,render_template,request,jsonify
from bson import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]

app = Flask(__name__)

@app.route('/making_Capsule', methods =['POST'])
def makingCapsule():
    doc = {
        'sendId' : request.form['sendId'],
        'receiveId' : request.form['receiveId'],
        'CreatedAt' : datetime.now(),
        'openTime' : datetime.strptime(request.form['openTime'],'%Y-%m-%d'),
        'title' : request.form['title'],
        'previewTitle' : request.form['previewTitle'],
        'contents' : request.form['contents'],
        #'photo' : request.form['photo'],
        #'video' : request.form['video'],
        'link' : request.form['link'],
        'isOpen' : False
    }
    db.Capsule.insert_one(doc)
    return "유효"
