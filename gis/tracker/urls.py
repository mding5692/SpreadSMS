from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from tracker import views

urlpatterns = patterns('',
                       url(r'^$', views.homepage, name='homepage'),
                       url(r'^sms/$', views.process_sms, name='sms'),
                       url(r'^regions/$', views.region_view, name='regions'),
                       url(r'^send/broadcast/(?P<text>.*)/$', views.process_proximity, name='process'),
                       url(r'^register/$', views.register_view, name='register'),
                       url(r'^register_api/$', views.RegistrationApi.as_view(), name='register_api'),
                       url(r'^send/$', views.proximity_view, name='proximity'),)

urlpatterns = format_suffix_patterns(urlpatterns)