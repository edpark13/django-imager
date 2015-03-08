# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20150306_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now=True)),
                ('published', models.CharField(default=b'private', max_length=3, choices=[(b'pub', b'public'), (b'pri', b'private'), (b'sha', b'shared')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'photos/%Y/%m/%d')),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now=True)),
                ('published', models.CharField(default=b'private', max_length=3, choices=[(b'pub', b'public'), (b'pri', b'private'), (b'sha', b'shared')])),
                ('profile', models.ForeignKey(related_name='photos', to='profiles.ImagerProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='albums',
            name='cover',
            field=models.ForeignKey(blank=True, to='imager_images.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albums',
            name='photos',
            field=models.ManyToManyField(related_name='album', to='imager_images.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albums',
            name='profile',
            field=models.ForeignKey(to='profiles.ImagerProfile'),
            preserve_default=True,
        ),
    ]
