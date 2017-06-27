# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AddField(
            model_name='event',
            name='winner2',
            field=models.CharField(default=b'nil', max_length=10),
        ),
        migrations.AddField(
            model_name='event',
            name='winner3',
            field=models.CharField(default=b'nil', max_length=10),
        ),
        migrations.AlterField(
            model_name='venue',
            name='current_event',
            field=models.CharField(default=b'Nil', max_length=6),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True, choices=[(b'201', b'201'), (b'202', b'202'), (b'301', b'301'), (b'302', b'302')]),
        ),
    ]
