from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, Required, Length, EqualTo

class RegisterForm(FlaskForm):
    Email = StringField('Email', validators = [Required(), Length(1, 64), Email()])
    Password = PasswordField('Password', validators=[Required(), EqualTo('Password2', 
    message='Passwords must match.')])
    Password2 = PasswordField('Confirm password', validators=[Required()])
    Submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Length(1, 64), Email()])
    password = PasswordField(('Password'), validators=[Required()])
    remember_me = BooleanField(('Remember Me'))
    submit = SubmitField(('Sign In'))