# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0018_inches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inches',
            name='size',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
