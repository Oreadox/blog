from flask import Flask,abort
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth

# from models import *

app = Flask(__name__)
db=SQLAlchemy()
app.config.from_object(config)
auth = HTTPBasicAuth()

