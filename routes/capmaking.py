from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

capmaking = Blueprint('capmaking',__name__,url_prefix='/capmaking')

@capmaking.route('/making_Capsule', methods =['POST'])
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
