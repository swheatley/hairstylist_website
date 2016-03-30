# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_delete_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hairstyle',
        ),
    ]
