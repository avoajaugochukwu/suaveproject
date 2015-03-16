# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0006_auto_20150316_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='client',
        ),
    ]
