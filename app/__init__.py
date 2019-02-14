from flask import Flask,abort,g
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth
from app.models import User

app = Flask(__name__)
db=SQLAlchemy(app)
app.config.from_object(config)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

