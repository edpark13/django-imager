from django.shortcuts import render
from models import Photo, Albums
from django.views.generic import CreateView, UpdateView

# Create your views here.
class Add_Photo(CreateView):
    template_name = 'photo_add.html'
    model = Photo
    fields = (
        'image',
        'title',
        'description',
        'published')

class PhotoEditUpdateView(UpdateView):
    model = Photo
    template_name = 'photo_edit.html'

class AlbumEditUpdateView(UpdateView):
    model = Albums
    template_name = 'album_edit.html'
