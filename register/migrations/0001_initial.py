# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'userinfo',
                'verbose_name_plural': 'userinfos',
            },
        ),
    ]
