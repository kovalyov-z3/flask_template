from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from app.auth import auth as auth_blueprint
from app.models import db, login
from flask_alembic import Alembic


def create_app(config_class = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login.init_app(app)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
