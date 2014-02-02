#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpc_worker_services import PreciousWorkerService
from worker_utils import *

import logging
logger = logging.getLogger("worker")

class Worker(object):
    def __init__(self):
        logging.warn("message warn")
        pass

    def main(self):
        logger.info("1111111111111111111111111111TEST")

        #print get_ip_addr()
        #print get_uname()
        #print get_free_ram()
        #print get_free_space("/home/bzyx/Development/")
        logger.debug("222222222222222222222222")
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(PreciousWorkerService, port=22222)
        t.start()
