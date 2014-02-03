# -*- coding: utf-8 -*-
from precious import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
        
    def __repr__(self):
        return '<User %r>' % (self.id)