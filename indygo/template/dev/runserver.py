#!virtualenv/bin/python
import os, sys, subprocess

# set the parent directory as current
pwd = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, pwd)

from lib.cmd import valid_settings, perform_syncdb

def is_valid_conf(conf):
	return conf in valid_settings()

def runserver(conf):
	if is_valid_conf(conf):
		perform_syncdb(conf)
		subprocess.call(["python", "manage.py", "runserver", "127.0.0.1:8080", "--settings=settings.%s" % conf])

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: runserver.py <settings.py>"
		print "---- Valid settings:"
		for setting in valid_settings():
			print setting
		sys.exit(1)
	
	conf = sys.argv[1]

	runserver(conf)


