from django.conf.urls import patterns, include, url
from django.contrib import admin
from imager import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'imager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',),
    url(r'^restricted/', views.restricted, name='restricted'),
)
