# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0007_remove_size_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='tailor',
            name='address',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tailor',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tailor',
            name='rate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tailor',
            name='specialty',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
    ]
