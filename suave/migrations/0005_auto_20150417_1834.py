# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0004_auto_20150416_1250'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inches',
        ),
        migrations.RemoveField(
            model_name='size',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
