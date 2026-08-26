from flask import session, Blueprint, request,jsonify,render_template, redirect, url_for
from database import db
from enum import Enum #enum값 사용 위함

class Class(Enum):
    SW_AI = 1
    Game = 2
    Game_tech = 3

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods = ['POST'])
def login(): #아이디가 없으면 "사용자 없음", 비밀번호만 틀리면 "비밀번호가 틀림 알림 가도록"

    userId = request.form['id']
    userPw = request.form['pw']
    isUser = db.Users.find_one({"id": userId})
    if isUser is not None: #사용자가 있다면
        if db.Users.find_one({"id": userId, "pw": userPw}) is not None: #비번까지 검증
            #정보 가져오기
            user = db.Users.find_one({"id":userId, "pw": userPw})
            session['id'] = userId
            session['name'] = user["name"]
            session['curriculum'] = user['curriculum']
            session['class'] = user['class']

            isSuccess = "success"
            #return render_template("login.html", success = isSuccess ) #(변수) 판단후 넘김
            #return jsonify({'result': 'success'})
            return redirect(url_for("capsule.main")) #로그인 페이지로 이동
        else: #비밀번호가 틀리다면
            session['id'] = None
            isSuccess = "pw_fail"
            #return render_template("auth/login.html")
            return render_template("auth/login.html", success = isSuccess)
            #return render_template("auth/login.html", success = isSuccess)
            #return jsonify({'result': 'pw_fail'})
            #return redirect(url_for('login')) #로그인 페이지로 이동 #redirect할때 메모도 같이 보낼 수 있는지 확인

    else: #사용자가 없다면
        session['id'] = None
        isSuccess = "id_fail"
        return render_template("auth/login.html", success = isSuccess)
        #return render_template("auth/login.html")
        #return jsonify({'result': 'id_fail'})
        #return redirect(url_for('index')) #자신의 페이지로 이동
        #return jsonify({'id': userId, 'pw': userPw})

@auth_bp.route('/logout', methods = ['POST'])
def logout():
    session.pop('id',None)
    #return jsonify({'result': 'success'})
    return render_template("login.html", success = "logout_success" )


@auth_bp.route('/signup', methods = ['POST'])
def signup():#프론트에서 id 중복체크 필수로 만듬
    name_receive = request.form.get("name")
    id_receive = request.form.get("id")
    pw_receive = request.form.get("pw")
    curriculum_receive = request.form.get("curriculum")
    class_receive = request.form.get("class")
    mailAdress_receive = request.form.get("mailAddress")
    isJungler_receive = request.form.get("isJungler")

    required_fields = {
        "name": name_receive,
        "id": id_receive,
        "pw": pw_receive,
        "curriculum": curriculum_receive,
        "class": class_receive,
        "mailAddress": mailAdress_receive,
        "isJungler": isJungler_receive,
    }
    missing_fields = [key for key, value in required_fields.items() if not value]
    if missing_fields:
        return jsonify({
            "result": "fail",
            "message": "필수 입력값이 누락되었습니다.",
            "missing_fields": missing_fields,
        }), 400



    #isJungler 일치로직
    if  isJungler_receive == "Jungle@55Krafton":
        db.Users.insert_one({
        "name":name_receive,
        "id":id_receive,
        "pw":pw_receive,
        "curriculum": curriculum_receive,
        "class": class_receive,
        "mailAdress": mailAdress_receive,
        })
    else:
        return jsonify({'result': 'jungler_fail'})

    #fortest
    if db.Users.find_one({"name": name_receive,"id":id_receive}) is not None:
        return jsonify({'result': 'success'}, {"name": name_receive,"id":id_receive})
    else:
        return jsonify({'result': 'fail'})



@auth_bp.route('/signup/idCheck', methods = ['POST'])
def idCheck():
    id_receive= request.form["id"]
    user = db.Users.find_one({"id": id_receive})
    if user is None:
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'fail'})

@auth_bp.route('/getUserInfo', methods = ['GET'])
def getUserInfo():
    sId = session['id']
    sName = session['name']
    sCurriculum = session['curriculum']
    sClass = session['class']
    # return jsonify({"id":sId, "name":sName, "curriculum":sCurriculum, "class":sClass})
    return render_template("components/header.html", Id=sId,name=sName,curriculum=sCurriculum,class_name=sClass)
