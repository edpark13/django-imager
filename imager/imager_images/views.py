from django.core.urlresolvers import reverse_lazy, reverse
from models import Photo, Albums
from django.views.generic import CreateView, UpdateView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from forms import CreatePhotoViewForm

# @login_required
class Add_Photo(CreateView):
    form_class = CreatePhotoViewForm
    # model = Photo
    # template_name = 'photo_add.html'
    def get_form_kwargs(self):
        kwargs = super(Add_Photo, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('library', kwargs={'pk': self.object.pk})
    template_name = 'photo_add.html'
    model = Photo
    success_url = reverse_lazy('library')

# @login_required
class PhotoEditUpdateView(UpdateView):
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(PhotoEditUpdateView, self).dispatch(
            request, *args, **kwargs)
    model = Photo
    template_name = 'photo_edit.html'
    success_url = reverse_lazy('library')

# @login_required
class AlbumEditUpdateView(UpdateView):
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(AlbumEditUpdateView, self).dispatch(
            request, *args, **kwargs)
    model = Albums
    template_name = 'album_edit.html'
    success_url = reverse_lazy('library')

# @login_required
class Add_Album(CreateView):
    template_name = 'album_add.html'
    model = Albums
    success_url = reverse_lazy('library')
