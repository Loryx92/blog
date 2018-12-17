from django.conf.urls import url

from .views import *

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',post_comment, name='post_comment'),

]