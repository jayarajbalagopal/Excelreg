# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20170509_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='excelid',
            field=models.CharField(max_length=10),
        ),
    ]
