from paste.script import templates
import pkg_resources

class IndyGoTemplate(templates.Template):
	egg_plugins = ["IndyGoTemplate"]
	_template_dir = pkg_resources.resource_filename("indygo", "template")
	summary = "Complete Django Development Environment with pip+virtualenv, ready for deployment"
	required_templates = []

