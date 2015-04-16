# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0003_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fabric',
            name='image_url',
            field=models.CharField(default='no_image.png', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='fabric',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
