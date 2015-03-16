from django.core.urlresolvers import reverse_lazy
from models import Photo, Albums
from django.views.generic import CreateView, UpdateView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from profiles.models import ImagerProfile

class Add_Photo(CreateView):
    model = Photo
    fields = ['title', 'description', 'image', 'published']
    template_name = 'photo_add.html'

    def form_valid(self, form):
        form.instance.profile = ImagerProfile.objects.get(
            pk=self.request.user.profile.id)
        return super(Add_Photo, self).form_valid(form)

    success_url = reverse_lazy('library')


class PhotoEditUpdateView(UpdateView):
    model = Photo
    fields = ['title', 'description', 'published']
    template_name = 'photo_edit.html'
    def dispatch(self, request, *args, **kwargs):
        photo_profile = Photo.objects.get(id=int(self.kwargs['pk'])).profile
        user_profile = ImagerProfile.objects.get(user=self.request.user)
        if photo_profile != user_profile:
            return redirect('/accounts/login/')
        return super(PhotoEditUpdateView, self).dispatch(request, *args, **kwargs)
    success_url = reverse_lazy('library')

class AlbumEditUpdateView(UpdateView):
    model = Photo
    fields = ['title', 'description', 'published']
    template_name = 'photo_edit.html'
    def dispatch(self, request, *args, **kwargs):
        photo_profile = Photo.objects.get(id=int(self.kwargs['pk'])).profile
        user_profile = ImagerProfile.objects.get(user=self.request.user)
        if photo_profile != user_profile:
            return redirect('/accounts/login/')
        return super(PhotoEditUpdateView, self).dispatch(request, *args, **kwargs)
    success_url = reverse_lazy('library')

# @login_required
class Add_Album(CreateView):
    model = Albums
    fields = ['title', 'description', 'photos', 'cover', 'published']
    template_name = 'album_add.html'

    def form_valid(self, form):
        form.instance.profile = ImagerProfile.objects.get(
            pk=self.request.user.profile.id)
        return super(Add_Album, self).form_valid(form)

    success_url = reverse_lazy('library')
