#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("scheduler")

import rpyc

from precious import db, models
from precious.utils import get_worker_port
from precious.worker import ProjectManagment

def build_precious():
    c = rpyc.connect('localhost', get_worker_port())
    print c.root.sysinfo()
    print c.root.run_command("ls")
    print c.root.mkdir("precious")
    print c.root.cd("precious")
    print c.root.run_command("git clone https://github.com/bzyx/precious.git")
    print c.root.run_command("ls", timeout=0.01)
    print c.root.set_cwd("/home/bzyx/precious_build/")
    print c.root.cd("..")
    print c.root.run_command("ls")
    print c.root.rmrf("precious")
    c.close()

def check_remote_git_revision():
    logger.info("Checking project remote revision")
    proj = models.Project.query.all()[0]
    pm = ProjectManagment(proj)
    pm.start_project()



def check_should_buid():
    logger.info("Checking for project need to be build")
    #build_precious()
    # for proj in models.Project.query.all():
    #   if proj.schedule - timedelta?
    #         proj.schedule =
    #        proj.build())
