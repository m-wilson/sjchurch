from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
    # individual/detail

     url(r'^view/(?P<individual_slug>[-\w]+)/$',
         views.individualDetailView,
         name='individual-detail'),


)