from django.shortcuts import render
from models import Photo
from django.views.generic import CreateView

# Create your views here.
class Add_Photo(CreateView):
    template_name = 'photo_add.html'
    model = Photo
    fields = (
        'image',
        'title',
        'description',
        'published')
