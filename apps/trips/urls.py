from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'travels$', views.travels),
    url(r'create$', views.create),
    url(r'logout$', views.logout),
    url(r'trips/create$', views.create),
    url(r'trips/(?P<trips_id>\d+)/create$', views.create),
    url(r'trips/(?P<trips_id>\d+)/travels$', views.travels),
]