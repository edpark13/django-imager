# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_imagerprofile_blocking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='blocking',
            field=models.ManyToManyField(related_name='blockers', to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='_followers', to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
    ]
