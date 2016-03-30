# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateField(default=datetime.datetime(2015, 12, 9, 21, 51, 30, 809548))),
                ('comment', models.TextField(help_text=b'comment', null=True, blank=True)),
                ('host', models.TextField(help_text=b'Who is hosting', null=True, blank=True)),
                ('when', models.TextField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hairstyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hair_images', models.ImageField(null=True, upload_to=b'300')),
            ],
        ),
    ]
