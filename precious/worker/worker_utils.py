#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from urllib2 import urlopen
from sarge import run, Capture, shell_format, default_capture_timeout,\
    capture_both


default_capture_timeout = 0.1


def get_ip_addr():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    socket_name = s.getsockname()[0]
    s.close()
    return socket_name


def get_public_ip_addr():
    return json.load(urlopen('http://wtfismyip.com/json'))['YourFuckingIPAddress']


def get_public_hostname():
    return json.load(urlopen('http://wtfismyip.com/json'))['YourFuckingHostname']


def get_uname():
    p = run("uname -a", stdout=Capture())
    return ' '.join(p.stdout.text.split())


def get_free_ram():
    p = run("free -m", stdout=Capture())
    return p.stdout.text.split("\n")


def get_free_space(location):
    p = run(shell_format('du -hs {0}', location), stdout=Capture())
    return p.stdout.text.split()[0]


def run_command(cmd, input=None, async=False, **kwargs):
    timeout = kwargs.pop('timeout', None)
    ts = time.time()
    p = capture_both(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode,
            "stdout": p.stdout.text.split("\n"),
            "stderr": p.stderr.text.split("\n"),
            "tstart": ts,
            "tstop": time.time()}


def run_command_raw_output(cmd, input=None, async=False, **kwargs):
    timeout = kwargs.pop('timeout', None)
    ts = time.time()
    p = capture_both(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode,
            "stdout": p.stdout.text,
            "stderr": p.stderr.text,
            "tstart": ts,
            "tstop": time.time()}


def run_command_forget_output(cmd, input=None, async=False, **kwargs):
    ts = time.time()
    p = run(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode, "output": "",
            "tstart": ts,
            "tstop": time.time()}
