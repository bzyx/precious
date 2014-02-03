#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        t = ThreadedServer(PreciousWorkerService, port=22222)
        t.start()
