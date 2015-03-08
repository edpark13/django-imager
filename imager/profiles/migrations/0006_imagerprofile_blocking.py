# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150306_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='blocking',
            field=models.ManyToManyField(related_name='blocking_rel_+', to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
    ]
