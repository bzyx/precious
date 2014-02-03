# -*- coding: utf-8 -*-

from base import Build_step, FormElements


class Custom_commands(Build_step):
    @staticmethod
    def description():
        return ('Custom user build script',
                {'text': ['Commands:', FormElements.Textarea]})

    def get_commands(self):
        return self.args['text'].split('\n')
