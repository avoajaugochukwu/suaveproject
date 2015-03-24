# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0019_auto_20150324_1254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inches',
        ),
    ]
