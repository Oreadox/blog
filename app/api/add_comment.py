# encoding: utf-8
from flask_restful import Resource, request
from app import db, auth
from app.models import User, Article, Comment


class add_comment(Resource):
    '发布评论'

    def __init__(self):
        self.success_msg = {
            "status": 1,
            "message": "成功!"
        }

    @auth.login_required
    def post(self):
        dict = request.get_json(force=True)
        content = dict.get("content")
        article_id = dict.get("article_id")
        author_id = ''
        if not content:
            return self.fail_msg(msg='内容不能为空！')
        if not Article.query.filter_by(article_id=article_id).first():
            return self.fail_msg(msg='该文章不存在！')
        if Article.query.filter_by(article_id=article_id, can_have_comments=False).first():
            return self.fail_msg(msg='该文章不能被评论！')
        article = Comment(content=content, author_id=author_id, article_id=article_id)
        db.session.add(article)
        db.session.commit()
        return self.success_msg

    def fail_msg(self, msg):
        message = {
            "status": 0,
            "message": msg
        }
        return message
