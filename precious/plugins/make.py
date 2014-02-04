# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Make(Build_step):
    @staticmethod
    def description():
        return ('Makefile',
                {'configure': ('Use configure:', FormElements.Checkbox),
                 'configure_args': ('Configure arguments:', FormElements.Text),
                 'make_clean': ('Run make clean:', FormElements.Checkbox),
                 'make_install': ('Run make install:', FormElements.Checkbox),
                 })

    def __init__(self, **kwargs):
        for key in self.description()[1].keys():
            if key not in kwargs.keys():
                kwargs[key] = u''
        super(Make, self).__init__(**kwargs)

    def get_commands(self):
        commands = []

        if self.args['make_clean']:
            commands.append('make clean')

        if self.args['configure']:
            commands.append('./configure %s' % self.args['configure_args'])

        commands.append('make')

        if self.args['make_install']:
            commands.append('make install')

        return commands
