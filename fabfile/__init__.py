from fabric.api import *

env.hosts = ["root@65.49.73.73"]

def host_type():
	print local("uname -s")

def setup_git():
	""" create an empty git repo on the server and push the local git repo to that """
	run("mkdir -p repos/sample.git")
	local("git push")

def setup():
	pass


