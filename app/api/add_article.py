# encoding: utf-8

from flask_restful import Resource, request

from app import db, auth
from app.models import User, Article


class add_article(Resource):
    '发布文章'

    def __init__(self):
        self.success_msg = {
            "status": 1,
            "message": "成功!"
        }

    @auth.login_required
    def post(self):
        dict = request.get_json(force=True)
        title = dict.get("title")
        content = dict.get("content")
        author_id = ''
        if not title:
            return self.fail_msg(msg='标题不能为空！')
        if not User.query.filter_by(id=author_id, is_admin=True).first():
            return self.fail_msg(msg='非管理员不能发布文章！')
        article = Article(title=title, content=content, author_id=author_id)
        db.session.add(article)
        db.session.commit()
        return self.success_msg

    def fail_msg(self, msg):
        message = {
            "status": 0,
            "message": msg
        }
        return message
