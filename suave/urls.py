from django.conf.urls import patterns, include, url
from suave import views
from django.conf import settings



urlpatterns = patterns('',
		##
		#register: found on the homepage links to registration of clients
		#register-->clientRegister


		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.client_register, name='client_register'),

		url(r'^createOrder/$', views.create_order, name='create_order'),
		url(r'^dashboard/$', views.client_dashboard, name='client_dashboard'),

		url(r'^signin/$', views.signin, name='signin'),
		url(r'^signout/$', views.signout, name='signout'),



		url(r'^tailor/$', views.tailor_home, name='tailor_home'),
		url(r'^tailor/register$', views.tailor_register, name='tailor_register'),
		url(r'^tailor/dashboard$', views.tailor_dashboard, name="tailor_dashboard"),

		url(r'^tailor/view/order/(?P<main_order_id>[\w\-]+)$', views.tailor_order_details, name='tailor_order_details'),
		url(r'^tailor/view/workInProgress/$', views.tailor_work_in_progress, name="tailor_work_in_progress"),
		url(r'^tailor/start/order/(?P<main_order_id>[\w\-]+)$', views.tailor_start_order, name="tailor_start_order"),



		url(r'^not/logged/in$', views.login_failed, name='login_failed'),

)