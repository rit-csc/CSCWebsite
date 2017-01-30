from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

import urllib
import json

from pages.models import *
from csc_new import settings

from .forms import SignInForm

# Create your views here.

def generic(request):
    
    request_path_string = str(request.path)
    if request_path_string[-1] == "/":
        # a trailing slash in a URL can cause issues with
        # resolving the URL, especially for templates.
        # If there is a trailing slash, we remove it here.
        request_path_string = request_path_string[0:-1]

    template = loader.get_template("pages%s.html" % request_path_string)
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
        'events':re.events,
        'MEDIA_URL':settings.MEDIA_URL,
        'img_list':Photo.objects.values_list('src', flat=True),
    })
    return HttpResponse(template.render(context))


def resources(request):
    template = loader.get_template("pages/resources.html")
    context = RequestContext(request, {
        'exams': ExamReview.objects.all().order_by("last_modified").reverse(),
        'MEDIA_URL': settings.MEDIA_URL,
        'img_list': Photo.objects.values_list('src', flat=True),
        'slides': GeneralMeetingSlides.objects.all(),
    })
    return HttpResponse(template.render(context))


def pictures(request):
    template = loader.get_template("pages/pictures.html")
    context = RequestContext(request, {
        'pics':Photo.objects.all(),
        'MEDIA_URL':settings.MEDIA_URL,
        'img_list':Photo.objects.values_list('src', flat=True),
    })
    return HttpResponse(template.render(context))


def projects(request):
    template = "pages/projects.html"

    try:
        api_url = "https://api.github.com/orgs/rit-csc/repos"
        # get the http response
        httpresponse = urllib.request.urlopen(api_url)
        # read the data
        data = httpresponse.read().decode("utf-8")
        # close the connection
        httpresponse.close()

        # convert the data to a json object
        data_as_json = json.loads(data)

        # Sort repos by last_updated, with the most recently-updated repos first.
        repos = sorted(data_as_json, key=lambda repo:repo['updated_at'], reverse=True)

        return render_to_response(template, {"success":True, "repos":repos,
                                                'MEDIA_URL':settings.MEDIA_URL,
                                                'img_list':Photo.objects.values_list('src', flat=True)})
    except:
        return render_to_response(template, {"success":False,
                                                'MEDIA_URL':settings.MEDIA_URL,
                                                'img_list':Photo.objects.values_list('src', flat=True)})

def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        
        if form.is_valid():
            
            if form.cleaned_data['mailinglist'] == 'yes':
                email_addr = form.cleaned_data['email']
                #add to mailman
                os.system("echo \"%s\" | /usr/lib/mailman/bin/add_members -r - announcements" % email_addr)

            return HttpResponseRedirect('/thanks');

    else:
        form = SignInForm()

    return render(request, 'pages/signup.html', {
        'form':form,
        'MEDIA_URL':settings.MEDIA_URL,
        'img_list':Photo.objects.values_list('src', flat=True)
    })

