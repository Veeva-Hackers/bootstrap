from django.shortcuts import render, render_to_response
from hello import models

# Create your views here.
def home(request):
    models.parseFromFlatFile()
    return render_to_response('index.html', {
        'girum': 'ibssa'
    })

def search(request):
    return None
