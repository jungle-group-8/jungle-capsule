from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

members = Blueprint('capmember',__name__,url_prefix='/capmember')

doc = {
    'members': [
        "정진영(13기-72)",
        "조성준(정글13기-73)",
        "조은(정글13기-74)",
        "조은아(정글13기-13)",
        "조재후(정글13기-14)",
        "조진근(정글13기-75)",
        "최동호(정글13기-15)",
        "최진웅(13기-76)",
        "최현욱(정글 13기-77)",
        "한정민(정글13기-78)",
        "허준강(정글13기-42)"
    ]
}
db.members.insert_one(doc)

@members.route('/member', methods=['GET'])
def member():
    member = list(db.members.find())
    return render_template('member.html' , member=member)