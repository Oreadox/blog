# encoding: utf-8

from flask_restful import Resource, request
from flask import g
from app import db, auth
from app.models import User, Article
from app.etc import success_msg, fail_msg


class add_article(Resource):
    '发布文章'

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        title = data.get("title")
        content = data.get("content")
        author_id = g.user.id
        if not title:
            return fail_msg(msg='标题不能为空！')
        if not g.user.is_admin:
            return fail_msg(msg='非管理员不能发布文章！')
        article = Article(title=title, content=content, author_id=author_id)
        db.session.add(article)
        db.session.commit()
        return success_msg
