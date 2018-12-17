from django.contrib.syndication.views import Feed

from blog.models import Post


class AllPostsRssFeed(Feed):

    title="Mu&Bai的博客"

    link='/'

    description='Mu%Bai的博客文章'

    def items(self):

        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s'%(item.category,item.title)
    def item_description(self, item):
        return item.body


