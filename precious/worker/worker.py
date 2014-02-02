#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rpc.PreciousWorkerService import PreciousWorkerService
from utils import *


if __name__ == "__main__":
    print get_ip_addr()
    print get_uname()
    #from rpyc.utils.server import ThreadedServer
    #t = ThreadedServer(PreciousWorkerService, port=22222)
    #t.start()
