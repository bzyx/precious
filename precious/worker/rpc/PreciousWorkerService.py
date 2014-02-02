#-*- coding: utf-8 -*-

import rpyc


class PreciousWorkerService(rpyc.Service):

    def on_connect(self):
        print "on_connect(self):"

    def on_disconnect(self):
        print "on_disconnect(self):"

    def exposed_say_hello(self):
        print "Hello!"
        return "Hello"

    def exposed_say_hello_par(self, name):
        print "Hello! " + name
        return "Hello " + name

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PreciousWorkerService, port=22222)
    t.start()
