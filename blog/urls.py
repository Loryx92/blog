from django.conf.urls import url
from .views import  *

app_name='blog'
urlpatterns=[
    url(r'^$',IndexViews.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)',PostDetailView.as_view(),name='detail'),

]
urlpatterns+=[
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9])+/$',CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9])+/$',TagView.as_view(),name='tag'),
    url(r'^full_width/$',full_width,name='full_width'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
]