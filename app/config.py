# encoding: utf-8
# import os

DEBUG = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = "S83rQ53gC4vdarcIAvY89Ky4"
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db1'
USERNAME = 'user'
PASSWORD = 'user'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=True

