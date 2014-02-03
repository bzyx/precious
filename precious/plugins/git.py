# -*- coding: utf-8 -*-

from base import VCS
import subprocess
import shlex


class Git(VCS):
    def __init__(self, work_dir):
        self.work_dir = work_dir

    def BuildStepArgs(self):
        return {'repo': 'text', 'branch': 'text'}

    def BuildStepDescription(self):
        return ('Git plugin', {'repo': 'Remote repository url', 'branch': 'Selected branch'})

    def BuildStep(self, repo, branch='HEAD'):
        command_line = "git clone -v --depth 1 --branch {0} {1} {2}".format(branch, repo, self.work_dir)
        p = subprocess.Popen(shlex.split(command_line), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        return (p.returncode, p.stdout.read())

    def GetRevision(self, repo, branch='HEAD'):
        command_line = "git ls-remote {1} {0}".format(branch, repo)
        p = subprocess.Popen(shlex.split(command_line), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output,_ = p.communicate()
        return (p.returncode, output.split()[0])
