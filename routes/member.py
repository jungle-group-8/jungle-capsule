from flask import Blueprint, jsonify, session
from database import db

members = Blueprint('capmember',__name__,url_prefix='/capmember')

# doc = {
#     'members': [
#         "정진영(13기-72)",
#         "조성준(정글13기-73)",
#         "조은(정글13기-74)",
#         "조은아(정글13기-13)",
#         "조재후(정글13기-14)",
#         "조진근(정글13기-75)",
#         "최동호(정글13기-15)",
#         "최진웅(13기-76)",
#         "최현욱(정글 13기-77)",
#         "한정민(정글13기-78)",
#         "허준강(정글13기-42)"
#     ]
# }
# db.members.insert_one(doc)

@members.route('/member', methods=['GET'])
def member():
    user_id = session.get('id')

    if not user_id:
        return jsonify({'result': 'fail', 'message': '로그인이 필요합니다.'}), 401

    user = db.Users.find_one({'id': user_id})

    if not user:
        return jsonify({'result': 'fail', 'message': '사용자 정보가 없습니다.'}), 404

    curriculum = user.get("curriculum")
    class_ = user.get("class")

    print("curriculum:", curriculum, type(curriculum).__name__, flush=True)
    print("class:", class_, flush=True)
    if not curriculum or not class_:
        return jsonify({'result': 'fail', 'message': '커리큘럼 또는 기수 정보가 없습니다.'}), 400

    class_values = [class_]
    try:
        numeric_class = int(str(class_).strip())
        class_values.extend([numeric_class, str(numeric_class)])
    except ValueError:
        pass

    print("curriculum query value:", repr(curriculum), flush=True)
    print("class query values:", class_values, flush=True)

    member_list = list(
        db.Users.find(
            {
                'id': {'$ne': user_id},
                'curriculum': curriculum,
                'class': {'$in': class_values}
            },
            {
                '_id': 0,
                'id': 1,
                'name': 1
            }
        )
    )

    return jsonify({'result': 'success', 'members': member_list})
