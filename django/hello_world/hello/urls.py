from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^init/', views.initializeDB, name='initializeDB')
)
