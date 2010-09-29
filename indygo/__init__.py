from paste.script import templates
import pkg_resources

class IndyGoTemplate(templates.Template):
	egg_plugins = ["IndyGoTemplate"]
	_template_dir = pkg_resources.resource_filename("indygo", "template")
	 summary = "A pastescript template for a complete django project with pip+virtualenv, fabric, a gevent-based wsgi server and various helpers scripts. Ready to deploy on your production server in minutes."
	required_templates = []

