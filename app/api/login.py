# encoding: utf-8

from flask_restful import Resource, reqparse
from app import db
from app.models import User



class login(Resource):
    '用户登录'

    def __init__(self):
        self.success_msg = {
            "status": 1,
            "message": "成功!"
        }
        self.parser = reqparse.RequestParser()

    def post(self):
        args = self.parser.parse_args()
        username = args.get("username")
        password = args.get("password")
        if not username or not password:
            return self.fail_msg(msg="输入错误!")
        if User.query.filter_by(username=username,password=password).first():
            pass
        else:
            return self.fail_msg(msg="用户名或密码错误!")

    def fail_msg(self,msg):
        message={
            "status": 0,
            "message": msg
        }
        return message

