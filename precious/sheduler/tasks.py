#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("scheduler")


from precious import models
from precious.worker import ProjectManagment


def check_remote_git_revision():
    logger.info("Checking project remote revision")
    for project in models.Project.query.all():
        pm = ProjectManagment(project)
        pm.start_project()
        if pm.check_revison() is True:
            pm.build_project()


def check_should_buid():
    logger.info("Checking for project need to be build")
    for project in models.Project.query.all():
        pm = ProjectManagment(project)
        pm.start_project()
        pm.build_project()


def check_project_buid_web():
    logger.info("Will build project from web")
    for project in models.Project.query.all():
        pm = ProjectManagment(project)
        pm.start_project()
        if pm.check_project_shedudled() is True:
            pm.build_project()
