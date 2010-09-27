"""
This is a signal handler that is only called when DEBUG=True.
Here we create a default superuser with

	admin/1234

and a localhost site with the appropriate attributes.
"""
from django.db import models
from django.conf import settings

if settings.DEBUG:
	from django.db.models import signals
	from django.contrib.auth.models import User
	from django.contrib.sites.models import Site
	def create_new_user(sender, **kwargs):
		try:
			admin = User.objects.get(username="admin")
		except:
			print "---- Creating superuser: username=admin, password=1234. Set settings.DEBUG = False to disable this feature ---"
			user = User.objects.create_user("admin", "admin@home.com", "1234")
			user.is_staff = True
			user.is_superuser = True
			user.save()
		try:
			current_site = Site.objects.get_current()
		except:
			localhost = settings.LOCALHOST if not settings.LOCALHOST.startswith("http://") else settings.LOCALHOST.replace("http://", "")
			print "---- Creating current site: domain=%s, name=Localhost. Set settings.DEBUG = False to disable this feature ---" % settings.LOCALHOST
			current_site = Site.objects.create(domain=localhost, name="Localhost")
	signals.post_syncdb.connect(create_new_user)
