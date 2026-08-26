from flask import Flask,render_template,request,jsonify,session,redirect,url_for
from bson import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime
import random

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]

app = Flask(__name__)

@app.route('/list_Capsule/<user_id>', methods = ['GET'])
def list_Capsule(user_id):
    capsules = list(db.Capsule.find({'receiveId':user_id}))
    for capsule in capsules :
        if capsules['openTime'] > datetime.today():
            doc = {
                'id':ObjectId(capsules['_id']),
                'dDay':(datetime(capsules['openTime']) - datetime.today()),
                'previewTitle': capsules['previewTitle'],
                'isOpen':False
             }
        else:
            doc = {
                    'id':ObjectId(capsules['_id']),
                    'dDay':"0",
                    'previewTitle': capsules['previewTitle'],
                    'isOpen':True
             }
    db.Capsule_list.insert_one(doc)
    