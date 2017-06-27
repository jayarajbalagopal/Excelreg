# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20170614_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('venue_id', models.CharField(max_length=3)),
                ('em_1', models.CharField(max_length=100)),
                ('em_2', models.CharField(max_length=100)),
                ('em_num_1', models.CharField(max_length=10, null=True)),
                ('em_num_2', models.CharField(max_length=10, null=True)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.IntegerField(default=0)),
                ('winner1', models.CharField(default=b'nil', max_length=10)),
            ],
            options={
                'verbose_name': 'events',
                'verbose_name_plural': 'events',
            },
        ),
    ]
