# encoding: utf-8

from flask_restful import Resource, request
from flask import g
from app import db, auth
from app.models import User, Article
from app.etc import success_msg, fail_msg


class set_article(Resource):
    '设置文章能否被评论'

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        article_id = data.get("id")
        enable_comment = data.get("enable_comment")
        if not g.user.is_admin:
            return fail_msg(msg='非管理员不能进行相关设置！')
        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return fail_msg(msg='该文章不存在！')
        article.can_have_comments = enable_comment
        db.session.commit()
        return success_msg
