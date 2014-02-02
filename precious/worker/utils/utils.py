#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sarge import run, Capture


def get_ip_addr():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    socket_name = s.getsockname()[0]
    s.close()
    return socket_name


def get_uname():
    p = run("uname -a", stdout=Capture())
    return ' '.join(p.stdout.text.split())
