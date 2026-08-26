from flask import Flask,render_template,request,jsonify,session,redirect,url_for
from bson import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime
import random
from routes import capmaking,capsulelist,checkcap,deletecap,detailcpa,member,question

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]



app = Flask(__name__)
app.register_blueprint(capmaking.capmaking)
app.register_blueprint(capsulelist.caplist)
app.register_blueprint(checkcap.checkcap)
app.register_blueprint(deletecap.deletecap)
app.register_blueprint(detailcpa.detailcap)
app.register_blueprint(member.members)
app.register_blueprint(question.question)


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)