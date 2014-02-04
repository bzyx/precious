#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rpyc
from precious.utils import get_worker_port

c = rpyc.connect('localhost', get_worker_port())
print c.root.sysinfo()
print c.root.run_command("ls")
print c.root.mkdir("precious")
print c.root.cd("precious")
print c.root.run_command("git clone https://github.com/bzyx/precious.git")
print c.root.run_command("ls", timeout=0.01)
print c.root.set_cwd("/home/bzyx/precious_build/")
print c.root.cd("..")
print c.root.run_command("ls")
print c.root.rmrf("precious")


import pdb;pdb.set_trace()
