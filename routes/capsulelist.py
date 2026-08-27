from flask import Blueprint,session,render_template
from datetime import datetime,timedelta
from database import db

caplist = Blueprint('caplist',__name__,url_prefix='/caplist')

def get_capsules_list(user_id):
    print("조회할 receiveId:", repr(user_id), flush=True)

    capsules = list(
        db.Capsule.find({"receiveId": user_id})
    )

    print("조회된 캡슐 개수:", len(capsules), flush=True)
    print("조회 결과:", capsules, flush=True)

    if not capsules:
        return []

    capsules_list = []
    today = datetime.now()

    for capsule in capsules:
        open_time = capsule['openTime']

        if today < open_time:
            d_day = (open_time - today).days + 1
            is_open = False
        else:
            d_day = "Day"
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
    return capsules_list

def count_cap():
    user_id = session.get('id')

    if not user_id:
        return render_template('auth/login.html')

    openCap = list(
        db.Capsule.find({
            'receiveId': user_id,
            'isOpen': True
        })
    )
    OpenCapCount = len(openCap)
    today_start = datetime.now().replace(
            hour=0,
            minute=0,
            second=0
        )
    tomorrow_start = today_start + timedelta(days=1)

    # 오늘 작성한 캡슐
    SendCap = list(
        db.Capsule.find({
            'sendId': user_id,
            'CreatedAt': {
                            '$gte': today_start,
                            '$lt': tomorrow_start
                        }
        })
    )
    SendCapCount = len(SendCap)

    

    create = list(
        db.Capsule.find({
            'receiveId': user_id,
            'CreatedAt': {
                '$gte': today_start,
                '$lt': tomorrow_start
            }
        })
    )
    CreateCount = len(create)

    return {"OpenCapCount" : OpenCapCount,
        "CloseCapCount" : SendCapCount,
        "CreateCount" :CreateCount}