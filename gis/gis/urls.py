from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', lambda r: HttpResponseRedirect('tracker/proximity')),
    url(r'^tracker/', include('tracker.urls', namespace="tracker")),
    url(r'^admin/', include(admin.site.urls)),
)
