from django.conf.urls import patterns, url
from profiles.views import ImagerProfileUpdateView

urlpatterns = patterns('profiles.views',
    # url(r'^$', ImagerProfileListView.as_view(), name='profile_list'),
    url(r'^edit/(?P<pk>\d+)/$', ImagerProfileUpdateView.as_view(), name='profile_edit')
)
