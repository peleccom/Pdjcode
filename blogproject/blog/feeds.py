from django.contrib.syndication.views import Feed
from blog.models import BlogPost

class RSSFeed(Feed):
    title = "My awesome blog feed"
    description = "The latest from my awesome blog"
    link = "/blog/"
    item_link = link

    def items(self):
        return BlogPost.objects.all()[:10]
    def item_description(self, item):
        return item.body
    def item_title(self, item):
        return item.title