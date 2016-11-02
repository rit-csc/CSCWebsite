from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from pages import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# http://stackoverflow.com/questions/15491727/include-css-and-javascript-in-my-django-template

urlpatterns = [
    # Examples:
	url(r'^$', views.index),
    url(r'^admin', include(admin.site.urls)),
	
	# Custom stuff GOES HERE
	url(r'^member/?', include('member.urls')),
    # Note that "/?" at the end means a trailing
    # slash at the end of the URL can be included
    # but is not required.
	url(r'^resources/?$', views.resources),
	url(r'^pictures/?$', views.pictures),
	url(r'^projects/?$', views.projects),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += [url(r'^.*', views.generic)]
