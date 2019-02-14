# encoding: utf-8

from flask import Flask,abort,g
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(config)
auth = HTTPBasicAuth()

