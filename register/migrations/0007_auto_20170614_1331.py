# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True),
        ),
    ]
