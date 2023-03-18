from flask import render_template
from app.auth import auth

@auth.route('/login')
def login_handler():
    return render_template("auth/login.html")

@auth.route('/register')
def register_handler():
    return render_template("auth/register.html")
