#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from apscheduler.scheduler import Scheduler
#from apscheduler.jobstores.sqlalchemy_store import SQLAlchemyJobStore
#from precious.utils import get_db_uri
from precious.sheduler.tasks import *


logger = logging.getLogger("scheduler")


if __name__ == '__main__':
    scheduler = Scheduler(standalone=True, misfire_grace_time=10,
                          coalescing=False)
    #scheduler.add_jobstore(SQLAlchemyJobStore(get_db_uri()), 'file')

    scheduler.add_interval_job(check_remote_git_revision, seconds=30)
    scheduler.add_interval_job(check_should_buid, minutes=30)

    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
