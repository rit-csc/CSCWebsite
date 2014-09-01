from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from pages.models import RenderableEvents

# Create your views here.

def generic(request):
	template = loader.get_template("pages%s" % request.path)
	context = RequestContext(request, {
		#Nothing really should go here
	})
	return HttpResponse(template.render(context))

def index(request):
	RenderableEvents.getEvents()
	template = loader.get_template("pages%s" % request.path)
	context = RequestContext(request, {
		'events' : RenderableEvents.events,
	})
	return HttpResponse(template.render(context))
	