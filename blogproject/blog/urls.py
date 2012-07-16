from django.conf.urls.defaults import *
from blog.views import archive
from blog.feeds import RSSFeed

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^feeds/$', RSSFeed()),
)
