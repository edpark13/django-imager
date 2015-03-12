from django.conf.urls import patterns, url
from views import Add_Photo
from django.contrib.auth.decorators import login_required



urlpatterns = patterns('', 
    url(r'^photo/add/$',
                           login_required(Add_Photo.as_view()),
                           name='photo_add'),
    )
