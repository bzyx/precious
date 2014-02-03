"""
Basic example showing how to start the scheduler and schedule a job that executes on 3 second intervals.
"""

import logging
from datetime import datetime

from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.sqlalchemy_store import SQLAlchemyJobStore

from precious.utils import get_db_uri
from precious.sheduler.tasks import *



logger = logging.getLogger("scheduler")

def tick():
    print('Tick! The time is: %s' % datetime.now())
    logger.info('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = Scheduler(standalone=True, misfire_grace_time=10,
                          coalescing=False)
    #Works strange with sqlite...
    #scheduler.add_jobstore(SQLAlchemyJobStore(get_db_uri()), 'default')

    scheduler.add_interval_job(tick, seconds=5)
    scheduler.add_interval_job(tick, seconds=5)

    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
