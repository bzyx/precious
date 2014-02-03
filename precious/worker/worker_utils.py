#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sarge import run, Capture, shell_format


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


def get_free_ram():
    p = run("free -m", stdout=Capture())
    return p.stdout.text.split("\n")[1]


def get_free_space(location):
    p = run(shell_format('du -hs {0}', location), stdout=Capture())
    return p.stdout.text.split("\n")[0]


def run_command(cmd, input=None, async=False, **kwargs):
    kwargs['stdout'] = Capture()
    p = run(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode,
            "output": p.stdout.text.split("\n")}


def run_command_raw_output(cmd, input=None, async=False, **kwargs):
    kwargs['stdout'] = Capture()
    p = run(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode,
            "output": p.stdout.text}


def run_command_forget_output(cmd, input=None, async=False, **kwargs):
    p = run(cmd, input=input, async=async, **kwargs)
    return {"command": cmd,
            "returncode": p.returncode, "output": ""}
