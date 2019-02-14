# encoding: utf-8
# from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app import app
from app.api.login import login
from app.api.signup import signup

CORS(app)
api = Api(app)
api.add_resource(login, '/api/login/')
api.add_resource(signup, '/api/signup/')

if __name__ == '__main__':
    app.run(debug=True)
