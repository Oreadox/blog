# encoding: utf-8

from flask import g
from flask_restful import Resource, reqparse, request
from app import db
from app.models import User
from app.etc import success_msg, fail_msg



class login(Resource):
    '用户登录'

    # def __init__(self):
    #     self.parser = reqparse.RequestParser()

    def post(self):
        dict = request.get_json(force=True)
        # args = self.parser.parse_args()
        username = dict.get("username")
        password = dict.get("password")
        if not username or not password:
            return fail_msg(msg="输入错误!")
        if User.query.filter_by(username=username,password=password).first():
            token = g.user.generate_auth_token()
            return ({'token': token.decode('ascii')})
        else:
            return fail_msg(msg="用户名或密码错误!")
