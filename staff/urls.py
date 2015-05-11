from django.conf.urls import patterns, include, url
from staff import views

urlpatterns = patterns('',
		##
		#Staff module


		url(r'^$', views.index, name='index'),


)