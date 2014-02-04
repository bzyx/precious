#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("worker")

import rpyc
from precious import db
from precious.utils import get_worker_host, get_worker_port
from precious.models import Project


(NONE, STARTED, BUILD, REMOVED, BUILDING, ERROR) = range(6)


class ProjectManagment(object):

    def __init__(self, project_obj):
        assert isinstance(project_obj, Project)
        self.project = project_obj
        self.connection = rpyc.connect(get_worker_host(), get_worker_port())
        self.config = self.project.config
        if self.config is None:
            self.config = {"status": NONE}

    def start_project(self):
        if self.config is not None and self.config["status"] < STARTED:
            logging.info("Startrting project: {0}".format(self.project.name))
            directory = "{0}_{1}".format(self.project.id, '_'.join(
                                         self.project.name.lower().split()))
            self.connection.root.mkdir(directory)
            self.config["directory"] = directory
            self.config["status"] = STARTED
            self.project.config = self.config
            db.session.add(self.project)
            db.session.commit()
        else:
            logging.info(
                "Project: {0} already started.".format(self.project.name))

    def build_project(self):
        pass

    def remove_poject(self):
        pass

    def is_project_building(self):
        pass
