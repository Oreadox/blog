# encoding: utf-8

from app import db
from app.config import SECRET_KEY
from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), index=True, nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    articles = db.relationship("Article", backref='author')
    comments = db.relationship("Comment", backref='author')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def hash_password(self, password):
        self.password_hash = custom_app_context.encrypt(password)

    def verify_password(self, password):
        return custom_app_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=60 * 60 * 24):
        serialize = Serializer(SECRET_KEY, expires_in=expiration)
        return serialize.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        serialize = Serializer(SECRET_KEY)
        try:
            data = serialize.loads(token)
        except SignatureExpired:
            return None  # token已过期
        except BadSignature:
            return None  # token无效
        # id = data['id']
        # return id
        user = User.query.get(data['id'])
        return user


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text)
    comments = db.relationship("Comment", backref='article')
    can_have_comments = db.Column(db.Boolean, nullable=False, default=True)
    datetime = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, content, author_id, article_id):
        self.content = content
        self.author_id = author_id
        self.article_id = article_id

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
