# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Custom_commands(Build_step):
    @staticmethod
    def description():
        return ('Custom user build script',
                {'text': ('Commands:', FormElements.Textarea)})

    def __init__(self, **kwargs):
        if not kwargs['text']:
            kwargs['text'] = u''
        super(Custom_commands, self).__init__(**kwargs)

    def get_commands(self):
        return [line for line in self.args['text'].split('\n') if line != ""]
