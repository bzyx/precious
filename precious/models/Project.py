# -*- coding: utf-8 -*-

import jsonpickle
import json
from precious import db
from sqlalchemy.types import PickleType


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(80), index=True, unique=True)
    description = db.Column(db.UnicodeText)
    _conf = db.Column("conf", db.Text, default="[]")
    _schedule = db.Column("schedule", db.Text)
    config = db.Column(PickleType(pickler=json))
    history = db.relationship(
        "Build", cascade="all,delete", backref="projects")

    def __init__(self, name, description="", conf=[]):
        self.name = name
        self.description = description
        self.conf = conf

    @property
    def conf(self):
        jsonpickle.decode(self._conf)

    @conf.setter
    def conf(self, conf):
        self._conf = jsonpickle.encode(conf)

    @conf.deleter
    def conf(self):
        self._conf = jsonpickle.encode([])

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
