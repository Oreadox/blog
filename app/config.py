# encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)
HOST = 'localhost'
PORT = '3306'
DATABASE = 'db1'
USERNAME = 'user'
PASSWORD = 'user'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

