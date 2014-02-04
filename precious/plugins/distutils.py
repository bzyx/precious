# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Distutils(Build_step):
    @staticmethod
    def description():
        return ('Distutils',
                {'command': ('Command:', FormElements.Text)
                 })

    def __init__(self, **kwargs):
        for key in self.description()[1].keys():
            if key not in kwargs.keys():
                kwargs[key] = u''

        super(Distutils, self).__init__(**kwargs)

        if not self.args['command']:
            self.args['command'] = u"build"

    def get_commands(self):
        if not self.args['command']:
            return [u"echo \"No command for setup.py set\"", u"exit 1"]

        return [u"python setup.py %s" % (self.args['command'])]
