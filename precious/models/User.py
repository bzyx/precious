# -*- coding: utf-8 -*-

from precious import db
from enum import Enum
from hashlib import sha256
from datetime import datetime

UserRole = Enum('User', 'Admin')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True)
    role = db.Column(db.SmallInteger, default=UserRole.User.index)
    provider = db.Column(db.String(16), default="Local", index=True)
    password = db.Column(db.LargeBinary(32))
    last_login = db.Column(db.DateTime)
    registered = db.Column(db.DateTime)

    def __init__(self, name, provider="Local", password=None):
        self.name = name
        self.provider = provider
        self.registered = datetime.now()
        if password:
            self.set_password(password)

    def __repr__(self):
        return '<User id:%r name:%s>' % (self.id, self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password(self, p):
        self.password = sha256(p).digest()

    def check_password(self, p):
        if self.password == sha256(p).digest():
            return True
        else:
            return False
