from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns(
	'',
	# The index page is the main splash for the application.
	url(r'^$', views, name='index'),
	url(r'^.*/$', views.generic, name='generic')
)
urlpatterns += staticfiles_urlpatterns()
