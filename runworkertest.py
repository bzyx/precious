#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rpyc

c = rpyc.connect('localhost', 22222)
print c.root.say_hello()

import pdb; pdb.set_trace()
