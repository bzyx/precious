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
        logger.info("CONNECTED")

    def on_disconnect(self):
        logger.info("DISCONNECTED")

    def exposed_sysinfo(self):
        print "Sending sysinfo"
        return [get_ip_addr(), get_uname(), get_free_ram(),
                get_free_space(get_config_path())]


    def exposed_run_command(self, command):
        print "RUNNING: ", command
        return run_command(command)

    def exposed_run_command_raw(self, command):
        print "RUNNING: ", command
        return run_command_raw_output(command)

    def exposed_run_command_silient(self, command):
        print "RUNNING: ", command
        return run_command_forget_output(command)


    def exposed_say_hello_par(self, name):
        print "Hello! " + name
        return "Hello " + name


