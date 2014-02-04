# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Make(Build_step):
    @staticmethod
    def description():
        return (u'Makefile',
                {'configure': (u'Use configure:', FormElements.Checkbox),
                 'configure_args': (u'Configure arguments:', FormElements.Text),
                 'make_clean': (u'Run make clean:', FormElements.Checkbox),
                 'make_install': (u'Run make install:', FormElements.Checkbox),
                 })

    def __init__(self, **kwargs):
        for key in self.description()[1].keys():
            if key not in kwargs.keys():
                kwargs[key] = u''
        super(Make, self).__init__(**kwargs)

    def get_commands(self):
        commands = []

        if self.args['make_clean']:
            commands.append(u'make clean')

        if self.args['configure']:
            commands.append(u'./configure %s' % self.args['configure_args'])

        commands.append(u'make')

        if self.args['make_install']:
            commands.append(u'make install')

        return commands
