from flask import Blueprint, render_template

capsule_bp = Blueprint("capsule", __name__)

@capsule_bp.route("/")
def main():
    return render_template("capsule/main.html")

@capsule_bp.route("/create")
def create_choice():
    return render_template("capsule/create-choice.html")

@capsule_bp.route("/create-capsule")
def create_capsule():
    return render_template("capsule/create-capsule.html")

@capsule_bp.route("/capsule-storage")
def capsule_storage():
    return render_template("capsule/storage.html")