# -*- coding: utf-8 -*-

from exceptions import NotImplementedError
from enum import Enum

FormElements = Enum("Text", "Password", "Email", "Radio", "Checkboxes", "Textarea")


class Build_step(object):
    @staticmethod
    def description():
        raise NotImplementedError()

    def __init__(self, **kwargs):
        self.args = kwargs

    def set_args(self, **kwargs):
        self.args = kwargs

    def get_args(self):
        return self.args

    def get_commands(self):
        raise NotImplementedError()


class Vcs(Build_step):
    def revision_command(self):
        raise NotImplementedError()
