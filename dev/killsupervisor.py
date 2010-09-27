#!virtualenv/bin/python
import os, subprocess

# assumption: under the project root there is a directory called tmp
# within the directory a supervisord.pid is placed when the daemon is running.
# read that pid and kill off the process using it
pwd = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

try:
	f = open(os.path.join(pwd, "tmp", "supervisord.pid"), "r")
	pid = f.read().strip()
	f.close()
	subprocess.call(["kill", pid])
	print "killed supervisord with pid:", pid
except:
	raise
	print "supervisord not running"

