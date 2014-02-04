#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from ConfigParser import ConfigParser, NoSectionError, NoOptionError

logger = logging.getLogger("root")

homepath = os.path.expanduser('~')
dot_prercious = os.path.join(homepath, '.precious')


def get_config_path():
    return dot_prercious


def get_config_file_path():
    return os.path.join(dot_prercious, 'precious.conf')


def get_logger_config_file_path():
    return os.path.join(dot_prercious, 'logging.conf')


def parse_config():
    config = ConfigParser()
    config.readfp(open(get_config_file_path()))
    return config


def get_logs_directory():
    return os.path.join(dot_prercious, 'logs')


def get_db_uri():
    return parse_config().get('database',
                              'uri').replace('$HOME', os.path.expanduser('~'))


def get_build_directory():
    config = parse_config()
    try:
        return config.get('worker', 'build_directory')
    except NoSectionError:
        logger.warn("No section worker in config file")
        return os.path.join(homepath, 'precious_build')


def get_worker_port():
    config = parse_config()
    try:
        return int(config.get('worker', 'port'))
    except (NoSectionError, NoOptionError):
        logger.warn("No port worker section in config file")

        return 22222


def get_worker_host():
    config = parse_config()
    try:
        return config.get('worker', 'host')
    except (NoSectionError, NoOptionError):
        logger.warn("No host in worker section in config file")
        return 'localhost'
