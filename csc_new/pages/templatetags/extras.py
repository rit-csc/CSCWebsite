# This file holds custom filters for Django

from django import template, forms
from django.core.urlresolvers import reverse
import datetime
from pages.models import *

register = template.Library()





# Repository attributes that may be useful at some point:
		# r.readme() -> :class: `Contents <github3.repos.contents.Contents>`
	#	# r.description -> Description of the repository
		# r.homepage -> URL of the home page for the project (GH-PAGES)
	#	# r.html_url -> URL of the project at GitHub (SRC CODE)
	#	# r.language -> language property
	#	# r.name -> name of the repository (i.e., "github3.py")
	#	# r.stargazers -> number of users who starred the repository
	#	# r.watchers -> number of users watching the repository
	#	# str(r) -> the full name
@register.inclusion_tag('pages/inclusionTemplates/repoInfo.html')
def repoInfo(repo):
	return {"name":repo.name,
			"fullname":str(repo),
			"html_url":repo.html_url,
			"description":repo.description,
			"readme":repo.readme,
			"language":repo.language,
			"stargazers":repo.stargazers,
			"watchers":repo.watchers}

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_value_at_index(lst, index):
    return lst[index]
