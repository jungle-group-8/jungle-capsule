from flask import Blueprint,render_template

auth_page_bp = Blueprint("authpage", __name__)

@auth_page_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_page_bp.route("/sign-up")
def sign_up():
    return render_template("auth/signup.html")

