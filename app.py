from flask import Flask,render_template,request,jsonify,session,redirect,url_for
from bson import ObjectId
from pymongo import MongoClient
from routes.capsule import capsule_bp
from routes.auth import auth_bp

from services.auth import login #blueprint사용 login.py import
from database import client   #database에서 client  변수 가져옴

import os
from datetime import datetime
import random
from routes import capmaking,capsulelist,checkcap,deletecap,detailcpa,member,question




app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.register_blueprint(login.auth_bp)

app.register_blueprint(capmaking.capmaking)
app.register_blueprint(capsulelist.caplist)
app.register_blueprint(checkcap.checkcap)
app.register_blueprint(deletecap.deletecap)
app.register_blueprint(detailcpa.detailcap)
app.register_blueprint(member.members)
app.register_blueprint(question.question)

app.register_blueprint(capsule_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)
   