# encoding: utf-8

from app import db
from app.config import SECRET_KEY
from passlib.apps import custom_app_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired,BadSignature


class User(db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), index=True, nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, default=0, nullable=False)

    def __init__(self, id, username, email, admin):
        self.id = id
        self.username = username
        self.email = email
        self.admin = admin
        # self.password_hash = password_hash

    # def __repr__(self):
    #     return '<User %r>' % self.name

    def hash_password(self, password):
        self.password_hash = custom_app_context.encrypt(password)

    def verify_password(self, password):
        return custom_app_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=60*60*24):
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