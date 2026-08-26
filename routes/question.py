from flask import Blueprint,request,redirect,url_for,render_template
from datetime import datetime
from database import db
from bson import ObjectId
import random

question = Blueprint('capquestion',__name__,url_prefix='/capquestion')

if db.Question.count_documents({}) == 0:
    QA_base = [{
    'Id':"min",
    'questionList':"오늘의 가장 고마웠던 사람이 누구인가요?",
    'CreatedAt':datetime.now()
        },
        {
    'Id':'jun',
    'questionList':"오늘의 배운 내용 중 하나를 미래의 나에게 보내보세요!",
    'CreatedAt':datetime.now()
        },
        {
        'Id':'soso',
        'questionList':"이번주 팀원들에게 한마디씩!",
        'CreatedAt':datetime.now()
        }]
    db.Question.insert_many(QA_base)

@question.route('/making_QA', methods =['POST'])
def making_QA():
    db_count = db.Question.count_documents({})
    if db_count > 3:
        old_Question = db.Question.find_one(sort=[('CreatedAt',1)])
        if old_Question:
            db.Question.delete_one({'_id':old_Question['_id']})
    doc = {
    'Id' : request.form['Id'],
    'questionList' : request.form['questionList'],
    'CreatedAt' : datetime.now()
    }
    db.Question.insert_one(doc)
    return '성공'


@question.route('/show_QA', methods =['GET'])
def show_QA():
    question = list(db.Question.find({}))
    rand_question = random.choice(question)
    qa = rand_question['questionList']
    return qa #render_template('qa.html',qa = qa)