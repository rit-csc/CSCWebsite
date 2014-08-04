from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

from pages import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# http://stackoverflow.com/questions/15491727/include-css-and-javascript-in-my-django-template

urlpatterns = patterns('',
    # Examples:
    url(r'^$', RedirectView.as_view(url='index.html', permanent=False)),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^helloWorld', include(admin.site.urls)),
	
	#Custom stuff GOES HERE
	
	url(r'^.*$', views.generic),
	#Custom stuff DOES NOT GO HERE
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
