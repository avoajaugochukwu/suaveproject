"""
HTTP status ranges in a nutshell:

1xx: hold on
2xx: here you go
3xx: go away
4xx: you fucked up
5xx: I fucked up
"""

from django.conf.urls import patterns, include, url
from suave import views

urlpatterns = patterns('',
		##
		#register: found on the homepage links to registration of clients
		#register-->clientRegister


		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.clientRegister, name='clientRegister'),
		url(r'^tailor$', views.tailorHome, name='tailorHome'),
		url(r'^user$', views.clientHome, name='clientHome'),
		url(r'^order/$', views.order, name='order'),
		url(r'^dashboard/$', views.clientDashboard, name='clientDashboard'),
		url(r'^test/$', views.test, name='test'),
)