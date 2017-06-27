# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20170509_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='excelid',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
