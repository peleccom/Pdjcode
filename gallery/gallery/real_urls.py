from django.conf.urls.defaults import *
form django.contrib import admin
urlpatterns =  patterns('',

url(r'^', include('items.urls')),
)