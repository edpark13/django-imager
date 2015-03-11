# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20150306_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='birthday',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='blocking',
            field=models.ManyToManyField(related_name='blockers', null=True, to='profiles.ImagerProfile', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='_followers', null=True, to='profiles.ImagerProfile', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone',
            field=models.IntegerField(max_length=11, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='picture',
            field=models.ImageField(default=b'photos/test/packman_2.jpg', null=True, upload_to=b'photos/test', blank=True),
            preserve_default=True,
        ),
    ]
