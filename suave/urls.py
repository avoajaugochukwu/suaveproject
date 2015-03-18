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
		url(r'^user$', views.clientHome, name='clientHome'),
		url(r'^createOrder/$', views.createOrder, name='createOrder'),
		url(r'^dashboard/$', views.clientDashboard, name='clientDashboard'),
		url(r'^test/$', views.test, name='test'),
		url(r'^signin/$', views.signin, name='signin'),
		url(r'^signout/$', views.signout, name='signout'),



		url(r'^tailor/$', views.tailorHome, name='tailorHome'),
		url(r'^tailor/register$', views.tailorRegister, name='tailorRegister'),
)