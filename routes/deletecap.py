from flask import Flask,render_template,request,jsonify
from bson import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime

client=MongoClient(os.getenv("MONGO_URL"))
db=client["jungle-capsule"]
collection=db["items"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/delete_Capsule', methods =['POST'])
def deleteCapsule():
    delete_id = request.form['id_give']
    db.Capsule.delete_one({'_id':ObjectId(delete_id)})
    return redirect(request.referrer or url_for('home'))
