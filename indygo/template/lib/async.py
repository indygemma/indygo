import os
import gevent

PWD = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def changemonitor(callback):
	monitored_endings = ["py"]
	exclude_dirs = [
		"bootstrap", "cache", "compass",
		"dev", "etc", "fabfile", "fixtures",
		"media", "templates", "tmp", "virtualenv",
		".git", ".svn", ".hg"
	]
	timestamps = {} # filename -> last modified timestamp
	while True:
		for dirpath, dirnames, filenames in os.walk("."):
			# dirpath starts with . eg "./bootstrap"
			try:
				realdirpath = dirpath.split(os.path.sep)[1]
			except:
				continue
			if realdirpath in exclude_dirs:
				continue
			for filename in filenames:
				# we're only interested in those files that have specific endings
				if any(filename.endswith(x) for x in monitored_endings):
					filepath = os.path.join(dirpath, filename)
					modtime = os.stat(filepath).st_mtime
					timestamps.setdefault(filepath, modtime)
					if timestamps[filepath] != modtime:
						# the file has changed. set the current time and call the callback
						print "change detected:", filepath
						timestamps[filepath] = modtime
						callback()
		# sleep for a second and let other greenthreads run their course
		gevent.sleep(1)

