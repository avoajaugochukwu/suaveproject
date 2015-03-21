# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0009_order_main_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='main_order_id',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
    ]
