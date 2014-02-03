# -*- coding: utf-8 -*-
from exceptions import NotImplementedError
from enum import Enum

FormElements = Enum("Text", "Password", "Email", "Radio", "Checkboxes" "Textarea")


class Build_step(object):
    def set_args(self, **args):
        raise NotImplementedError()

    def get_args(self):
        raise NotImplementedError()

    @staticmethod
    def description():
        raise NotImplementedError()

    def get_commands(self):
        raise NotImplementedError()


class Vcs(Build_step):
    def revision_command(self):
        raise NotImplementedError()
