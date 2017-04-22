# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170418_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
