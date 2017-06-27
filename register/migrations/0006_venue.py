# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20170512_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue',
            fields=[
                ('venue_id', models.IntegerField(max_length=3, serialize=False, primary_key=True)),
                ('occupied', models.BooleanField(default=False)),
                ('vm_1', models.CharField(max_length=100)),
                ('vm_2', models.CharField(max_length=100)),
                ('vm_num_1', models.CharField(max_length=10, null=True)),
                ('vm_num_2', models.CharField(max_length=10, null=True)),
                ('current_event', models.CharField(default=b'No ongoing event', max_length=6)),
                ('next_event', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'venue',
                'verbose_name_plural': 'venues',
            },
        ),
    ]
