#!/usr/bin/env python
# -*- coding: utf-8 -*-

from precious.utils import get_worker_port
from rpc_worker_services import PreciousWorkerService
from worker_utils import *

import logging
logger = logging.getLogger("worker")


class Worker(object):

    def __init__(self):
        pass

    def main(self):
        logger.info("Worker just staring.")
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(PreciousWorkerService, port=get_worker_port())
        t.start()
