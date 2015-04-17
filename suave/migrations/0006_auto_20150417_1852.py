# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0005_auto_20150417_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='style',
            name='image_url',
            field=models.CharField(default='no_image.png', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='style',
            name='pattern',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
    ]
