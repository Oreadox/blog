# encoding: utf-8

from app import db
from app.config import SECRET_KEY
from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature


class User(db.Model):
    __table_name__ = 'users'
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
        return serialize.dumps({'username': self.username})

    @staticmethod
    def verify_auth_token(token):
        serialize = Serializer(SECRET_KEY)
        try:
            data = serialize.loads(token)
        except SignatureExpired:
            return None  # token已过期
        except BadSignature:
            return None  # token无效

        username = data['username']
        return username
        # user = User.query.get(data['id'])
        # return user


class Article(db.Model):
    __table_name__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255), nullable=False, index=True)
    content = db.Column(db.Text)
    comments = db.relationship("Comment", backref='article')
    can_have_comments = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id


class Comment(db.Model):
    __table_name__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    content = db.Column(db.Text)

    def __init__(self, content, author_id, article_id):
        self.content = content
        self.author_id = author_id
        self.article_id = article_id
