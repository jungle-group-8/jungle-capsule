from flask import Blueprint,render_template

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bp.route("/sign-up")
def sign_up():
    return render_template("auth/signup.html")

