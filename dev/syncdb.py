#!virtualenv/bin/python
import os, subprocess, sys

pwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(pwd)
sys.path.insert(0, pwd)
from lib import cmd
from lib.cmd import valid_settings

def check_settings_exists(s):
	if s in valid_settings():
		return True
	print "settings.%s does not exist." % s
	for setting in valid_settings():
		print setting
	return False

def perform_syncdb(settings):
	if check_settings_exists(settings):
		cmd.perform_syncdb(settings)

if __name__ == '__main__':
	if not len(sys.argv) >= 2:
		print "Usage: syncdb <settings.py>"
		print "---- Valid settings:"
		for setting in valid_settings():
			print setting
		sys.exit(-1)
	
	settings = sys.argv[1]
	print "Using settings:", settings

	perform_syncdb(settings)

