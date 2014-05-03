from django.shortcuts import render, render_to_response
from hello import models

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render_to_response('index.html', {
        'girum': 'ibssa'
    })

def search(request):
    return None

def initializeDB(request):
    models.load()
    return HttpResponse("Initialized")
