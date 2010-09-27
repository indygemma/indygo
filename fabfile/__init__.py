from fabric.api import *

env.hosts = ["root@65.49.73.73"]

def host_type():
	run("uname -s")

### these install actions should be stored in a setup script under bootstrap
def install_nginx():
	run("apt-get install nginx")

def install_libevent():
	""" http://www.monkey.org/~provos/libevent-1.4.14b-stable.tar.gz """
	# ./configure
	# make
	# make install
	# run("apt-get install libevent-dev")

def setup_git():
	""" create an empty git repo on the server and push the local git repo to that """
	giturl = "%(user)s@%(host)s:~/repos/sample.git" % env
	run("mkdir -p repos/sample.git")
	with cd("repos/sample.git"):
		run("git init --bare")
	local("git remote add production %(giturl)s" % locals())
	local("git push production master")
	
def remove_git():
	""" remove the remote repo and the local reference to that repo """
	local("git remote rm production")
	run("rm -rf repos/sample.git")

def setup_site():
	run("mkdir -p sites")
	with cd("sites"):
		run("git clone ~/repos/sample.git")

def remove_site():
	run("rm -rf sites/sample")

def bootstrap():
	""" setup the whole site environment """
	with cd("sites/sample"):
		run("./bootstrap/bootstrap.py") # requires install_libevent for gevent

def enable_nginx(): # requires install_nginx
	with cd("sites/sample"):
		run("./etc/nginx/enable.py production")
		run("/etc/init.d/nginx restart")

def push():
	local("git push production")
	with cd("sites/sample"):
		run("git pull")
