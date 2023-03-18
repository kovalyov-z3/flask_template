from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from app.auth import auth as auth_blueprint

def create_app(config_class = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app