import os
class Config():
    REGISTERED_USERS = {
    'christinaparece@gmail.com':{"name":"Christina","password":"beasty"},
    'beasty@gmail.com':{"name":"Christina","password":"beasty"}
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")