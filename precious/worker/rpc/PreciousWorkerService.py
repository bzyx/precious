#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rpyc
from sarge import run, Capture

class PreciousWorkerService(rpyc.Service):

    def on_connect(self):
        print "on_connect(self):"

    def on_disconnect(self):
        print "on_disconnect(self):"

    def exposed_say_hello(self):
        print "Hello!"
        p = run("uname -a", stdout=Capture())
        print p.stdout.text
        return p.stdout.text


    def exposed_say_hello_par(self, name):
        print "Hello! " + name
        return "Hello " + name

