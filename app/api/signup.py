# encoding: utf-8

from flask_restful import Resource, reqparse
from app import db
from app.models import User


class signup(Resource):
    '创建用户'

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
        email = args.get("email")
        if not username or not password or not email:
            return self.fail_msg(msg="输入错误!")
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return self.fail_msg(msg="用户名或邮箱已注册!")
        user = User(username=username, email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return self.success_msg

    def fail_msg(self,msg):
        message={
            "status": 0,
            "message": msg
        }
        return message

