from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def generic(request):
	return HttpResponse("%s" % request.path)
