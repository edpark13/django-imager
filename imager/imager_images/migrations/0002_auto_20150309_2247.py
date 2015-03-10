# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='published',
            field=models.CharField(default=b'pri', max_length=4, choices=[(b'pub', b'public'), (b'pri', b'private'), (b'sha', b'shared')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='albums',
            name='title',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(default=b'pri', max_length=4, choices=[(b'pub', b'public'), (b'pri', b'private'), (b'sha', b'shared')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
    ]
