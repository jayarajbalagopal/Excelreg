# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20170615_0430'),
    ]

    operations = [
        migrations.DeleteModel(
            name='event',
        ),
        migrations.DeleteModel(
            name='venue',
        ),
    ]
