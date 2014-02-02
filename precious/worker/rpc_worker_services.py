#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("worker")

import rpyc
from sarge import run, Capture, shell_format
from worker_utils import *

from precious.utils import get_config_path

class PreciousWorkerService(rpyc.Service):

    def on_connect(self):
        print "on_connect(self):"
        logger.info("TEST MESSAGE")

    def on_disconnect(self):
        print "on_disconnect(self):"

    def exposed_sysinfo(self):
        print "Sending sysinfo"
        return [get_ip_addr(), get_uname(), get_free_ram(),
                get_free_space(get_config_path())]


    def exposed_run_command(self, command):
        print "RUNNING: ", command
        p = run(command, stdout=Capture())
        return p.stdout.text.split("\n")


    def exposed_say_hello_par(self, name):
        print "Hello! " + name
        return "Hello " + name

