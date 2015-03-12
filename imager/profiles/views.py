from django.views.generic import ListView, UpdateView
from profiles.models import ImagerProfile
from django.core.urlresolvers import reverse
# from profiles.forms import ImagerProfileEditForm

# class ImagerProfileListView(ListView):
#     model = ImagerProfile

class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    print 'HEEEEEEEEEERRRRRRRRRRRRREEEEEEEEEEEEEee'
    # fields = ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('profile')
