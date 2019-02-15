# encoding: utf-8
from flask import g
from flask_restful import Resource, request
from app import db, auth
from app.models import User, Article, Comment
from app.etc import success_msg, fail_msg


class add_comment(Resource):
    '发布评论'


    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        content = data.get("content")
        article_id = data.get("article_id")
        author_id = g.user.id
        if not content:
            return fail_msg(msg='内容不能为空！')
        if not Article.query.filter_by(article_id=article_id).first():
            return fail_msg(msg='该文章不存在！')
        if Article.query.filter_by(article_id=article_id, can_have_comments=False).first():
            return fail_msg(msg='该文章不能被评论！')
        article = Comment(content=content, author_id=author_id, article_id=article_id)
        db.session.add(article)
        db.session.commit()
        return success_msg
