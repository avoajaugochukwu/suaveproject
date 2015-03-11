from django.conf.urls import patterns, include, url
from suave import views

urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'SuaveProject.views.home', name='home'),
		# url(r'^blog/', include('blog.urls')),

		url(r'^$', views.index, name='index'),
		url(r'^signup$', views.signUp, name='signUp'),
		url(r'^tailor$', views.tailorHome, name='tailorHome'),
		url(r'^user$', views.clientHome, name='clientHome'),
)