from django.conf.urls import *
from models import Update
from django.views.generic import ListView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Update.objects.all())),
    url(r'^updates-after/(?P<id>\d+)/$', 'liveupdate.views.updates_after'),
)