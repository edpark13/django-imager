# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(height_field=b'100px', width_field=b'100px', upload_to=b'profile_images', blank=True)),
                ('phone', models.IntegerField(max_length=11)),
                ('birthday', models.DateField()),
                ('picture_privacy', models.BooleanField(default=True)),
                ('phone_privacy', models.BooleanField(default=True)),
                ('birthday_privacy', models.BooleanField(default=True)),
                ('name_privacy', models.BooleanField(default=True)),
                ('email_privacy', models.BooleanField(default=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
