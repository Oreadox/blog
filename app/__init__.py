# encoding: utf-8

from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from app.models import User
from flask import g


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True
