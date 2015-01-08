# This file holds custom filters for Django

from django import template, forms
from django.core.urlresolvers import reverse
import datetime
from pages.models import *

register = template.Library()

@register.inclusion_tag('pages/inclusionTemplates/repoInfo.html')
def repoInfo(repo):
	return repo

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_value_at_index(lst, index):
    return lst[index]
