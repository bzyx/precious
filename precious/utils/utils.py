#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

homepath = os.path.expanduser('~')
dot_prercious = os.path.join(homepath, '.precious')

def get_config_path():
    return dot_prercious

def get_config_file_path():
    return os.path.join(dot_prercious, 'precious.conf')

def get_logger_config_file_path():
    return os.path.join(dot_prercious, 'logging.conf')

def get_logs_directory():
    return os.path.join(dot_prercious, 'logs')

def get_build_directory():
    # TODO: THIS IS A MOCKUP - SHOULD BE READ FROM DB OR CONFIG FILE
    return os.path.join(homepath, 'precious_build')
