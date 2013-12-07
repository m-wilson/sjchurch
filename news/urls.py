from django.conf.urls import patterns, url
from news.models import Post
from news.views import helloWorld, newsItem
import feeds
import views


urlpatterns = patterns('',
    # RSS feed
    url(r'^feed/$',
        feeds.BasicNewsFeed(),
        name='feed'),
    url(r'^feed/(?P<slug>[-\w]+)/$',
        feeds.BasicNewsCategoryFeed(),
        name='category-feed'),

    # Pages
    url(r'^hello/$', helloWorld),
#    url(r'^$', newsItem), #REPLACE urls below with function based views- class based stuff is too hidden away!
    url(r'^$',
        views.PostListView.as_view(),
        name='post-list'),
    url(r'^category/(?P<slug>[-\w]+)/$',
        views.PostListCategoryView.as_view(),
        name='post-list-category'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.PostListMonthView.as_view(),
        name='post-list-month'),
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
#         views.PostDetailView.as_view(model=Post),
#         name='post-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',newsItem, name= 'post-detail'),
)
