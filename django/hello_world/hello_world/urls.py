from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^search$', 'hello.views.search_yelp', name='search_yelp'),
    url(r'^searchrestaurant$', 'hello.views.search_restaurant_name', name='search_restaurant_name'),
    url(r'^init/', 'hello.views.initialize_db', name='initialize_db')
)

urlpatterns += staticfiles_urlpatterns()
