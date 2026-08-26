from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

checkcap = Blueprint('capcheck',__name__,url_prefix='/capcheck')

@checkcap.route('/check_Capsule/<user_id>', methods =['GET'])
def check_Capsule(user_id):
    # user_id = session.get('uesr_id') #사용자 아이디

    # if not user_id:
    #     return redirect(url_for(long_page))
    
    capslues = list(db.Capsule.find({'receiveId':user_id}))
    if not capslues:
        return "존재하지않습니다."
    for c in capslues:
        c['_id'] = str(c['_id'])
    return capslues #render_template('index.html', capsules=capslues, now=datetime.now())