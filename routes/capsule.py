from flask import Blueprint, render_template, request, session
from routes.capsulelist import get_capsules_list
from routes.question import show_QA
from routes.capsulelist import count_cap

capsule_bp = Blueprint("capsule", __name__)

@capsule_bp.route("/")
def main():
    qa=show_QA()
    countCapDic = count_cap()
    return render_template("capsule/main.html",qa = qa ,count_cap = countCapDic)

@capsule_bp.route("/create")
def create_choice():
    return render_template("capsule/create-choice.html")

@capsule_bp.route("/create-capsule")
def create_capsule():
    receiver_id = request.args.get("receiverId", "").strip()
    return render_template(
        "capsule/create-capsule.html",
        receiver_id=receiver_id
    )

@capsule_bp.route("/capsule-storage")
def capsule_storage():
    user_id = session.get("id")

    if not user_id:
        return render_template("auth/login.html")

    capsules_list = get_capsules_list(user_id)

    return render_template(
        "capsule/storage.html",
        capsules_list=capsules_list
    )
