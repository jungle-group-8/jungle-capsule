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




        
        




if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)