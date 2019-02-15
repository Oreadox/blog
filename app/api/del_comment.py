# encoding: utf-8
from flask import g
from flask_restful import Resource, request
from app import db, auth
from app.models import User, Article, Comment
from app.etc import success_msg, fail_msg


class del_comment(Resource):
    '删除评论'

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        comment_id = data.get("id")
        if not g.user.is_admin:
            return fail_msg(msg='非管理员不能删除评论！')
        comment = Comment.query.filter_by(id=comment_id).first()
        if not comment:
            return fail_msg(msg='该评论不存在！')
        db.session.delete(comment)
        db.session.commit()
        return success_msg
