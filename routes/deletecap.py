from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId

deletecap = Blueprint('capdelete',__name__,url_prefix='/capdelete')


@deletecap.route('/delete_Capsule', methods =['POST'])
def deleteCapsule():
    delete_id = request.form['id_give']
    db.Capsule.delete_one({'_id':ObjectId(delete_id)})
    return redirect(request.referrer or url_for('home'))
