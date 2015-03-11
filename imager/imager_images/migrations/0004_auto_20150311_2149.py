# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='profile',
            field=models.ForeignKey(related_name='albums', to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=b'photos/test'),
            preserve_default=True,
        ),
    ]
