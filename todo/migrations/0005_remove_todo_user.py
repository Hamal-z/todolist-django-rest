# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170421_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
