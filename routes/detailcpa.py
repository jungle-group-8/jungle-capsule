from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

detailcap = Blueprint('capdetail',__name__,url_prefix='/capdetail')

@detailcap.route('/detail_Capsule/<capsule_id>', methods=['GET'])
def detail_Capsule(capsule_id):
    
    if not ObjectId.is_valid(capsule_id):
        return  "유효하지않음"
    capsules = db.Capsule.find_one({'_id':ObjectId(capsule_id)})
    if not capsules:
            return "유효하지않음"
    # if capsules['receiveId'] != session.get('user_id'):
    #     return
    
    now = datetime.now()
    if now <capsules['openTime']:
        return render_template('locked.html', capsules=capsules)
    return render_template('detail.html',capsules=capsules)

