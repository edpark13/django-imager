from django.forms.models import ModelForm
from models import Photo

class CreatePhotoViewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        return super(CreatePhotoViewForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(CreatePhotoViewForm, self).save(*args, **kwargs)
        if self.request:
            obj.user = self.request
        obj.save()
        return obj

    class Meta:
        model = Photo
        fields = ['image',
                  'title',
                  'description',
                  'published',
                  ]
