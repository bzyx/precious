import sys
import subprocess

procs = []
runserver = subprocess.Popen([sys.executable, "runserver.py"])
runsheduler = subprocess.Popen([sys.executable, "runsheduler.py"])
runworker = subprocess.Popen([sys.executable, "runworker.py"])
procs.append(runserver)
procs.append(runsheduler)
procs.append(runworker)

for proc in procs:
    proc.wait()
