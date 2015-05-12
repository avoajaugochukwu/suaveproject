from django.conf.urls import patterns, include, url
from staff import views

urlpatterns = patterns('',
		##
		#Staff module


		url(r'^$', views.index, name='index'),


		url(r'^signin/$', views.signin, name='signin'),
		url(r'^adminGateWay/$', views.admin_gateway, name='admin_gateway'),

		url(r'^Order/List$', views.order_list, name="order_list"),
		url(r'^Order/Details/(?P<order_id>[\w\-]+)$', views.order_details, name='order_details'),

		url(r'^Order/(?P<order_id>[\w\-]+)/Edit$', views.order_edit, name='order_edit'),

		url(r'^Tailor/List$', views.tailor_list, name="tailor_list"),

)