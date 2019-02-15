# encoding: utf-8


from flask_restful import Resource, request
from flask import g
from app import db, auth
from app.models import User, Article
from app.etc import success_msg, fail_msg


class del_article(Resource):
    '删除文章'

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        article_id = data.get("id")
        if not g.user.is_admin:
            return fail_msg(msg='非管理员不能删除文章！')
        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return fail_msg(msg='该文章不存在！')
        db.session.delete(article)
        db.session.commit()
        return success_msg
