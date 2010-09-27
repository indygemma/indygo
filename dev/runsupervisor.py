#!/usr/bin/env python
import os, sys

# set the parent directory as current
pwd = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, pwd)

from lib.cmd import valid_settings, run_supervisord

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: runsupervisor.py <configuration file>"
		sys.exit(1)
	
	conf = sys.argv[1]
	run_supervisord(conf, *sys.argv[2:])

