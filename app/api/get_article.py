# encoding: utf-8

from flask_restful import Resource, request
from flask import g, jsonify
from app import db, auth
from app.models import User, Article
from app.etc import fail_msg, to_json


class get_article(Resource):
    '查看文章[获取文章内容(包含评论)]'

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        article_id = data.get("id")
        article = Article.query.filter_by(id=article_id).first()
        if not article:
            return fail_msg(msg="该文章不存在！")
        output = {}
        output['article'] = to_json(article.__dict__.copy())
        if article.comments:
            output['comments'] = {to_json(comment.__dict__.copy()) for comment in article.comments}
        else:
            output['comments'] = {}
        return jsonify(output)
