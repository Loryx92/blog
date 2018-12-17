from django import template
from django.db.models import Count

from ..models import Post, Category, Tag

register=template.Library()
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-created_time")[:num]

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag()
def get_categories():
    # 引入count函数,计算分类下的文章数,过滤掉文章数小于1的分类
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)