# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(to='suave.Client', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='size',
            name='client',
            field=models.ForeignKey(to='suave.Client', null=True),
            preserve_default=True,
        ),
    ]
