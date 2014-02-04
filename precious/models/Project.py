# -*- coding: utf-8 -*-

import json
from copy import deepcopy
from precious import db
from precious.plugins import Git


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

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.build_steps = [Git()]

    def __repr__(self):
        return '<Project id:%r name:%s>' % (self.id, self.name)

    def build_step_append(self, step):
        bs = deepcopy(self.build_steps)
        bs.append(step)
        self.build_steps = bs

    def build_step_remove(self, index):
        bs = deepcopy(self.build_steps)
        del bs[index]
        self.build_steps = bs

    def build_step_move_up(self, index):
        bs = deepcopy(self.build_steps)
        bs[index-1], bs[index] = bs[index], bs[index-1]
        self.build_steps = bs

    def build_step_move_down(self, index):
        bs = deepcopy(self.build_steps)
        bs[index+1], bs[index] = bs[index], bs[index+1]
        self.build_steps = bs
