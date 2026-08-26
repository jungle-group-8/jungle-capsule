from flask import Blueprint, render_template, request

capsule_bp = Blueprint("capsule", __name__)

@capsule_bp.route("/")
def main():
    return render_template("capsule/main.html")

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
    return render_template("capsule/storage.html")
