from django.views.generic import UpdateView
from profiles.models import ImagerProfile
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import redirect_to_login
# @login_required
class ImagerProfileUpdateView(UpdateView):
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(ImagerProfileUpdateView, self).dispatch(
            request, *args, **kwargs)


    model = ImagerProfile
    template_name = 'profile_edit.html'
    fields = (
        'phone',
        'birthday',
        'picture_privacy',
        'phone_privacy',
        'birthday_privacy',
        'name_privacy',
        'email_privacy',
        'following',
        'blocking')
    success_url = reverse_lazy('profile')
