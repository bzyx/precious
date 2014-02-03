# -*- coding: utf-8 -*-

from precious import db
from enum import Enum

UserRole = Enum('Admin', 'User')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True)
    role = db.Column(db.SmallInteger, default=UserRole.User)
    provider = db.Column(db.String(16), index=True)
        
    def __repr__(self):
        return '<User %r>' % (self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
