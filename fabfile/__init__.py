from fabric.api import *
import os

USER = "root"
env.hosts = ["%s@65.49.73.73" % USER]
PROJECT_NAME = "sample"
REPO_DIR  = os.path.join("/home", USER, "repos")
REPO_PATH = os.path.join(REPO_DIR, "%s.git" % PROJECT_NAME)
SITE_DIR  = os.path.join("/home", USER, "sites")
SITE_PATH = os.path.join(SITE_DIR, PROJECT_NAME)

def host_type():
	run("uname -s")

### these install actions should be stored in a setup script under bootstrap
def install_nginx():
	run("apt-get install nginx")

def install_libevent():
	""" http://www.monkey.org/~provos/libevent-1.4.14b-stable.tar.gz """
	# ./configure --prefix=/usr
	# make
	# make install
	# ldconfig
	# TODO: on servers without root access I'll have to statically compile gevent
	# run("apt-get install libevent-dev")

def setup_repo():
	""" create an empty git repo on the server and push the local git repo to that """
	giturl = "%(user)s@%(host)s:%(REPO_PATH)s" % {"user":env.user, "host":env.host, "REPO_PATH": REPO_PATH}
	run("mkdir -p %s" % REPO_PATH)
	with cd(REPO_PATH):
		run("git init --bare")
	local("git remote add production %(giturl)s" % locals())
	local("git push production master")
	
def remove_repo():
	""" remove the remote repo and the local reference to that repo """
	local("git remote rm production")
	run("rm -rf %s" % REPO_PATH)

def setup_site():
	run("mkdir -p %s" % SITE_DIR)
	with cd(SITE_DIR):
		run("git clone %s" % REPO_PATH)

def remove_site():
	run("rm -rf %s" % SITE_PATH)

def clean():
	""" remove git repo and site directory """
	remove_repo()
	remove_site()

def bootstrap():
	""" setup the whole site environment """
	setup_repo()
	setup_site()
	with cd(SITE_PATH):
		run("./bootstrap/bootstrap.py") # requires install_libevent for gevent

def run_pip_freeze():
	with cd(os.path.join(SITE_PATH, "virtualenv", "bin")):
		run("./pip freeze")

def run_wsgi():
	with cd(SITE_PATH):
		run("./dev/runwsgi.py production")

def restart_server():
	with settings(warn_only=True):
		result = run("pkill %s" % PROJECT_NAME) # all wsgi servers run as this. set in dev/runwsgi.py via setproctitle
	if result.failed:
		print "There's no server running. Ignoring kill request"

def run_supervisor():
	with cd(SITE_PATH):
		run("./dev/runsupervisor.py production")

def kill_supervisor():
	with cd(SITE_PATH):
		run("./dev/killsupervisor.py")

stop = kill_supervisor # alias for kill_supervisor

def enable_nginx(): # requires install_nginx
	with cd(SITE_PATH):
		run("./etc/nginx/enable.py production")
		run("/etc/init.d/nginx restart")

def push():
	local("git push production")
	with cd(SITE_PATH):
		run("git pull")

def deploy():
	push()
	run_supervisor()
	restart_server()

