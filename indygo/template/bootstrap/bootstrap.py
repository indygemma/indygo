#!/usr/bin/env python
import os, sys, subprocess, shutil

pwd = os.path.dirname(__file__)
dependencies_file = os.path.join(pwd, "dependencies.txt")
virtualenv_dir = os.path.join(pwd, "..", "virtualenv")

#if os.path.exists(virtualenv_dir):
#	shutil.rmtree(virtualenv_dir)

subprocess.call(["pip", "install", "-E", virtualenv_dir,
								   "-r", dependencies_file])
