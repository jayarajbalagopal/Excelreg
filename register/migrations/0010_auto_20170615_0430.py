# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20170615_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue_id',
            field=models.CharField(max_length=3, choices=[(b'201', b'201'), (b'202', b'202'), (b'301', b'301'), (b'302', b'302')]),
        ),
    ]
