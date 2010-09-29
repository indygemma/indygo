#!/usr/bin/env python
import os, subprocess, sys, shutil

def set_permissions(project_dir):
	""" set permissions to 755 for selected scripts """
	files_to_change = [
		("bootstrap", "bootstrap.py"),
		("bootstrap", "setup_pip_virtualenv.py"),
		("bootstrap", "setup_ubuntu_packages.sh"),
		("dev", "killsupervisor.py"),
		("dev", "runserver.py"),
		("dev", "runsupervisor.py"),
		("dev", "runwsgi.py"),
		("dev", "syncdb.py"),
		("etc", "nginx", "enable.py"),
		("manage.py",),
	]
	for filepath in files_to_change:
		fullpath = os.path.join(project_dir, *filepath)
		print "changing permissions to 755 for", fullpath
		subprocess.call(["chmod", "755", "%s" % fullpath])
	

def rename_dotfiles(project_dir):
	""" rename dotfiles, namely gitignore -> .gitignore """
	print "adding .gitignore"
	shutil.move(
			os.path.join(project_dir, "gitignore"),
			os.path.join(project_dir, ".gitignore")
	)

def call_paster():
	if len(sys.argv) < 2:
		print "Usage: indygo <projectname>"
		sys.exit(0)
	name = sys.argv[1]
	pwd = os.path.abspath(os.path.dirname(name))
	project_dir = os.path.join(pwd, name)
	subprocess.call(["paster", "create", "--template=indygo", name])
	set_permissions(project_dir)
	rename_dotfiles(project_dir)

