#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("worker")

import rpyc
import os.path
from sarge import run, Capture, shell_format
from worker_utils import *

from precious.utils import get_config_path, get_build_directory


class PreciousWorkerService(rpyc.Service):

    def on_connect(self):
        """
           Use this as __init__
        """
        logger.info("CONNECTED")
        self.cwd = get_build_directory()

    def on_disconnect(self):
        """
            disconnection
        """
        logger.info("DISCONNECTED")

    def exposed_sysinfo(self):
        """
            informations about the machine
        """
        logger.debug("SENDING SYSINFO")
        return {"local_ip": get_ip_addr(),
                "public_ip": get_public_ip_addr(),
                "hostname": get_public_hostname(),
                "free_ram": get_free_ram(),
                "size_of_build_directory": get_free_space(get_config_path()),
                }

    def exposed_run_command(self, command, timeout=None):
        """
            run a command and return the output splited by new lines
        """
        logger.debug("RUNNING: {0}".format(command))
        return run_command(command, timeout=timeout, cwd=self.cwd, )

    def exposed_run_command_raw(self, command, timeout=None):
        """
            run a command and return the raw output
        """
        logger.debug("RUNNING: {0}".format(command))
        return run_command_raw_output(command, timeout=timeout, cwd=self.cwd)

    def exposed_run_command_silient(self, command, timeout=None):
        """
            rund a command and don't return the output
        """
        logger.debug("RUNNING: {0}".format(command))
        return run_command_forget_output(command, cwd=self.cwd)

    def exposed_set_cwd(self, new_cwd):
        """
            set new working directory. it must be inside the building directory
        """
        logger.debug("Change cwd to: {0}".format(new_cwd))
        if new_cwd.startswith(get_build_directory()):
            self.cwd = new_cwd
        else:
            return {'output': "cwd must be insisde build directory",
                    'returncode': 1,
                    'command': ""}

    def exposed_get_cwd(self, new_cwd):
        """
            get current directory
        """
        return self.cwd

    def exposed_cd(self, cd_to):
        """
            classic 'cd' command.
            with safeguard for going outside the build directory
        """
        logger.debug("Run cd to: {0}".format(cd_to))
        if (cd_to == ".."):
            if (os.path.normpath(self.cwd) == get_build_directory()):
                return

        self.cwd = os.path.normpath(os.path.join(self.cwd, cd_to))
        logger.debug("New cwd: {0}".format(self.cwd))

    def exposed_mkdir(self, dir_):
        """
            classic 'mkdir'
        """
        logger.debug("Creating directory {0}".format(dir_))
        formated = shell_format('mkdir  {0}', dir_)
        logger.debug("Creating formated {0}".format(formated))
        return run_command_forget_output(formated, cwd=self.cwd)

    def exposed_rmrf(self, dir_):
        """
            classid 'rm -rf'
        """
        logger.debug("Removing directory {0}".format(dir_))
        return run_command_forget_output(
            shell_format('rm -rf  {0}', dir_), cwd=self.cwd)
