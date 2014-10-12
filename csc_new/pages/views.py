from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

from pages.models import *
from csc_new import settings

# Create your views here.

def generic(request):
	template = loader.get_template("pages%s.html" % request.path)
	context = RequestContext(request, {
		'MEDIA_URL' : settings.MEDIA_URL,
		'img_list' : Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def index(request):
	re = RenderableEvents()
	re.getEvents()
	template = loader.get_template("pages/index.html")
	context = RequestContext(request, {
		'events' : re.events,
		'MEDIA_URL' : settings.MEDIA_URL,
		'img_list' : Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))
	
def resources(request):
	template = loader.get_template("pages/resources.html")
	context = RequestContext(request, {
		'exams' : ExamReview.objects.all(),
		'MEDIA_URL' : settings.MEDIA_URL,
		'img_list' : Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def pictures(request):
	template = loader.get_template("pages/pictures.html")
	context = RequestContext(request, {
		'pics' : Photo.objects.all(),
		'MEDIA_URL' : settings.MEDIA_URL,
		'img_list' : Photo.objects.values_list('src', flat=True),
	})
	return HttpResponse(template.render(context))

def projects(request):
	template = "pages/projects.html"
	repos = {
				"csc_exam_reviews":{
					"name":"csc_exam_reviews",
					"description":"A collection of practice exams for exams in core curriculum CS courses at RIT.",
					"language":"TeX",
					"misc_info":"The source files for our department-sponsored exam review sessions, currently including content for all CS1, CS2, and Mechanics of Programming exams."
				},
				"git_instructions":{
					"name":"git_instructions",
					"description":"An introductory tutorial for setting up and using a Git repository, developed for the CS department by the CSC.",
					"language":"HTML, CSS",
					"misc_info":"Our work-in-progress tutorial to help RIT's CS department incorporate Git as the primary type of version control in the introductory course curriculum."
				},
				"sensorship":{
					"name":"sensorship",
					"description":"A simple Pong desktop game that utilizes the accelerometer data from connected Android devices.",
					"language":"Java",
					"misc_info":"This project was a hack for Yale University's Yhack 2013."
				},
				"MorseCode":{
					"name":"MorseCode",
					"description":"An Android app developed by Mike Lyman and Doug Krofcheck that makes discrete Morse Code texting available to the masses.",
					"language":"Java",
					"misc_info":"This project was a hack for Yale University's Yhack 2013."
				},
				"CSC-Plays-Pokemon":{
					"name":"CSC-Plays-Pokemon",
					"description":"A program to accompany Eric Falkenberg's workshop on the technical side of \"Twitch Plays Pokémon\".",
					"language":"C++",
					"misc_info":""
				},
			}

	return render_to_response(template, {"success":True, "repos":repos, 'MEDIA_URL' : settings.MEDIA_URL, 'img_list' : Photo.objects.values_list('src', flat=True)})
	
