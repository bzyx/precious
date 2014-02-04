# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Virtualenv(Build_step):
    @staticmethod
    def description():
        return (u'Python Virtual Environment',
                {'name': (u'Name:', FormElements.Text),
                 'python': (u'Python interpreter:', FormElements.Text),
                 'clear': (u'Clear out:', FormElements.Checkbox),
                 'system-site-packages': (u'System site packages:', FormElements.Checkbox),
                 })

    def __init__(self, **kwargs):
        for key in self.description()[1].keys():
            if key not in kwargs.keys():
                kwargs[key] = u''
        super(Virtualenv, self).__init__(**kwargs)

    def get_commands(self):
        if not self.args['name']:
            return [u"echo \"No virtualenv name set\"", u"exit 1"]

        commands = []
        pars = u" "
        if self.args['clear']:
            pars += u"--clear "
        if self.args['system-site-packages']:
            pars += u"--system-site-packages "
        commands.append(u"virtualenv -p %s~/.virtualenvs/%s" % (self.args['python'], pars, self.args['name']))
        commands.append(u"source ~/.virtualenvs/%s/bin/activate" % (self.args['name']))
        return commands
