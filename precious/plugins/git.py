# -*- coding: utf-8 -*-

from base import Vcs, FormElements


class Git(Vcs):
    @staticmethod
    def description():
        return ('Git plugin',
                {'repo': ('Remote repository url', FormElements.Text),
                 'branch': ('Selected branch', FormElements.Text)
                 })

    def get_commands(self):
        return ["git clone -v --depth 1 --branch {0} {1} .".format(self.args['branch'], self.args['repo'])]

    def revision_command(self):
        return "git ls-remote {1} {0}".format(self.args['branch'], self.args['repo']) + " | awk '{print $1}'"
