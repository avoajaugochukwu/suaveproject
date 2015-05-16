from django.conf.urls import patterns, include, url
from suave import views

urlpatterns = patterns('',
		##
		#register: found on the homepage links to registration of clients
		#register-->clientRegister


		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.client_register, name='client_register'),

		url(r'^createOrder/$', views.createOrder, name='createOrder'),
		url(r'^dashboard/$', views.client_dashboard, name='client_dashboard'),

		url(r'^signin/$', views.signin, name='signin'),
		url(r'^signout/$', views.signout, name='signout'),



		url(r'^tailor/$', views.tailorHome, name='tailorHome'),
		url(r'^tailor/register$', views.tailorRegister, name='tailorRegister'),
		url(r'^tailor/dashboard$', views.tailorDashboard, name="tailorDashboard"),
		# url(r'^tailor/view/order/$', views.tailorOrderDetails, name='tailorOrderDetails'), #(?P<category_name_slug>[\w\-]+)
		url(r'^tailor/view/order/(?P<main_order_id>[\w\-]+)$', views.tailorOrderDetails, name='tailorOrderDetails'),
		url(r'^tailor/view/workinprogress/$', views.tailorWorkInProgress, name="tailorWorkInProgress"),
		url(r'^tailor/start/order/(?P<main_order_id>[\w\-]+)$', views.tailorStartOrder, name="tailorStartOrder"),



		url(r'^not/logged/in$', views.notLoggedIn, name='notLoggedIn'),

)