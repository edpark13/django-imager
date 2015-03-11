from django.conf.urls import patterns, include, url
from django.contrib import admin
from imager import views
from imager import settings
from django.conf import settings as dcs
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'imager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',),
    url(r'^profile/', 'imager.views.profile', name='profile'),
    url(r'^library/', 'imager.views.library', name='library'),
    url(r'^stream/', 'imager.views.stream', name='stream'),
    url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^profile/', include('profiles.urls')),
)
if settings.DEBUG:
    urlpatterns += static(dcs.MEDIA_URL, document_root=dcs.MEDIA_ROOT)
