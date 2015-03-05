# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='followed_by', to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
    ]
