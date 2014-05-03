from django.shortcuts import render_to_response
from django.http import HttpResponse
from yelpapi.yelpapi import YelpAPI
import json

from hello import models


def home(request):
    return render_to_response('index.html', {
        'hello': 'world'
    })


def search_yelp(request):
    yelp_api = YelpAPI(consumer_key='iuNELsk9FWsJUHb-LdFx_A', consumer_secret='THc0I88ppFD45fjK_fGnXEhaGKs', token='jv8hIDODrf8kHAIalsFdgaJKSvo86E0U',
                       token_secret='_zQuQVlWTn_tzfnw_uhAWbQJJIs')
    search_results = yelp_api.search_query(radius_filter='5', term = 'restaurants', limit = 25)

    for business in search_results.businesses:
        name =  business.name
        image_url = business.image_url
        url = business.url
        ratings = business.ratings
        print 'name: ' , name

    return render_to_response('portfolio.html', {
        'results': search_results
    })

def search_restaurant_name(request):
    matching_restaurants = models.Restaurant.objects.all()
    output = json.dumps(matching_restaurants)
    return HttpResponse(output)

def initialize_db(request):
    models.load()
    return HttpResponse("Initialized")
