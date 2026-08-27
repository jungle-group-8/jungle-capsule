from flask import Blueprint, request
from database import db
from bson import ObjectId

deletecap = Blueprint('capdelete',__name__,url_prefix='/capdelete')


@deletecap.route('/delete_Capsule', methods =['DELETE'])
def deleteCapsule():
    delete_id = request.form['id_give']
    db.Capsule.delete_one({'_id':ObjectId(delete_id)})
    return {'result': 'success'}, 200
