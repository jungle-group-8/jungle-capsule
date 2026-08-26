from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

caplist = Blueprint('caplist',__name__,url_prefix='/caplist')

@caplist.route('/list_Capsule/<user_id>', methods = ['GET'])
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
                    'dDay':"오픈가능",
                    'previewTitle': capsules['previewTitle'],
                    'isOpen':True
             }
    db.Capsule_list.insert_one(doc)
    