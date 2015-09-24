from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from mainapp.views import *


urlpatterns = patterns('',

	url(r'^$', StartPage),
    url(r'^main/$', MainPage),
    #url(r'^start/$', StartPage),
    url(r'^fetch/$', GetData),
    url(r'^map/$', MapPage),
    url(r'^sample_map.html', MapPage),

    url(r'^admin/', include(admin.site.urls)),
)
