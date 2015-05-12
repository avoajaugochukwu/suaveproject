"""
HTTP status ranges in a nutshell:

1xx: hold on
2xx: here you go
3xx: go away
4xx: you fucked up
5xx: I fucked up
"""




from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^suave/', include('suave.urls', namespace="suave")),
    url(r'^suave/staff/', include('staff.urls', namespace="staff")),
)
