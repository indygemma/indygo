from django.views.generic.simple import direct_to_template
from django.template import RequestContext

def index(request, **kwargs):
	return direct_to_template(request, "site/index.html", context_instance=RequestContext(request))

