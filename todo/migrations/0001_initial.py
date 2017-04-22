# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('tid', models.IntegerField(default=1, serialize=False, primary_key=True)),
                ('todo', models.CharField(max_length=50)),
                ('flag', models.CharField(default='1', max_length=2)),
                ('priority', models.CharField(max_length=2)),
                ('pubtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
                ('lastdate', models.DateTimeField(verbose_name='最后修改日期', auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority', 'pubtime'],
            },
        ),
    ]
