# -*- coding: utf-8 -*-

from precious.plugins import Vcs, FormElements


class Git(Vcs):
    @staticmethod
    def description():
        return ('Git',
                {'repo': ('Remote repository url', FormElements.Text),
                 'branch': ('Selected branch', FormElements.Text)
                 })

    def __init__(self, **kwargs):
        if 'repo' not in kwargs.keys():
            kwargs['repo'] = u''
        if 'branch' not in kwargs.keys():
            kwargs['branch'] = u''
        super(Git, self).__init__(**kwargs)

    def get_commands(self):
        return ["git clone -v --depth 1 --branch {0} {1} .".format(self.args['branch'], self.args['repo'])]

    def revision_command(self):
        return "git ls-remote {1} {0}".format(self.args['branch'], self.args['repo']) + " | awk '{print $1}'"
