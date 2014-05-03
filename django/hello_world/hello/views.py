from django.shortcuts import render_to_response
from yelpapi.yelpapi import YelpAPI
from django.http import HttpResponse

from hello import models

# Create your views here.
def home(request):
    return render_to_response('index.html', {
        'hello': 'world'
    })


def search(request):
    yelp_api = YelpAPI(consumer_key='blah', consumer_secret='blah', token='blah',
                       token_secret='blah')
    # search_results = yelp_api.search_query('blah')

    # business_results = yelp_api.business_query(id='blah')

    return render_to_response('portfolio.html', {
        'hello': 'world'
    })

def initializeDB(request):
    models.load()
    return HttpResponse("Initialized")
