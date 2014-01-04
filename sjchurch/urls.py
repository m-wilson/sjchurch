from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#import filer.server.urls

admin.autodiscover()

urlpatterns = patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     url(r'', include('django.contrib.staticfiles.urls')),
    # Examples:
    # url(r'^$', 'sjchurch.views.home', name='home'),
    # url(r'^sjchurch/', include('sjchurch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')), 
    url(r'^events/', include('events.urls')),  
    url(r'^people/', include('people.urls')),
    url(r'^', include('filer.server.urls')), 
    url(r'^', include('cms.urls')), # NB this is a 'catch all' pattern, if it is not placed last nothing that follows can ever be matched against!
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns