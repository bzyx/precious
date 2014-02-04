# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Virtualenv(Build_step):
    @staticmethod
    def description():
        return ('Python Virtual Environment',
                {'name': ('Name:', FormElements.Text),
                 'python': ('Python interpreter:', FormElements.Text),
                 'clear': ('Clear out:', FormElements.Checkbox),
                 'system-site-packages': ('System site packages:', FormElements.Checkbox),
                 })

    def __init__(self, **kwargs):
        for key in self.description()[1].keys():
            if key not in kwargs.keys():
                kwargs[key] = u''
        super(Virtualenv, self).__init__(**kwargs)

    def get_commands(self):
        if not self.args['name']:
            return ["echo \"No virtualenv name set\"", "exit 1"]

        commands = []
        pars = " "
        if self.args['clear']:
            pars += "--clear "
        if self.args['system-site-packages']:
            pars += "--system-site-packages "
        commands.append("virtualenv -p %s~/.virtualenvs/%s" % (self.args['python'], pars, self.args['name']))
        commands.append("source ~/.virtualenvs/%s/bin/activate" % (self.args['name']))
        return commands
