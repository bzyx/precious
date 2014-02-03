#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("scheduler")

from precious import db, models

def check_remote_git_revision():
    logger.info("Checking project remote revision")
    print models.Project.query.all()
