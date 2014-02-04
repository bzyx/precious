# -*- coding: utf-8 -*-

__all__ = []

import pkgutil
import inspect
from exceptions import NotImplementedError
from enum import Enum

FormElements = Enum("Text", "Password", "Textarea", "Checkbox")


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


for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith('__'):
            continue

        globals()[name] = value
        __all__.append(name)


def get_build_steps():
    build_steps = {}
    for name in __all__:
        module = globals()[name]
        if inspect.isclass(module) \
           and issubclass(module, Build_step) \
           and not issubclass(module, Vcs) \
           and module is not Build_step:
            build_steps[name] = module
    return build_steps
