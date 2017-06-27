# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20170510_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='excelid',
            field=models.CharField(default=b'excel', max_length=10, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
