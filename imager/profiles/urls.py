from django.conf.urls import patterns, url
from profiles.views import ImagerProfileUpdateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('profiles.views',
    # url(r'^$', ImagerProfileListView.as_view(), name='profile_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ImagerProfileUpdateView.as_view()), name='profile_edit')
)
