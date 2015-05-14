# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tailor',
            name='phone_number',
            field=models.CharField(default=0, max_length=13),
            preserve_default=True,
        ),
    ]
