from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework import viewsets, routers, serializers
from hello.models import Restaurant, Violation, Address

admin.autodiscover()

router = routers.DefaultRouter()

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ('resource_code', 'activity_date', 'violation_description')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    violations = ViolationSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('facility_name', 'violations')

class ViolationViewSet(viewsets.ModelViewSet):
    model = Violation

class RestaurantViewSet(viewsets.ModelViewSet):
    model = Restaurant
    serializer_class = RestaurantSerializer


router.register(r'restaurants', RestaurantViewSet)
router.register(r'violations', ViolationViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^search$', 'hello.views.search_yelp', name='search_yelp'),
    url(r'^searchrestaurant$', 'hello.views.search_restaurant_name', name='search_restaurant_name'),
    url(r'^init/', 'hello.views.initialize_db', name='initialize_db')
)

urlpatterns += staticfiles_urlpatterns()
