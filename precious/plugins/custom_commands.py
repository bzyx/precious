# -*- coding: utf-8 -*-

from precious.plugins import Build_step, FormElements


class Custom_commands(Build_step):
    @staticmethod
    def description():
        return ('Custom user build script',
                {'text': ('Commands:', FormElements.Textarea)})

    def get_commands(self):
        return [line for line in self.args['text'].split('\n') if line != ""]
