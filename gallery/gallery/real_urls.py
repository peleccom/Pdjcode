from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from django.contrib import admin
urlpatterns =  patterns('',

url(r'^', include('items.urls')),
)