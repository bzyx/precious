# -*- coding: utf-8 -*-

import jsonpickle
import json
from precious import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(80), index=True, unique=True)
    description = db.Column(db.UnicodeText)
    _build_steps = db.Column("build_steps", db.Text, default="[]")
    _schedule = db.Column("schedule", db.Text)
    config = db.Column(db.PickleType(pickler=json))
    history = db.relationship(
        "Build", cascade="all,delete", backref="projects")

    def __init__(self, name, description="", conf=[]):
        self.name = name
        self.description = description
        self.conf = conf

    @property
    def build_steps(self):
        jsonpickle.decode(self._build_steps)

    @build_steps.setter
    def build_steps(self, build_steps):
        self._build_steps = jsonpickle.encode(build_steps)

    @build_steps.deleter
    def build_steps(self):
        self._build_steps = jsonpickle.encode([])

    @property
    def schedule(self):
        jsonpickle.decode(self._schedule)

    @schedule.setter
    def schedule(self, schedule):
        self._schedule = jsonpickle.encode(schedule)

    @schedule.deleter
    def schedule(self):
        self._schedule = jsonpickle.encode([])

    def __repr__(self):
        return '<Project id:%r name:%s>' % (self.id, self.name)
