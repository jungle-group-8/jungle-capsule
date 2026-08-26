from flask import Flask,render_template,request,jsonify
from bson import ObjectId
from pymongo import MongoClient
import os




app = Flask(__name__)






if __name__ == '__main__':  
   app.run('0.0.0.0', port=5001, debug=True)