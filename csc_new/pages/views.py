from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

import requests

from pages.models import *
from csc_new import settings

# Create your views here.

def generic(request):
	template = loader.get_template("pages%s.html" % request.path)
	context = RequestContext(request, {
		'MEDIA_URL':settings.MEDIA_URL,
		'img_list':Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def index(request):
	re = RenderableEvents()
	re.getEvents()
	template = loader.get_template("pages/index.html")
	context = RequestContext(request, {
		'events' : re.events,
		'MEDIA_URL':settings.MEDIA_URL,
		'img_list':Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))
	
def resources(request):
	template = loader.get_template("pages/resources.html")
	context = RequestContext(request, {
		'exams' : ExamReview.objects.all(),
		'MEDIA_URL':settings.MEDIA_URL,
		'img_list':Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def pictures(request):
	template = loader.get_template("pages/pictures.html")
	context = RequestContext(request, {
		'pics' : Photo.objects.all(),
		'MEDIA_URL':settings.MEDIA_URL,
		'img_list':Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def projects(request):
	template = "pages/projects.html"

	try:
		api_url = "https://api.github.com/orgs/rit-csc/repos"
		r = requests.get(api_url)

		# # Response will have the following structure:
		# [
		# 	{
		# 		"name": 		{{name_of_repo}},
		# 		"full_name":	"rit-csc/"{{name_of_repo}},
		# 		"private":		true/false,
		# 		"html_url":		"https://github.com/rit-csc/"{{name_of_repo}},
		# 		"description":	{{description}},
		# 		"fork":			true/false,
		# 		"updated_at":	{{updated_at}},		# format: 2015-01-01T12:12:12Z
		# 		"stargazers_count":	{{num_stargazers}},
		# 		"watchers_count":	{{num_watchers}},
		# 		"language":		{{language}},
		# 		"has_issues":	true/false,
		# 		"has_pages":	true/false,
		# 		"open_issues_count":	{{open_issues_count}},
		# 		...
		# 	},
		# 	...
		# ]

		# Sort repos by last_updated, with the most recently-updated repos first.
		repos = sorted(r.json(), key=lambda repo: repo['updated_at'], reverse=True)

		return render_to_response(template, {"success":True, "repos":repos,
												'MEDIA_URL':settings.MEDIA_URL,
												'img_list':Photo.objects.values_list('src', flat=True)})
	
	except:
		return render_to_response(template, {"success":False,
												'MEDIA_URL':settings.MEDIA_URL,
												'img_list':Photo.objects.values_list('src', flat=True)})
