from flask import render_template, flash, redirect, url_for
from app.auth import auth
from app.auth.forms import RegisterForm, LoginForm 
from app.models import User
from app.models import db
from flask_login import login_user, current_user

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return "You are logged in!"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
    return render_template("auth/login.html", form=form)

@auth.route('/register', methods=["GET", "POST"])
def register_handler():
    form = RegisterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        
        user = User(email = form.Email.data)
        user.set_password(form.Password.data)
        db.session.add(user)
        db.session.commit()
        flash("All right!")
    
    return render_template("auth/register.html", form=form)

