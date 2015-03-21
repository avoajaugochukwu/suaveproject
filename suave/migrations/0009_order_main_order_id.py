# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0008_auto_20150318_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='main_order_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
