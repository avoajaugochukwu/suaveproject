# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0013_remove_order_fabric'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fabric',
            field=models.ForeignKey(to='suave.Fabric', null=True),
            preserve_default=True,
        ),
    ]
