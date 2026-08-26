from flask import Blueprint,request,redirect,url_for,render_template,session
from datetime import datetime
from database import db
from bson import ObjectId

caplist = Blueprint('caplist',__name__,url_prefix='/caplist')

@caplist.route('/list_Capsule', methods=['GET'])
def list_Capsule():
    user_id = session.get('id')

    if not user_id:
        return render_template('auth/login.html')

    capsules = list(
        db.Capsule.find({'receiveId': user_id})
    )

    if not capsules:
        return None

    capsules_list = []
    today = datetime.now()

    for capsule in capsules:
        open_time = capsule['openTime']

        if today < open_time:
            d_day = (open_time - today).days + 1
            is_open = False
        else:
            d_day = "오픈가능"
            is_open = True

            db.Capsule.update_one(
                {'_id': capsule['_id']},
                {'$set': {'isOpen': True}}
            )

        doc = {
            'id': str(capsule['_id']),
            'user_id': capsule['sendId'],
            'dDay': d_day,
            'previewTitle': capsule['previewTitle'],
            'isOpen': is_open
        }

        capsules_list.append(doc)
    return render_template(
        'capsule/storage.html',
        capsules_list=capsules_list
    )