from flask import Blueprint, jsonify, session
from datetime import datetime
from database import db
from bson import ObjectId
from services.imageupload import view_file

detailcap = Blueprint('capdetail',__name__,url_prefix='/capdetail')

@detailcap.route('/detail_Capsule/<capsule_id>', methods=['GET'])
def detail_Capsule(capsule_id):
    user_id = session.get('id')

    if not user_id:
        return jsonify({'message': '로그인이 필요합니다.'}), 401

    if not ObjectId.is_valid(capsule_id):
        return jsonify({'message': '유효하지 않은 캡슐 ID입니다.'}), 400

    capsule = db.Capsule.find_one({
        '_id': ObjectId(capsule_id),
        'receiveId': user_id
    })

    if not capsule:
        return jsonify({'message': '캡슐을 찾을 수 없습니다.'}), 404

    now = datetime.now()

    if now < capsule['openTime']:
        return jsonify({'message': '아직 열 수 없는 캡슐입니다.'}), 403

    sender = db.Users.find_one({
        'id': capsule.get('sendId')
    })

    if sender:
        sender_name = sender.get('name', '알수없음')
    else:
        sender_name = '알수없음'

    presigned_url = None
    if capsule.get('objectKey'):
        presigned_url = view_file(capsule.get('objectKey'))

    doc = {
        'title': capsule.get('title'),
        'sendId': sender_name,
        'previewTitle': capsule.get('previewTitle'),
        'contents': capsule.get('contents'),
        'link': capsule.get('link'),
        'presignedUrl':presigned_url,
        'CreatedAt': capsule.get('CreatedAt')
    }

    if doc['CreatedAt']:
        doc['CreatedAt'] = doc['CreatedAt'].isoformat()

    return jsonify(doc)
