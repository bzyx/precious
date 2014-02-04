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

(NONE, STARTED,  BUILD, REMOVED, BUILDING, ERROR) = range(6)


class ProjectManagment(object):

    def __init__(self, project_obj):
        assert isinstance(project_obj, Project)
        self.project = project_obj
        self.connection = rpyc.connect(get_worker_host(), get_worker_port())
        self.config = self.project.config
        self.project_name_uniform = '_'.join(self.project.name.lower().split())

        if self.config is None:
            self.config = {"status": NONE}

    def start_project(self):
        if self.config is not None and self.config["status"] < STARTED:
            directory = "{0}_{1}".format(self.project.id,
                                         self.project_name_uniform)
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
            logging.debug(
                "Project: {0} already started.".format(self.project.name))

    def build_project(self):
        logging.info("Building project: {0}.".format(self.project.name))
        directory = self.project.config['directory']
        status = self.config["status"]
        outputs = []
        timestamp_ = datetime.now()
        git_command = self.project.build_steps[0]
        print git_command, type(git_command)
        revision = self.connection.root.run_command(
            git_command.revision_command())["stdout"][0]
        print revision, type(revision)
        build_directory = "{0}_{1}".format(self.project_name_uniform, revision)
        self.connection.root.cd(directory)
        self.config["status"] = BUILD
        self.connection.root.mkdir(build_directory)
        self.connection.root.cd(build_directory)

        # if status >= STARTED and status < CLONED:
        #     logging.info("First time build. Clonning from VCS.")
        #     outputs.append(self.connection.root.run_command(
        #                    "git clone https://github.com/bzyx/precious.git"))
        #     self.config["status"] = CLONED
        # else:
        #     logging.info("Running pull from VCS.")
        #     self.connection.root.cd("precious")
        #     outputs.append(self.connection.root.run_command("git pull"))
        # revision = self.connection.root.run_command(
        #     "git rev-parse HEAD")["stdout"][0]

        build = Build(self.project, revision)
        build.date = timestamp_
        build_steps = self.project.build_steps

        logging.info("Starting build.")
        self.config["status"] = BUILDING
        #build_steps.append("echo dupa")
        # build_steps.append("ls")
        #build_steps.append("cat requirements.txt")
        for step in build_steps:
            for line in step.get_commands():
                logging.debug("RUNNING: {0} {1} : {2}".format(
                              self.project_name_uniform, revision, line))
                output = self.connection.root.run_command(line)
                outputs.append(output)
        #" \n".join(out["stdout"]) for out in outputs
        # print outputs[0]["stdout"]
        #import pdb; pdb.set_trace()
        combined = list(
            chain.from_iterable([out["stdout"] for out in outputs]))
        build.stdout = " \n".join(combined)
        build.succes = outputs[-1]["returncode"]

        self.connection.root.cd("..")
        self.connection.root.rmrf(build_directory)

        self.config["status"] = BUILD

        self.project.config = self.config
        self.project.history.append(build)
        db.session.add(self.project)
        db.session.commit()

    def remove_poject(self):
        pass

    def is_project_building(self):
        pass
