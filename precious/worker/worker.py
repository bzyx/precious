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
        print "THIS IS IMPORTANT COPY THOSE TO WEB CONTROL PANEL"
        print "PUBLIC HOSTNAME: ",get_public_hostname()
        print "PUBLIC IP ADDR:  ",get_public_ip_addr()
        print "IP ADDR:         ",get_ip_addr()
        print "WILL START IN 2 SECONDS                        !"
        import time
        time.sleep(2)

        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(PreciousWorkerService, port=get_worker_port())
        t.start()
