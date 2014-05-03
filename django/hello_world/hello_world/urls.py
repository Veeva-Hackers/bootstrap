from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^search', 'hello.views.search', name='search'),
    url(r'^init/', 'hello.views.initializeDB', name='initializeDB'),
)

urlpatterns += staticfiles_urlpatterns()
