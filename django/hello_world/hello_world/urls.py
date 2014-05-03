from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

from hello import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'violations', views.ViolationViewSet)
router.register(r'addresses', views.AddressViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^search/$', 'hello.views.search_yelp', name='search_yelp'),
    url(r'^searchrestaurant/$', 'hello.views.search_restaurant_name', name='search_restaurant_name'),
    url(r'^init/', 'hello.views.initialize_db', name='initialize_db'),
    url(r'^restaurants/(?P<primary_key>\w+)/$', 'hello.views.get_facility', name='get_facility'),
)

urlpatterns += staticfiles_urlpatterns()
