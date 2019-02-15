# encoding: utf-8

from flask_restful import Api
from flask_cors import CORS
from app import app
from app.api.login import login
from app.api.signup import signup
from app.api.add_article import add_article
from app.api.add_comment import add_comment

CORS(app)
api = Api(app)
api.add_resource(login, '/api/login/')
api.add_resource(signup, '/api/signup/')
api.add_resource(add_article, '/api/add_article/')
api.add_resource(add_comment, '/api/add_comment/')

if __name__ == '__main__':
    app.run(debug=True)
