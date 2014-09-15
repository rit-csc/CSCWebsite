from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

from pages.models import RenderableEvents, ExamReview

# Create your views here.

def generic(request):
	template = loader.get_template("pages%s.html" % request.path)
	context = RequestContext(request, {
		#Nothing really should go here
	})
	return HttpResponse(template.render(context))

def index(request):
	re = RenderableEvents()
	re.getEvents()
	template = loader.get_template("pages/index.html")
	context = RequestContext(request, {
		'events' : re.events,
	})
	return HttpResponse(template.render(context))
	
def resources(request):
	template = loader.get_template("pages/resources.html")
	context = RequestContext(request, {
		'exams' : ExamReview.objects.all(),
	})
	return HttpResponse(template.render(context))

def projects(request):
	template = "pages/projects.html"
	repos = {
				"csc_exam_reviews":{
					"name":"csc_exam_reviews",
					"description":"bleh",
					"language":"TeX",
					"misc_info":"Misc info!"
				},
				"git_instructions":{
					"name":"git_instructions",
					"description":"bleh",
					"language":"Html, CSS",
					"misc_info":"Misc info!"
				},
				"sensorship":{
					"name":"sensorship",
					"description":"A simple Pong desktop game that utilizes the accelerometer data from connected Android devices.",
					"language":"Java",
					"misc_info":"Misc info!"
				},
				"MorseCode":{
					"name":"MorseCode",
					"description":"bleh",
					"language":"Java",
					"misc_info":"Misc info!"
				},
				"CSC-Plays-Pokemon":{
					"name":"CSC-Plays-Pokemon",
					"description":"bleh",
					"language":"C++",
					"misc_info":"Misc info!"
				},
			}

	return render_to_response(template, {"success":True, "repos":repos})
	