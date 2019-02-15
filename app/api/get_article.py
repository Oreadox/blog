# encoding: utf-8

from flask_restful import Resource, reqparse, reqparse
from flask import g, jsonify
from app import db, auth
from app.models import User, Article
from app.etc import fail_msg


class get_article(Resource):
    '查看文章[获取文章内容(包含评论)]'

    parser = reqparse.RequestParser()

    @auth.login_required
    def get(self):
        data = self.parser.parse_args()
        article_id = data.get("id")
        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return fail_msg(msg="该文章不存在！")
        output = {}
        output['article'] = article.to_json()
        output['comments'] = {comment.to_json() for comment in article.comments}
        return jsonify(output)
