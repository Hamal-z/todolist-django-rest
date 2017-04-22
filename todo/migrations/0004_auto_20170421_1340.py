# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170418_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(default='3', max_length=2),
        ),
    ]
