import logging

from apscheduler.scheduler import Scheduler
#from apscheduler.jobstores.sqlalchemy_store import SQLAlchemyJobStore
#from precious.utils import get_db_uri
from tasks import *


logger = logging.getLogger("scheduler")

scheduler = Scheduler(standalone=True, misfire_grace_time=10, coalescing=False)
#scheduler.add_jobstore(SQLAlchemyJobStore(get_db_uri()), 'file')

scheduler.add_interval_job(check_remote_git_revision, seconds=30)
scheduler.add_interval_job(check_should_buid, minutes=30)
