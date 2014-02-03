# -*- coding: utf-8 -*-

from precious import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), index=True, unique=True)
    description = db.Column(db.Text)
    conf = db.Column(db.LargeBinary)

    def __init__(self, name, description="", conf=None):
        self.name = name
        self.description = description
        self.conf = conf

    def __repr__(self):
        return '<Project %r %s>' % (self.id, self.name)
