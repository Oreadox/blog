# encoding: utf-8

from flask_restful import Resource ,request
from app import db
from app.models import User
from app.etc import success_msg, fail_msg


class signup(Resource):
    '创建用户'

    def post(self):
        data = request.get_json(force=True)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        print("email={}".format(email))
        if not username or not password or not email:
            return fail_msg(msg="输入错误!")
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return fail_msg(msg="用户名或邮箱已注册!")
        user = User(username=username, email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return success_msg
