from django.conf.urls import patterns, url
from profile.views import ImagerProfileListView, ImagerProfileUpdateView

urlpatterns = patterns('profiles.views',
    url(r'^$', ImagerProfileListView.as_view(), name='profile_list'),
    # url(r'^(?P<pk>\d+)/edit/$', ImagerProfileUpdateView.as_view(), name='profile_edit')
)
