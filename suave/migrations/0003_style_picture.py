# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suave', '0002_auto_20150514_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='picture',
            field=models.ImageField(upload_to=b'img/styles', blank=True),
            preserve_default=True,
        ),
    ]
