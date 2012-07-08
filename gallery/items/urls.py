from django.conf.urls.defaults import *
from models import Item,Photo
from django.views import generic
from views import PhotoDetailView

urlpatterns = patterns('django.views.generic',
url(r'^$','simple.direct_to_template',
        kwargs = {
                  'template': 'index.html',
                  'extra_context' : {'item_list':Item.objects.all}
                  },
        name='index'),
url(r'^items/$',generic.ListView.as_view(
            queryset = Item.objects.all(),
            template_name = 'items_list.html',
            allow_empty=True),
     name ='item_list'),
                       
url(r'^items/(?P<pk>\d+)/$', generic.detail.DetailView.as_view(
        queryset = Item.objects.all(),
        template_name = 'items_detail.html',
        slug_url_kwarg = 'object_id',
                                                                      ) ,
     name= 'item_detail'
     ),
url(r'^photos/(?P<pk>\d+)/$', PhotoDetailView.as_view(
                template_name = 'photos_detail.html'
                                                             ),
    name = 'photo_detail'
    ),


) 