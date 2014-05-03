from django.shortcuts import render_to_response
from django.http import HttpResponse
from yelpapi.yelpapi import YelpAPI
import json
# import oauth2
from rest_framework import viewsets, serializers
from rest_framework.renderers import JSONRenderer

from hello import models
from hello.models import Violation, Restaurant, Address

def home(request):
    return render_to_response('index.html', {
        'hello': 'world'
    })


def search_yelp(request):

# Sign the URL
#     consumer = oauth2.Consumer('iuNELsk9FWsJUHb-LdFx_A', 'THc0I88ppFD45fjK_fGnXEhaGKs')
#     oauth_request = oauth2.Request('GET', 'http://api.yelp.com/v2/search', {})
  # oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
  #                       'oauth_timestamp': oauth2.generate_timestamp(),
  #                       'oauth_token': token,
  #                       'oauth_consumer_key': consumer_key})

    # yelp_api = YelpAPI(consumer_key='iuNELsk9FWsJUHb-LdFx_A',
    #                    consumer_secret='THc0I88ppFD45fjK_fGnXEhaGKs',
    #                    token='jv8hIDODrf8kHAIalsFdgaJKSvo86E0U',
    #                    token_secret='_zQuQVlWTn_tzfnw_uhAWbQJJIs')
    #
    #
    #
    # search_results = yelp_api.search_query(term='ice cream', location='austin, tx', sort=2, limit=25)

    # for business in search_results.businesses:
    #     name = business.name
    #     image_url = business.image_url
    #     url = business.url
    #     ratings = business.ratings
    #     print 'name: ', name

    return render_to_response('portfolio.html', {
        # 'results': search_results
    })


def search_restaurant_name(request):
    q = '1'
    q = q.upper()
    matching_restaurants = models.Restaurant.objects.filter(facility_name__istartswith=q)

    serializer = RestaurantSerializer(matching_restaurants)
    return HttpResponse(JSONRenderer().render(serializer.data))

def initialize_db(request):
    models.load()
    return HttpResponse("Initialized")

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address', 'city', 'state', 'zip')

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ('resource_code', 'activity_date', 'violation_description')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    violations = ViolationSerializer(many=True)
    location_1 = AddressSerializer()

    class Meta:
        model = Restaurant
        fields = ('facility_name', 'human_address', 'violations', 'location_1')

class ViolationViewSet(viewsets.ModelViewSet):
    model = Violation

class AddressViewSet(viewsets.ModelViewSet):
    model = Address

class RestaurantViewSet(viewsets.ModelViewSet):
    model = Restaurant
    serializer_class = RestaurantSerializer


def get_facility(request, primary_key):
    restaurant = models.Restaurant.objects.filter(id=primary_key)
    return render_to_response('portfolio_item.html')
