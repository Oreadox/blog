# encoding: utf-8

from flask_restful import Resource, request
from app import db
from app.models import User

class signup(Resource):
    '发布文章'

    def __init__(self):
        self.success_msg = {
            "status": 1,
            "message": "成功!"
        }
        self.fail_msg = {
            "status": 0,
            "message": "发布失败!"
        }

    def post(self):
        pass
