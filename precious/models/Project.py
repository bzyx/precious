# -*- coding: utf-8 -*-

import json
from precious import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(80), index=True, unique=True)
    description = db.Column(db.UnicodeText)
    build_steps = db.Column(db.PickleType, default=[])
    schedule = db.Column(db.PickleType, default=None)
    config = db.Column(db.PickleType(pickler=json))
    history = db.relationship(
        "Build", cascade="all,delete", backref="projects")

    def __init__(self, name, description="", build_steps=[]):
        self.name = name
        self.description = description
        self.build_steps = build_steps

    def __repr__(self):
        return '<Project id:%r name:%s>' % (self.id, self.name)
