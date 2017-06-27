# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('venue_id', models.CharField(max_length=3, choices=[(b'201', b'201'), (b'202', b'202'), (b'301', b'301'), (b'302', b'302')])),
                ('em_1', models.CharField(max_length=100)),
                ('em_2', models.CharField(max_length=100)),
                ('em_num_1', models.CharField(max_length=10, null=True)),
                ('em_num_2', models.CharField(max_length=10, null=True)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.IntegerField(default=0)),
                ('winner1', models.CharField(default=b'nil', max_length=10)),
                ('winner2', models.CharField(default=b'nil', max_length=10)),
                ('winner3', models.CharField(default=b'nil', max_length=10)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='venue',
            fields=[
                ('venue_id', models.CharField(max_length=3, serialize=False, primary_key=True, choices=[(b'201', b'201'), (b'202', b'202'), (b'301', b'301'), (b'302', b'302')])),
                ('occupied', models.BooleanField(default=False)),
                ('vm_1', models.CharField(max_length=100)),
                ('vm_2', models.CharField(max_length=100)),
                ('vm_num_1', models.CharField(max_length=10, null=True)),
                ('vm_num_2', models.CharField(max_length=10, null=True)),
                ('current_event', models.CharField(default=b'Nil', max_length=6)),
                ('next_event', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name': 'venue',
                'verbose_name_plural': 'venues',
            },
        ),
    ]
