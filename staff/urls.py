from django.conf.urls import patterns, include, url
from staff import views

urlpatterns = patterns('',
		##
		#Staff module


		url(r'^$', views.index, name='index'),


		url(r'^signin/$', views.signin, name='signin'),
		url(r'^adminGateWay/$', views.admin_gateway, name='admin_gateway'),

		url(r'^Order/List$', views.order_list, name="order_list"),
		url(r'^Order/List/Deleted$', views.order_list_deleted, name="order_list_deleted"),
		url(r'^Order/Details/(?P<order_id>[\w\-]+)$', views.order_details, name='order_details'),
		url(r'^Order/(?P<order_id>[\w\-]+)/Edit$', views.order_edit, name='order_edit'),
		url(r'^Order/(?P<order_id>[\w\-]+)/Delete$', views.order_delete, name='order_delete'),



		url(r'^Tailor/List$', views.tailor_list, name="tailor_list"),
		url(r'^Tailor/Details/(?P<tailor_id>[\w\-]+)$', views.tailor_details, name='tailor_details'),
		url(r'^Tailor/Approve/(?P<tailor_id>[\w\-]+)$', views.tailor_approve, name='tailor_approve'),
		url(r'^Tailor/Reject/(?P<tailor_id>[\w\-]+)$', views.tailor_reject, name='tailor_reject'),



		url(r'^Style/$', views.style_home, name="style_home"),
		url(r'^Style/style_add_form/$', views.style_add_form, name="style_add_form"),
)