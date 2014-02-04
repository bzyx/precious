#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("worker")

import rpyc
from datetime import datetime
from itertools import chain
from precious import db
from precious.plugins import Git
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
        revision = self.connection.root.run_command(
            git_command.revision_command())["stdout"][0]
        build_directory = "{0}_{1}".format(self.project_name_uniform, revision)

        self.connection.root.cd(directory)
        self.config["status"] = BUILD
        self.connection.root.mkdir(build_directory)
        self.connection.root.cd(build_directory)

        build = Build(self.project, revision)
        build.date = timestamp_
        build_steps = self.project.build_steps

        logging.info("Starting build.")
        self.config["status"] = BUILDING

        build.succes = True
        for step in build_steps:
            for line in step.get_commands():
                logging.debug("RUNNING: {0} {1} : {2}".format(
                              self.project_name_uniform, revision, line))
                output = self.connection.root.run_command(line)
                if output["returncode"] != 0:
                    build.succes = False
                outputs.append(output)

        combined = list(
            chain.from_iterable([out["stdout"] for out in outputs]))
        build.stdout = " \n".join(combined)
        #build.succes = outputs[-1]["returncode"]

        self.connection.root.cd("..")
        self.connection.root.rmrf(build_directory)

        self.config["status"] = BUILD

        self.project.config = self.config
        self.project.history.append(build)
        db.session.add(self.project)
        db.session.commit()
        logging.info("End of buid project: {0}.".format(
            self.project.name))

    def check_revison(self):
            logging.info("Checking revision project: {0}.".format(
                self.project.name))
            git_command = self.project.build_steps[0]
            if not isinstance(git_command, Git):
                return False
            if len(self.project.history) == 0:
                return True
            revison_in_db = self.project.history[-1].revision
            revision_in_git = self.connection.root.run_command(
                git_command.revision_command())["stdout"][0]
            logging.info("DB: {0} GIT: {1}".format(
                revison_in_db, revision_in_git))

            return revison_in_db != revision_in_git

    def remove_poject(self):
        pass

    def is_project_building(self):
        pass
