from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

from pages.models import RenderableEvents, ExamReview
from github3 import GitHub
from github3.orgs import Organization

# Create your views here.

def generic(request):
	template = loader.get_template("pages%s.html" % request.path)
	context = RequestContext(request, {
		#Nothing really should go here
	})
	return HttpResponse(template.render(context))

def index(request):
	RenderableEvents.getEvents()
	template = loader.get_template("pages/index.html")
	context = RequestContext(request, {
		'events' : RenderableEvents.events,
	})
	return HttpResponse(template.render(context))
	
def resources(request):
	RenderableEvents.getEvents()
	template = loader.get_template("pages/resources.html")
	context = RequestContext(request, {
		'exams' : ExamReview.objects.all(),
	})
	return HttpResponse(template.render(context))

def projects(request):
	template = "pages/projects.html"
	# Create anonymous (unauthenticated) GitHub session.
	anon = GitHub()
	# Fetch the "rit-csc" organization.
	ourOrg = anon.organization(login="rit-csc")
	# Iterate over all of our repositories and generate the dictionary
	# of info to be passed to the template.
	repos = {}
	for r in ourOrg.iter_repos(type='public'):
		# repos[str(r.name)] = {"description":r.description,"link_to_src":r.html_url}
		repos[str(r.name)] = r.html_url
	return render_to_response(template, {"repos":repos})



# Repository attributes that may be useful at some point:
		# r.readme() -> :class: `Contents <github3.repos.contents.Contents>`
		# r.description -> Description of the repository
		# r.homepage -> URL of the home page for the project (GH-PAGES)
		# r.html_url -> URL of the project at GitHub (SRC CODE)
		# r.language -> language property
		# r.name -> name of the repository (i.e., "github3.py")
		# r.stargazers -> number of users who starred the repository
		# r.watchers -> number of users watching the repository
		# str(r) -> the full name
	