#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("worker")

import rpyc
from datetime import datetime
from itertools import chain
from precious import db
from precious.utils import get_worker_host, get_worker_port
from precious.models import Project, Build

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
            directory = "{0}_{1}".format(self.project.id, '_'.join(
                                         self.project.name.lower().split()))
            logging.info("Startrting project: {0}".format(self.project.name))
            self.connection.root.mkdir(directory)
            self.config["directory"] = directory
            self.config["status"] = STARTED
            self.config["repository"] = "https://github.com/bzyx/precious.git"
            self.config["branch"] = "master"
            self.project.config = self.config
            db.session.add(self.project)
            db.session.commit()
        else:
            logging.info(
                "Project: {0} already started.".format(self.project.name))

    def build_project(self):
        directory = self.project.config['directory']
        self.connection.root.set_cwd(directory)
        self.connection.root.run_command(
            "git clone https://github.com/bzyx/precious.git")
        self.connection.root.cd("precious")
        revision = self.connection.root.run_command(
            "git rev-parse HEAD")["stdout"][0]
        build = Build(self.project, revision)

        outputs = []
        build_steps = self.project.build_steps
        if build_steps is None:
            build_steps = []

        build_steps.append("echo dupa")
        build_steps.append("ls")
        build_steps.append("cat requirements.txt")
        for step in build_steps:
            output = self.connection.root.run_command(step)
            outputs.append(output)
        #" \n".join(out["stdout"]) for out in outputs
        # print outputs[0]["stdout"]
        #import pdb; pdb.set_trace()
        combined = list(
            chain.from_iterable([out["stdout"] for out in outputs]))
        build.stdout = " \n".join(combined)
        build.succes = outputs[-1]["returncode"]

        self.project.history.append(build)

        db.session.add(self.project)
        db.session.commit()

    def remove_poject(self):
        pass

    def is_project_building(self):
        pass
