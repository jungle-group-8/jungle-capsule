from flask import Blueprint,request,redirect,url_for,render_template,session,flash
from datetime import datetime
from database import db
from bson import ObjectId


capmaking = Blueprint('capmaking',__name__,url_prefix='/capmaking')

@capmaking.route('/making_Capsule', methods=['POST'])
def makingCapsule():
    user_id = session.get('id')

    if not user_id:
        return render_template('auth/login.html')

    doc = {
        'sendId': user_id,
        'receiveId': request.form['receiveId'],
        'CreatedAt': datetime.today(),
        'openTime': datetime.strptime(request.form['openTime'], '%Y-%m-%d'),
        'title': request.form['title'],
        'previewTitle': request.form['previewTitle'],
        'contents': request.form['contents'],
        # 'photo': request.form['photo'],
        # 'video': request.form['video'],
        'link': request.form['link'],
        'isOpen': False
    }

    db.Capsule.insert_one(doc)
    flash("캡슐이 정상적으로 저장되었습니다.")
    return redirect(url_for("capsule.main"))