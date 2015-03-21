# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0012_auto_20150321_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='fabric',
        ),
    ]
