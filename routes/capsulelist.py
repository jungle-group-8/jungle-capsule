from flask import Blueprint,request,redirect,url_for,render_template,session
from datetime import datetime,timedelta
from database import db
from bson import ObjectId

caplist = Blueprint('caplist',__name__,url_prefix='/caplist')

@caplist.route('/list_Capsule/<user_id>', methods = ['GET'])
def list_Capsule(user_id):
    capsules = list(db.Capsule.find({'receiveId':user_id}))
    capsules_list =[]
    for capsule in capsules :
        open_time = capsule['openTime']
        today = datetime.now()

        if today < open_time :
            dday = (open_time - today).days + 1
            is_open = False
        else :
            dday = "오픈가능"
            is_open = True
            db.Capsule.update_one({'_id':capsule['_id']},{'$set':{'isOpen':True}})

        doc = {
                'id':str(capsule['_id']),
                'user_id': capsule['sendId'], ####
                'dDay': dday,
                'previewTitle': capsule['previewTitle'],
                'isOpen':is_open
             }
        capsules_list.append(doc)

    return render_template('main.html',capsules_list=capsules_list)

#db.Capsule_list.update_many({'sendId':session.get('user_Id')},{'$set':{'isOpen':False}})
@caplist.route('/count_cap', methods = ['GET'])
def count_cap():
    openCap = list(db.Capsule.find({'receiveId':session.get('user_id'),'isOpen':True}))
    OpenCapCount = len(openCap)
    CloseCap = list(db.Capsule.find({'receiveId':session.get('user_id')}))
    CloseCapCount = len(CloseCap) - OpenCapCount
    today_start = datetime.now().replace(hour=0, minute=0, second=0)
    tomorrow_start = today_start + timedelta(days =1)

    create = list(db.Capsule.find({'receiveId':session.get('user_id'),'CreatedAt':{'$gte': today_start,'$lt':tomorrow_start}}))
    CreateCount = len(create)
    return render_template('main.html', OpenCapCount=OpenCapCount, CloseCapCount= CloseCapCount, CreateCount=CreateCount)