import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevConfig:
    SECRET_KEY = "a really long secret key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:########/vacuum_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False