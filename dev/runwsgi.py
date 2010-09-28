#!virtualenv/bin/python
from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer
import sys
import os
import traceback
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import call_command
from django.core.signals import got_request_exception
import gevent
import setproctitle

# add the project root to the sys.path so we can find settings
pwd = os.path.join(os.path.dirname(__file__), "..")
os.chdir(pwd)
sys.path.insert(0, os.getcwd())

from lib.cmd import valid_settings, perform_syncdb

VALID_SETTINGS = valid_settings()

if len(sys.argv) < 2:
	print "Usage: runwsgi.py <settings.py>"
	print "---- Valid settings:"
	for setting in VALID_SETTINGS:
		print setting
	sys.exit(1)

settings = sys.argv[1]

if not settings in VALID_SETTINGS:
	print "Invalid settings file: %s" % settings
	print "---- Valid settings:"
	for setting in VALID_SETTINGS:
		print setting
	sys.exit(1)

# set the process name to something meaningful
setproctitle.setproctitle("sample")

# insert right django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.%s' % settings

# make sure our db is sync'd before we go on
perform_syncdb(settings)

def exception_printer(sender, **kwargs):
    traceback.print_exc()

got_request_exception.connect(exception_printer)

#call_command('syncdb')
print 'gevent wsgi server is running on 8080 with settings: %s' % settings
server = WSGIServer(('127.0.0.1', 8080), WSGIHandler())
server.start()

while True:
	gevent.sleep(0.0001)

